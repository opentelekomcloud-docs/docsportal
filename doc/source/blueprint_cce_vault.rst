=============================================
(No) Secret Zero with CCE and Hashicorp Vault
=============================================

With centralized secret management it becomes unnecessary to keep secrets used
by various application spreaded across DevOps environments. This helps to close
some security attack vectors, but usually introduces a problem of the so-called
Secret Zero as a key to the key storage.

This article demonstrates how to utilize Infrastructure authorization of the
HashiCorp Vault with CCE on an example of deploying Zookeeper cluster with
enabled TLS protection. Certificates for Zookeeper are stored in Vault where
they oblige required practices (rotation, audit, etc).

Overview
========

.. graphviz:: dot/cce_vault_overview.dot
   :caption: CCE and Vault overview
   :layout: dot

TLS secrets are kept in the Vault. They are being read by Vault Agent component
running in the every pod of Zookeeper service, where it writes certificates
onto the file system where Zookeeper expectes them and also updates
certificates once they got changed in Vault allowing rotation without service
interuption. Agent is configured to use password-less access to Vault.

Establishing trust between CCE and Vault
========================================

Before any application from the CCE is able to login to vault relying on
infrastructure based authentication it is required to do some steps on the
Vault side. Kubernetes authentication plugin is enabled and configured to only
access requests from specific Kubernetes cluster by providing it's Certificate
Authority. To allow further multiple different CCE clusters to use vault a
dedicated auth path is going to be used.

.. code-block:: shell

   $ vault auth enable -path kubernetes_cce1 kubernetes
   $ vault write auth/kubernetes_cce1/config \
       kubernetes_host="$K8S_HOST" \
       kubernetes_ca_cert="$SA_CA_CRT"

Since in our example a dedicated service account with token is being
periodically rotated using `client JWT as reviewer JWT
<https://www.vaultproject.io/docs/auth/kubernetes#use-the-vault-client-s-jwt-as-the-reviewer-jwt>`_
can be used.

Access rules for Vault
======================

Once Auth plugin is enabled CCE workloads are able to authenticate to Vault,
but they can do nothing. It is now necessary to establish further level of
authorization and let particular service account of CCE to get access to
secrets in vault.

For the scope of the use case we are going to allow zookeeper service account
from zookeeper namespace to get access to the TLS secrets stored in vault (KV
storage). For that a policy that gives a read only access to the /tls/zk* and
/tls/ca paths is being created.

.. code-block:: shell

   $ vault policy write tls-zk-ro - <<EOF
   path "secret/data/tls/zk_*" {capabilities = ["read"] }
   path "secret/data/tls/ca" {capabilities = ["read"] }
   path "secret/metadata/tls/zk_*" {capabilities = ["read"] }
   path "secret/metadata/tls/ca" {capabilities = ["read"] }
   EOF

Next granting the policy to the particular requestor (zookeeper
service account in zookeeper namespace) must be done.

.. code-block:: shell

   $ vault write auth/kubernetes_cce1/role/zookeeper \
       bound_service_account_names=zookeeper \
       bound_service_account_namespaces=zookeeper \
       policies=tls-zk-ro \
       ttl=2h

With this done token of the service account zookeeper in the zookeeper
namespace would be able to access to the vault for reading secrets located
under `/secret/tls` path. And since it is higly recommended to follow the least
required privilege principle only read only access to the TLS data is granted.
A time to live of 3 hours is being used here meaning that once application
authorize to Vault the token it gets can be used during next 2 hours. This need
to be carefully aligned with the time to live or the service account token to
minimize their overlap. It is advised to keep it relatively short.

This is one the most sensitive steps in the whole configuration, since it can
not be generally excluded that the applications deployed in the Kubernetes find
escape or be compromised. For that case it is required to strictly limit amount
of secrets accessor will be able to read.

Populating secrets in Vault
===========================

Within Vault there are 2 possibilities to access TLS certificates:

* Store certificate data in the `KeyValue store
  <https://www.vaultproject.io/docs/secrets/kv/kv-v2>`_

* Use `PKI secrets engine <https://www.vaultproject.io/docs/secrets/pki>`_ to
  issue certificates

Vault enables users not only to store TLS certificates data in the KV store,
but also to create and  revoke them. To keep this tutorial simple enough we are
not going to do this and only upload generated certificates into the KV store.
A lesson on improving that is left to the reader.

.. code-block:: shell

   $ vault kv put secret/tls/ca certificate=@ca.crt
   $ vault kv put secret/tls/zk_server certificate=@zk_server.crt private_key=@zk_server.key
   $ vault kv put secret/tls/zk_client certificate=@zk_client.crt private_key=@zk_client.key

Deploying Zookeeper
===================

Now that the secrets are stored safely in Vault and only allowed applications
can fetch them it is time to look how exactly the application accesses the
secrets. Generally utilizing Vault requires modification of the application.
`Vault agent <https://www.vaultproject.io/docs/agent>`_ is a tool that was
created to simplify secrets delivery for applications where it is hard or
impossible to change the application itself.  Agent is taking care of reading
secrets from Vault and can deliver them to the file system.

1. Create a Kubernetes namespace named `zookeeper`.

.. code-block:: shell

   $ kubectl create namespace zookeeper

2. Create a Kubernetes service account named `zookeeper`.

.. code-block:: shell

   $ kubectl create serviceaccount zookeeper

3. In Kubernetes a *service account* provides an identity for the services
   running in the POD so that the process can access Kubernetes API. The same
   identity can be used to access Vault, but require one special permission -
   access to the tokenreview API. If a dedicated reviewer JWT is used this step
   is not necessary, but it also mean a long-living sensitive data is being
   used and permanently transferred over the network. More details on various
   ways to use Kubernetes token to authorize to Vault `can be found here
   <https://www.vaultproject.io/docs/auth/kubernetes#how-to-work-with-short-lived-kubernetes-tokens>`_.

.. code-block:: yaml
   :caption: role-binding.yaml

   ---
   apiVersion: rbac.authorization.k8s.io/v1
   kind: ClusterRoleBinding
   metadata:
     name: role-tokenreview-binding
     namespace: default
   roleRef:
     apiGroup: rbac.authorization.k8s.io
     kind: ClusterRole
     name: system:auth-delegator
   subjects:
     - kind: ServiceAccount
       name: zookeeper
       namespace: zookeeper

.. code-block:: shell

   $ kubectl apply --filename role-binding.yaml

4. Create Kubernetes ConfigMap with all required configurations

.. code-block:: yaml
   :caption: zookeeper-cm.yaml

   ---
   apiVersion: v1
   kind: ConfigMap
   metadata:
     name: zookeeper-config
     namespace: "zookeeper"
   data:
     ok: |
       #!/bin/sh
       # This sript is used by live-check of Kubernetes pod
       if [ -f /tls/ca.pem ]; then
         echo "srvr" | openssl s_client -CAfile /tls/ca.pem -cert /tls/client/tls.crt -key /tls/client/tls.key -connect 127.0.0.1:${1:-2281} -quiet -ign_eof 2>/dev/null | grep Mode

       else
         zkServer.sh status
       fi

     ready: |
       #!/bin/sh
       # This sript is used by readiness-check of Kubernetes pod
       if [ -f /tls/ca.pem ]; then
         echo "ruok" | openssl s_client -CAfile /tls/ca.pem -cert /tls/client/tls.crt -key /tls/client/tls.key -connect 127.0.0.1:${1:-2281} -quiet -ign_eof 2>/dev/null
       else
         echo ruok | nc 127.0.0.1 ${1:-2181}
       fi

     run: |
       #!/bin/bash
       # This is the main starting script
       set -a
       ROOT=$(echo /apache-zookeeper-*)
       ZK_USER=${ZK_USER:-"zookeeper"}
       ZK_LOG_LEVEL=${ZK_LOG_LEVEL:-"INFO"}
       ZK_DATA_DIR=${ZK_DATA_DIR:-"/data"}
       ZK_DATA_LOG_DIR=${ZK_DATA_LOG_DIR:-"/data/log"}
       ZK_CONF_DIR=${ZK_CONF_DIR:-"/conf"}
       ZK_CLIENT_PORT=${ZK_CLIENT_PORT:-2181}
       ZK_SSL_CLIENT_PORT=${ZK_SSL_CLIENT_PORT:-2281}
       ZK_SERVER_PORT=${ZK_SERVER_PORT:-2888}
       ZK_ELECTION_PORT=${ZK_ELECTION_PORT:-3888}
       ID_FILE="$ZK_DATA_DIR/myid"
       ZK_CONFIG_FILE="$ZK_CONF_DIR/zoo.cfg"
       LOG4J_PROPERTIES="$ZK_CONF_DIR/log4j.properties"
       HOST=$(hostname)
       DOMAIN=`hostname -d`
       APPJAR=$(echo $ROOT/*jar)
       CLASSPATH="${ROOT}/lib/*:${APPJAR}:${ZK_CONF_DIR}:"
       if [[ $HOST =~ (.*)-([0-9]+)$ ]]; then
           NAME=${BASH_REMATCH[1]}
           ORD=${BASH_REMATCH[2]}
           MY_ID=$((ORD+1))
       else
           echo "Failed to extract ordinal from hostname $HOST"
           exit 1
       fi
       mkdir -p $ZK_DATA_DIR
       mkdir -p $ZK_DATA_LOG_DIR
       echo $MY_ID >> $ID_FILE

       echo "dataDir=$ZK_DATA_DIR" >> $ZK_CONFIG_FILE
       echo "dataLogDir=$ZK_DATA_LOG_DIR" >> $ZK_CONFIG_FILE
       echo "4lw.commands.whitelist=*" >> $ZK_CONFIG_FILE
       # Client TLS configuration
       if [[ -f /tls/ca.pem ]]; then
         echo "secureClientPort=$ZK_SSL_CLIENT_PORT" >> $ZK_CONFIG_FILE
         echo "ssl.keyStore.location=/tls/client/client.pem" >> $ZK_CONFIG_FILE
         echo "ssl.trustStore.location=/tls/ca.pem" >> $ZK_CONFIG_FILE
       else
         echo "clientPort=$ZK_CLIENT_PORT" >> $ZK_CONFIG_FILE
       fi
       # Server TLS configuration
       if [[ -f /tls/ca.pem ]]; then
         echo "serverCnxnFactory=org.apache.zookeeper.server.NettyServerCnxnFactory" >> $ZK_CONFIG_FILE
         echo "sslQuorum=true" >> $ZK_CONFIG_FILE
         echo "ssl.quorum.keyStore.location=/tls/server/server.pem" >> $ZK_CONFIG_FILE
         echo "ssl.quorum.trustStore.location=/tls/ca.pem" >> $ZK_CONFIG_FILE
       fi
       for (( i=1; i<=$ZK_REPLICAS; i++ ))
       do
           echo "server.$i=$NAME-$((i-1)).$DOMAIN:$ZK_SERVER_PORT:$ZK_ELECTION_PORT" >> $ZK_CONFIG_FILE
       done
       rm -f $LOG4J_PROPERTIES
       echo "zookeeper.root.logger=$ZK_LOG_LEVEL, CONSOLE" >> $LOG4J_PROPERTIES
       echo "zookeeper.console.threshold=$ZK_LOG_LEVEL" >> $LOG4J_PROPERTIES
       echo "zookeeper.log.threshold=$ZK_LOG_LEVEL" >> $LOG4J_PROPERTIES
       echo "zookeeper.log.dir=$ZK_DATA_LOG_DIR" >> $LOG4J_PROPERTIES
       echo "zookeeper.log.file=zookeeper.log" >> $LOG4J_PROPERTIES
       echo "zookeeper.log.maxfilesize=256MB" >> $LOG4J_PROPERTIES
       echo "zookeeper.log.maxbackupindex=10" >> $LOG4J_PROPERTIES
       echo "zookeeper.tracelog.dir=$ZK_DATA_LOG_DIR" >> $LOG4J_PROPERTIES
       echo "zookeeper.tracelog.file=zookeeper_trace.log" >> $LOG4J_PROPERTIES
       echo "log4j.rootLogger=\${zookeeper.root.logger}" >> $LOG4J_PROPERTIES
       echo "log4j.appender.CONSOLE=org.apache.log4j.ConsoleAppender" >> $LOG4J_PROPERTIES
       echo "log4j.appender.CONSOLE.Threshold=\${zookeeper.console.threshold}" >> $LOG4J_PROPERTIES
       echo "log4j.appender.CONSOLE.layout=org.apache.log4j.PatternLayout" >> $LOG4J_PROPERTIES
       echo "log4j.appender.CONSOLE.layout.ConversionPattern=%d{ISO8601} [myid:%X{myid}] - %-5p [%t:%C{1}@%L] - %m%n" >> $LOG4J_PROPERTIES
       if [ -n "$JMXDISABLE" ]
       then
           MAIN=org.apache.zookeeper.server.quorum.QuorumPeerMain
       else
           MAIN="-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=$JMXPORT -Dcom.sun.management.jmxremote.authenticate=$JMXAUTH -Dcom.sun.management.jmxremote.ssl=$JMXSSL -Dzookeeper.jmx.log4j.disable=$JMXLOG4J org.apache.zookeeper.server.quorum.QuorumPeerMain"
       fi
       set -x
       exec java -cp "$CLASSPATH" $JVMFLAGS $MAIN $ZK_CONFIG_FILE

     vault-agent-config.hcl: |
       exit_after_auth = true
       pid_file = "/home/vault/pidfile"
       auto_auth {
           method "kubernetes" {
               mount_path = "auth/kubernetes_cce1"
               config = {
                   role = "zookeeper"
                   token_path = "/run/secrets/tokens/vault-token"
               }
           }
           sink "file" {
               config = {
                   path = "/home/vault/.vault-token"
               }
           }
       }

       cache {
           use_auto_auth_token = true
       }

       # ZK is neat-picky on cert file extensions
       template {
         destination = "/tls/ca.pem"
         contents = <<EOT
       {{- with secret "/secret/data/tls/ca" }}{{ .Data.data.certificate }}{{ end }}
       EOT
       }

       template {
         destination = "/tls/server/server.pem"
         contents = <<EOT
       {{- with secret "{{ zookeeper.vault_server_cert_path }}" }}{{ .Data.data.certificate }}
       {{ .Data.data.private_key }}{{ end }}
       EOT
       }
       template {
         destination = "/tls/server/tls.crt"
         contents = <<EOT
       {{- with secret "{{ zookeeper.vault_server_cert_path }}" }}{{ .Data.data.certificate }}{{ end }}
       EOT
       }
       template {
         destination = "/tls/server/tls.key"
         contents = <<EOT
       {{- with secret "{{ zookeeper.vault_server_cert_path }}" }}{{ .Data.data.private_key }}{{ end }}
       EOT
       }

       template {
         destination = "/tls/client/client.pem"
         contents = <<EOT
       {{- with secret "{{ zookeeper.vault_client_cert_path }}" }}{{ .Data.data.certificate }}
       {{ .Data.data.private_key }}{{ end }}
       EOT
       }
       template {
         destination = "/tls/client/tls.crt"
         contents = <<EOT
       {{- with secret "{{ zookeeper.vault_client_cert_path }}" }}{{ .Data.data.certificate }}{{ end }}
       EOT
       }
       template {
         destination = "/tls/client/tls.key"
         contents = <<EOT
       {{- with secret "{{ zookeeper.vault_client_cert_path }}" }}{{ .Data.data.private_key }}{{ end }}
       EOT
       }

.. code-block:: bash

   $ kubectl apply -f zookeeper-cm.yaml

5. Create Zookeeper Headless service to be used by pod to build quorum

.. code-block:: yaml
   :caption: zookeeper-svc.yaml

    ---
    name: "zookeeper-svc"
    namespace: "zookeeper"
    apiVersion: v1
    kind: Service
    spec:
      # Not exposing in the cluster
      clusterIP: None
      # Important to start up
      publishNotReadyAddresses: true
      selector:
        app: zookeeper
      ports:
      - port: 2281
        name: client
        targetPort: client
        protocol: TCP
      - port: 2888
        name: server
        targetPort: server
        protocol: TCP
      - port: 3888
        name: election
        targetPort: election
        protocol: TCP

.. code-block:: bash

   $ kubectl apply -f zookeeper-svc.yaml

6. Create Frontend service

.. code-block:: yaml
   :caption: zookeeper-svc-public.yaml

   apiVersion: v1
   kind: Service
   spec:
     clusterIP: None
     ports:
     - name: client
       port: 2281
       protocol: TCP
       targetPort: client
     selector:
       app: zookeeper
     sessionAffinity: None
     type: ClusterIP

.. code-block:: bash

   $ kubectl apply -f zookeeper-svc-public.yaml

7. Create StatefulSet replacing `<VAULT_PUBLIC_ADDR>` with address of available
   vault server

.. code-block:: yaml
   :caption: zookeeper-ss.yaml

   apiVersion: apps/v1
   kind: StatefulSet
   spec:
     podManagementPolicy: Parallel
     replicas: 3
     selector:
       matchLabels:
         app: zookeeper
         component: server
     serviceName: zookeeper-headless
     template:
       metadata:
         labels:
           app: zookeeper
           component: server
       spec:
         containers:

         - args:
           - agent
           - -config=/etc/vault/vault-agent-config.hcl
           - -log-level=debug
           - -exit-after-auth=false
           env:
           - name: VAULT_ADDR
             value: <VAULT_PUBLIC_ADDR>
           image: vault:1.9.0
           name: vault-agent-sidecar
           volumeMounts:
           - mountPath: /etc/vault
             name: vault-agent-config
           - mountPath: /tls
             name: cert-data
           - mountPath: /var/run/secrets/tokens
             name: k8-tokens

         - command:
           - /bin/bash
           - -xec
           - /config-scripts/run
           env:
           - name: ZK_REPLICAS
             value: "3"
           - name: ZOO_PORT
             value: "2181"
           - name: ZOO_STANDALONE_ENABLED
             value: "false"
           - name: ZOO_TICK_TIME
             value: "2000"
           image: zookeeper:3.7.0
           livenessProbe:
             exec:
               command:
               - sh
               - /config-scripts/ok
             failureThreshold: 2
             initialDelaySeconds: 20
             periodSeconds: 30
             successThreshold: 1
             timeoutSeconds: 5
           name: zookeeper
           ports:
           - containerPort: 2281
             name: client
             protocol: TCP
           - containerPort: 2888
             name: server
             protocol: TCP
           - containerPort: 3888
             name: election
             protocol: TCP
           readinessProbe:
             exec:
               command:
               - sh
               - /config-scripts/ready
             failureThreshold: 2
             initialDelaySeconds: 20
             periodSeconds: 30
             successThreshold: 1
             timeoutSeconds: 5
           securityContext:
             runAsUser: 1000
           volumeMounts:
           - mountPath: /data
             name: datadir
           - mountPath: /tls
             name: cert-data
           - mountPath: /config-scripts
             name: zookeeper-config
         dnsPolicy: ClusterFirst

         initContainers:
         - args:
           - agent
           - -config=/etc/vault/vault-agent-config.hcl
           - -log-level=debug
           - -exit-after-auth=true
           env:
           - name: VAULT_ADDR
             value: <VAULT_PUBLIC_ADDR>
           image: vault:1.9.0
           name: vault-agent
           volumeMounts:
           - mountPath: /etc/vault
             name: vault-agent-config
           - mountPath: /tls
             name: cert-data
           - mountPath: /var/run/secrets/tokens
             name: k8-tokens
         restartPolicy: Always
         serviceAccount: zookeeper
         serviceAccountName: zookeeper
         terminationGracePeriodSeconds: 1800
         volumes:
         - configMap:
             defaultMode: 420
             items:
             - key: vault-agent-config.hcl
               path: vault-agent-config.hcl
             name: zookeeper-config
           name: vault-agent-config
         - configMap:
             defaultMode: 365
             name: zookeeper-config
           name: zookeeper-config
         - emptyDir: {}
           name: cert-data
         - name: k8-tokens
           projected:
             defaultMode: 420
             sources:
             - serviceAccountToken:
                 expirationSeconds: 7200
                 path: vault-token

     updateStrategy:
       type: RollingUpdate
     volumeClaimTemplates:
     - apiVersion: v1
       kind: PersistentVolumeClaim
       metadata:
         name: datadir
       spec:
         accessModes:
         - ReadWriteOnce
         resources:
           requests:
             storage: 5Gi
         storageClassName: csi-disk
         volumeMode: Filesystem

.. code-block:: bash

   $ kubectl apply -f zookeeper-ss.yaml

With this a production ready Zookeeper service with enabled TLS has been
deployed sucessfully to the CCE. Vault agent takes care of authorizing to
HashiCorp Vault using Kubernetes service account with short time to live token
and fetches required secrets to the filesystem. In the whole Kubernetes
deployment there are no secrets for the application, neither key to the Vault,
not TLS certificates themselves. Even usage of Kubernetes secrets is not
required with this pattern.

References
==========

* https://learn.hashicorp.com/tutorials/vault/agent-kubernetes?in=vault/app-integration

* https://learn.hashicorp.com/tutorials/vault/agent-kubernetes?in=vault/auth-methods

* https://www.vaultproject.io/docs/auth/kubernetes
