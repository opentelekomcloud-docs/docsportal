:orphan:

========================
Connection Configuration
========================

You can connect to the Open Telekom Cloud and OpenStack clouds in general
using two approaches. The first one uses a credential file called
``clouds.yaml`` and the other one is to use ``environment variables``.

.. _clouds-yaml:

Configuring a clouds.yaml file
------------------------------

The credential file ``clouds.yaml`` will be queried automatically in different
locations with increasing precedence:

1. system-wide (/etc/openstack/{clouds,secure}.yaml)
2. Home directory / user space (~/.config/openstack/{clouds,secure}.yaml)
3. Current directory (./{clouds,secure}.yaml)

A sample clouds.yaml file is listed below to connect with Open Telekom Cloud:

**clouds.yaml**

.. code-block:: yaml

  clouds:
    otc:
      profile: otc
      auth:
        username: '<USER_NAME>'
        password: '<PASSWORD>'
        project_name: '<eu-de_project>'
        # or project_id: '<123456_PROJECT_ID>'
        user_domain_name: 'OTC00000000001000000xxx'
        # or user_domain_id: '<123456_DOMAIN_ID>'
        auth_url: 'https://iam.eu-de.otc.t-systems.com:443/v3'
      interface: 'public'
      identity_api_version: 3 # !Important
      ak: '<AK_VALUE>' # AK/SK pair for access to OBS
      sk: '<SK_VALUE>'

.. note::
   The name ``otc`` is self-defined and can be changed to any value.

AK/SK values required for access to some services (i.e. OBS) can
be either configured as shown above in the clouds.yaml/secure.yaml, or
they can be automatically retrieved from the S3_ACCESS_KEY_ID and
S3_SECRET_ACCESS_KEY.

Test your connection
^^^^^^^^^^^^^^^^^^^^

If you followed the `installation advices <index>`_ for your specific
operating system, you can use the following command to test the basic
functionality.

.. code-block:: bash

    $ openstack --os-cloud otc flavor list


Configuration of a Second Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Additional connections to other Openstack-clouds or -projects can be added
to the file as shown below:

**clouds.yaml**

.. code-block:: yaml

  clouds:
    otcfirstproject:
      profile: otc
      auth:
        username: '<USER_NAME>'
        password: '<PASSWORD>'
        project_name: '<eu-de_project>'
        # or project_id: '<123456_PROJECT_ID>'
        user_domain_name: 'OTC00000000001000000xxx'
        # or user_domain_id: '<123456_DOMAIN_ID>'
        auth_url: 'https://iam.eu-de.otc.t-systems.com:443/v3'
      interface: 'public'
      identity_api_version: 3 # !Important
      ak: '<AK_VALUE>' # AK/SK pair for access to OBS
      sk: '<SK_VALUE>'
    otcsecondproject:
      profile: otc
      auth:
       username: '<USER_NAME>'
        password: '<PASSWORD>'
        project_name: '<eu-de_project2>'
        # or project_id: '<123456_PROJECT_ID2>'
        user_domain_name: 'OTC00000000001000000xxx'
        # or user_domain_id: '<123456_DOMAIN_ID2>'
        auth_url: 'https://iam.eu-de.otc.t-systems.com:443/v3'
      interface: 'public'
      identity_api_version: 3 # !Important
      ak: '<AK_VALUE>' # AK/SK pair for access to OBS
      sk: '<SK_VALUE>'

Splitting the credentials in clouds.yaml and secure.yaml
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In some scenarios a split of security credentials from the configuration file
is necessary. The optional file ``secure.yaml`` can be used to store the
secret which is left out from ``clouds.yaml``:

**clouds.yaml**

.. code-block:: yaml

  clouds:
    otc:
      profile: otc
      auth:
        username: '<USER_NAME>'
        project_name: '<eu-de_project>'
        # or project_id: '<123456_PROJECT_ID>'
        user_domain_name: 'OTC00000000001000000xxx'
        # or user_domain_id: '<123456_DOMAIN_ID>'
        auth_url: 'https://iam.eu-de.otc.t-systems.com:443/v3'
      interface: 'public'
      identity_api_version: 3 # !Important

**secure.yaml**

.. code-block:: yaml

  clouds:
    otc:
      auth:
        password: '<PASSWORD>'
      ak: '<AK_VALUE>' # AK/SK pair for access to OBS
      sk: '<SK_VALUE>'


.. _environment-variables:

Agency based authorization
^^^^^^^^^^^^^^^^^^^^^^^^^^

Open Telekom Cloud supports a concept of agencies. One domain delegates access
to resources to another domain. After trust relationship is established the
following configuration can be used in ``clouds.yaml``:

.. code-block:: yaml

  clouds:
    otc:
      profile: otc
      auth_type: agency
      auth:
        username: '<USER_NAME>'
        project_name: '<eu-de_project>'
        # or project_id: '<123456_PROJECT_ID>'
        user_domain_name: 'OTC00000000001000000xxx'
        # or user_domain_id: '<123456_DOMAIN_ID>'
        auth_url: 'https://iam.eu-de.otc.t-systems.com:443/v3'
        target_domain_id: '<123456_DOMAIN_ID>' # Domain where agency is created
        # or target_domain_name: '<123456_DOMAIN_NAME'
        target_agency_name: 'test_agency' # name of the agency
        target_project_name: '<123456_PROJECT_NAME>' # project scoped operations
        # or target_project_id: '<123456_PROJECT_ID>'
        # When target_project_xx is not set - domain scope is selected

Configuration of Environment Variables
--------------------------------------

Historically OpenStack tools are supporting configuration through environment
variables. Create a simple file like ``.ostackrc`` in the home directory and
source the file to make the variables available. On Open Telekom Cloud servers
this file exists on bootup and needs to be changed according to your credentials.

.. code-block:: bash

    # .ostackrc file
    export OS_USERNAME="<USER_NAME>"
    export OS_USER_DOMAIN_NAME=<OTC00000000001000000XYZ>
    export OS_PASSWORD=<PASSWORD> # optional
    export OS_TENANT_NAME=eu-de
    export OS_PROJECT_NAME=<eu-de_PROJECT_NAME>
    export OS_AUTH_URL=https://iam.eu-de.otc.t-systems.com:443/v3
    export NOVA_ENDPOINT_TYPE=publicURL
    export OS_ENDPOINT_TYPE=publicURL
    export CINDER_ENDPOINT_TYPE=publicURL
    export OS_VOLUME_API_VERSION=2
    export OS_IDENTITY_API_VERSION=3
    export OS_IMAGE_API_VERSION=2

Run the source command to make the ``environment variables`` available.

.. code-block:: bash

   $ source .ostackrc

The ``environment variables`` are now available for usage. For testing your
connection run the following command.

Test your connection
^^^^^^^^^^^^^^^^^^^^

If you followed the `installation advices <index>`_ for your specific
operating system, you can use the following command to test the basic
functionality.

.. code-block:: bash

    $ openstack flavor list

.. note::
   You don't need to specify the `--os-cloud` parameter when environment
   variables are used.

Cache Settings
--------------

Accessing a cloud is often expensive, so it's quite common to use
client-side caching of those operations. To facilitate that, `openstacksdk`
understands passing through cache settings to dogpile.cache, with the following
behaviors:

* Listing no config settings means you get a null cache.
* `cache.expiration_time` and nothing else gets you memory cache.
* Otherwise, `cache.class` and `cache.arguments` are passed in

Different cloud behaviors are also differently expensive to deal with. If you
want to get really crazy and tweak stuff, you can specify different expiration
times on a per-resource basis by passing values, in seconds to an expiration
mapping keyed on the singular name of the resource. A value of `-1` indicates
that the resource should never expire.

`openstacksdk` does not actually cache anything itself, but it collects
and presents the cache information so that your various applications that
are connecting to OpenStack can share a cache should you desire.

.. code-block:: yaml

  cache:
    class: dogpile.cache.pylibmc
    expiration_time: 3600
    arguments:
      url:
        - 127.0.0.1
    expiration:
      server: 5
      flavor: -1
  clouds:
    mtvexx:
      profile: otc
      auth:
        username: "<USER_NAME>"
        password: '<PASSWORD>'
        project_name: <eu-de_PROJECT_NAME>
      region_name: eu-de
      dns_api_version: 1

`openstacksdk` can also cache authorization state (token) in the keyring.
That allow the consequent connections to the same cloud to skip fetching new
token. When the token gets expired or gets invalid `openstacksdk` will
establish new connection.


.. code-block:: yaml

  cache:
    auth: true

MFA Support
-----------

MFA support requires a specially prepared configuration file. In this case a
combination of 2 different authorization plugins is used with their individual
requirements to the specified parameters.

.. code-block:: yaml

  clouds:
    mfa:
      auth_type: "v3multifactor"
      auth_methods:
        - v3password
        - v3totp
      auth:
        auth_url: "https://iam.eu-de.otc.t-systems.com/v3"
        username: "<USER_NAME>"
        password: '<PASSWORD>'
        project_name: <eu-de_PROJECT_NAME>
        user_domain_name: 'OTC00000000001000000xxx'