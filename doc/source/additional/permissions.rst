**Permission Description**

Permissions are user management and cloud service management permissions. User management involves creating, deleting, and modifying users and granting
permissions to users. Cloud service management involves creating, viewing, modifying, and deleting resources of cloud services. After granting user management
and cloud service management permissions to a user group, the users added to the user group can inherit permissions of the user group. User group-specific
permissions simplify permission management.

**Permission Relationship**

.. figure:: /_static/images/permissions.png

**Default Permissions**

The system provides two types of default permissions: user management and cloud service management.

.. table:: **Table 1** User management permissions

+-----------------------------------------+------------------------+-------------------------------------------------------------------------------------+
| **Node Name**                           | **Permission Name**    | **Description**                                                                     |
+=========================================+========================+=====================================================================================+
| Base                                    | Security Administrator | Users with this permission can:                                                     |
|                                         |                        | Create, delete, and modify users.                                                   |
|                                         |                        | Grant permissions to users.                                                         |
+-----------------------------------------+------------------------+-------------------------------------------------------------------------------------+
| IAM                                     | Agent Operator         | Users with this permission can switch to an entrusted user for processing services. |
+-----------------------------------------+------------------------+-------------------------------------------------------------------------------------+

.. note::

   Currently, policies only support fine-grained authorizationof ECS, EVS, and VPC. ECS Admin, ECS User, ECS Viewer, EVS Admin, EVS Viewer,VPC Admin, and VPC 
   Viewer are preset fine-grained authorization policies.

.. table:: **Table 2** User group for cloud service management

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Permission Name**                                | **Managed Cloud Resource**                         | **Description**                                    |
+====================================================+====================================================+====================================================+
| Agent Operator                                     | Identity and Access Management                     | Permissions for switching roles to access          |
|                                                    |                                                    | resources of delegating accounts.                  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| IAM ReadOnlyAccess                                 | Identity and Access Management                     | Read-only permissions for IAM.                     |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| CBR Administrator                                  | Cloud Backup and Recovery                          | Administrator permissions for CBR. Users granted   |
|                                                    |                                                    | these permissions can operate and use all vaults,  |
|                                                    |                                                    | backups, and policies.                             |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| CBR User                                           | Cloud Backup and Recovery                          | Common user permissions for CBR. Users granted     |
|                                                    |                                                    | these permissions can create, view, and delete     |
|                                                    |                                                    | vaults and backups, but cannot create, update, or  |
|                                                    |                                                    | delete policies.                                   |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| CBR Viewer                                         | Cloud Backup and Recovery                          | Read-only permissions for CBR. Users granted these |
|                                                    |                                                    | permissions can only view CBR data.                |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| CCE Admin                                          | Cloud Container Engine                             | Read and write permissions for CCE clusters,       |
|                                                    |                                                    | including creating, deleting, and updating a       |
|                                                    |                                                    | cluster.                                           |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| CCE Administrator                                  | Cloud Container Engine                             | All permissions related to CCE service resources.  |
|                                                    |                                                    | Users who use this permission must have **Tenant   |
|                                                    |                                                    | Guest, Server Administrator, OBS Tenant            |
|                                                    |                                                    | Administrator,** and **ELB Administrator**         |
|                                                    |                                                    | permissions.                                       |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| CCE Viewer                                         | Cloud Container Engine                             | Read-only permissions for CCE clusters.            |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| CES Administrator                                  | Cloud Eye                                          | Permissions to view monitoring metrics as well as  |
|                                                    |                                                    | add, modify, and delete alarm rules. Users granted |
|                                                    |                                                    | permissions of this policy must also be granted    |
|                                                    |                                                    | permissions of the Tenant Guest policy.            |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| CSBS Administrator                                 | Cloud Server Backup Service                        | Permissions to create, restore, and delete backups |
|                                                    |                                                    | of ECSs, and manage backup policies. The creation, |
|                                                    |                                                    | restoration, and management permissions depend on  |
|                                                    |                                                    | the Server Administrator permission.               |
|                                                    |                                                    | If the **Server Administrator** permission is      |
|                                                    |                                                    | unavailable, ECS information cannot be obtained    |
|                                                    |                                                    | when users create and restore backups.             |
|                                                    |                                                    | If the **Server Administrator** permission is      |
|                                                    |                                                    | unavailable, ECS information cannot be obtained    |
|                                                    |                                                    | when users associate ECSs with backup policies..   |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| CSS Administrator                                  | Cloud Search Service                               | Management permissions on all CSS resources.The    |
|                                                    |                                                    | permissions depend on the Tenant Guest and Server  |
|                                                    |                                                    | Administrator permissions. CSS cannot run properly |
|                                                    |                                                    | if either of the permissions is unavailable.       |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| CTS Administrator                                  | Cloud Trace Service                                | Full permissions for CTS. This policy depends on   |
|                                                    |                                                    | the Tenant Guest policy in the same project and    |
|                                                    |                                                    | the Tenant Administrator policy in the OBS         |
|                                                    |                                                    | project.                                           |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| DCS Administrator                                  | Distributed Cache Service                          | Permissions to: Create, start, stop, restart, and  |
|                                                    |                                                    | delete DCS instances. Change passwords of DCS      |
|                                                    |                                                    | instances. Configure DCS instance parameters.      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| DDS Administrator                                  | Document Database Service                          | Users who have this right, plus **Tenant Guest**   |
|                                                    |                                                    | and **Server Administrator** rights, can perform   |
|                                                    |                                                    | any operations on DDS, including creating,         |
|                                                    |                                                    | deleting, rebooting, or scaling up DB instances,   |
|                                                    |                                                    | configuring database parameters, and restoring DB  |
|                                                    |                                                    | instances.                                         |
|                                                    |                                                    | Users who have this right but not the **Tenant     |
|                                                    |                                                    | Guest** or **Server Administrator** right cannot   |
|                                                    |                                                    | use DDS.                                           |
|                                                    |                                                    | Users who have the **VPC Administrator** right     |
|                                                    |                                                    | can create VPCs or subnets.                        |
|                                                    |                                                    | Users who have the **CES Administrator** right     |
|                                                    |                                                    | can add or modify alarm rules for DB instances.    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| DIS Administrator                                  | Data Ingestion Service                             | Permissions to:                                    |
|                                                    |                                                    | Create, delete, query, and list DIS streams.       |
|                                                    |                                                    | Push data to DIS streams or pull data from them.   |
|                                                    |                                                    | Query stream monitoring metrics.                   |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| DMS Administrator                                  | Distributed Message Service                        | Administrator permissions for DMS. Users granted   |
|                                                    |                                                    | these permissions can perform all operations on    |
|                                                    |                                                    | DMS queues.                                        |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| DNS Administrator                                  | Domain Name Service                                | Permissions to create, query, and delete zones and |
|                                                    |                                                    | record sets.                                       |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| DWS Administrator                                  | Data Warehouse Service                             | Management permissions on all DWS resources.       |
|                                                    |                                                    | The permissions depend on the **Tenant Guest** and |
|                                                    |                                                    | **Server Administrator** permissions. DWS cannot   |
|                                                    |                                                    | run properly if either of the permissions is       |
|                                                    |                                                    | unavailable.                                       |
|                                                    |                                                    | If DWS users are to create a VPC or a subnet,      |
|                                                    |                                                    | the VPC Administrator permission is required.      |
|                                                    |                                                    | If DWS users are to view monitoring metrics of     |
|                                                    |                                                    | data warehouse clusters, the **CES Administrator** |
|                                                    |                                                    | permission is required.                            |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| DWS Database Access                                | Data Warehouse Service                             | DWS Database Access permission. Users with this    |
|                                                    |                                                    | permission can generate temporary database user    |
|                                                    |                                                    | credentials based on IAM users to connect to the   |
|                                                    |                                                    | DWS cluster database.                              |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| ECS Admin                                          | Elastic Cloud Server                               | All ECS operation permissions, including creating, |
|                                                    |                                                    | deleting, and viewing ECSs and modifying ECS       |
|                                                    |                                                    | specifications.                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| ECS User                                           | Elastic Cloud Server                               | General operation permissions on ECSs (such as     |
|                                                    |                                                    | viewing and restarting ECSs), but not advanced     |
|                                                    |                                                    | operation permissions (such as creating or         |
|                                                    |                                                    | deleting ECSs, or reinstalling/changing ECS OSs).  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| ECS Viewer                                         | Elastic Cloud Server                               | ECS read-only permissions, such as viewing ECSs.   |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| ELB Administrator                                  | Elastic Load Balancing                             | Permissions on all ELB resources. This permission  |
|                                                    |                                                    | depends on the VPC Administrator, Server           |
|                                                    |                                                    | Administrator, CES Administrator, and OBS          |
|                                                    |                                                    | Administrator permissions. Users who use the ELB   |
|                                                    |                                                    | Administrator permission cannot use some functions |
|                                                    |                                                    | provided by the ELB service if they do not have    |
|                                                    |                                                    | the preceding permissions.                         |
|                                                    |                                                    | If users who use this permission do not have the   |
|                                                    |                                                    | VPC Administrator and Server Administrator         |
|                                                    |                                                    | permissions, they cannot create or delete load     |
|                                                    |                                                    | balancers and backend servers.                     |
|                                                    |                                                    | If users who use this permission do not have the   |
|                                                    |                                                    | CES Administrator permission, monitoring data      |
|                                                    |                                                    | cannot be reported to Cloud Eye.                   |
|                                                    |                                                    | If users who use this permission do not have the   |
|                                                    |                                                    | OBS Administrator permission, data backups cannot  |
|                                                    |                                                    | be stored in OBS buckets.                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| EVS Admin                                          | Elastic Volume Service                             | All EVS operation permissions, including creating, |
|                                                    |                                                    | deleting, and viewing EVS disks and modifying EVS  |
|                                                    |                                                    | disk specifications.                               |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| EVS Viewer                                         | Elastic Volume Service                             | EVS read-only permission, such as viewing EVS      |
|                                                    |                                                    | disks and EVS disk details.                        |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| GaussDB FullAccess                                 | GaussDB(for MySQL)                                 | Full permissions for GaussDB                       |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| GaussDB ReadOnlyAccess                             | GaussDB(for MySQL)                                 | Read-only permissions for GaussDB                  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| IAM ReadOnlyAccess                                 | Identity and Access Management                     | Read-only permissions for IAM.                     |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| IMS Administrator                                  | Image Management Service                           | Permissions to create, modify, delete, and share   |
|                                                    |                                                    | images. The permissions depend on the **Server     |
|                                                    |                                                    | Administrator** and **OBS Tenant Administrator**   |
|                                                    |                                                    | permissions.                                       |
|                                                    |                                                    | To create an image using an ECS, users need to     |
|                                                    |                                                    | configure this permission as well as the **Server  |
|                                                    |                                                    | Administrator** permission.                        |
|                                                    |                                                    | To create an image using an image file, users      |
|                                                    |                                                    | need to configure this permission as well as the   |
|                                                    |                                                    | **OBS Tenant Guest** permission.                   |
|                                                    |                                                    | To export an image, users need to configure this   |
|                                                    |                                                    | permission as well as the **OBS Tenant             |
|                                                    |                                                    | Administrator** permission.                        |
|                                                    |                                                    | To query predefined tags when adding a tag to an   |
|                                                    |                                                    | image or searching for an image by tag, users need |
|                                                    |                                                    | to configure this permission as well as the **TMS  |
|                                                    |                                                    | Administrator** permission.                        |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| KMS Administrator                                  | Key Management Service                             | Permissions to:                                    |
|                                                    |                                                    | Create, enable, disable, schedule the deletion     |
|                                                    |                                                    | of, and cancel the scheduled deletion of CMKs.     |
|                                                    |                                                    | Query the list of CMKs and information about       |
|                                                    |                                                    | CMKs.                                              |
|                                                    |                                                    | Create random numbers.                             |
|                                                    |                                                    | Create DEKs.                                       |
|                                                    |                                                    | Create DEKs without plaintext.                     |
|                                                    |                                                    | Encrypt and decrypt DEKs.                          |
|                                                    |                                                    | Change the aliases and description of CMKs.        |
|                                                    |                                                    | Create, revoke, and query grants on CMKs.          |
|                                                    |                                                    | Import, delete CMK material.                       |
|                                                    |                                                    | Add, delete, and query CMK tags.                   |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| LTS Administrator                                  | Log Tank Service                                   | Permissions to create log groups, query log        |
|                                                    |                                                    | groups, delete log groups, create log topics,      |
|                                                    |                                                    | query log topics, and delete log topics.           |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| ModelArts CommonOperations                         | ModelArts                                          | Common user permissions for ModelArts. Users       |
|                                                    |                                                    | granted these permissions can operate and use      |
|                                                    |                                                    | ModelArts, but cannot manage dedicated resource    |
|                                                    |                                                    | pools.                                             |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| ModelArts FullAccess                               | ModelArts                                          | Administrator permissions for ModelArts. Users     |
|                                                    |                                                    | granted these permissions can operate and use      |
|                                                    |                                                    | ModelArts.                                         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| MRS Administrator                                  | MapReduce Service                                  | Permissions to view MRS overview information,      |
|                                                    |                                                    | operation logs, cluster information, job           |
|                                                    |                                                    | information, HDFS file operation information,      |
|                                                    |                                                    | alarm list, and MRS Manager portal.                |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| NAT Gateway Administrator                          | NAT Gateway                                        | Permissions to create, delete, modify, and query   |
|                                                    |                                                    | all resources of the NAT Gateway service. The      |
|                                                    |                                                    | permissions depend on the Tenant Guest permission. |
|                                                    |                                                    | If a NAT user needs resources, including VPCs,     |
|                                                    |                                                    | subnets, and EIPs, to create NAT gateways, the VPC |
|                                                    |                                                    | Administrator and Server Administrator permissions |
|                                                    |                                                    | are required.                                      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| OBS Buckets Viewer                                 | Object Storage Service                             | Operation permissions: listing buckets, obtaining  |
|                                                    |                                                    | basic bucket information, obtaining bucket         |
|                                                    |                                                    | metadata, and listing objects.                     |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| RDS Administrator                                  | Relational Database Service                        | Users who have this right, plus **Tenant Guest**   |
|                                                    |                                                    | and **Server Administrator** rights, can perform   |
|                                                    |                                                    | any operations on RDS and DDS, including creating, |
|                                                    |                                                    | deleting, rebooting, or scaling up DB instances,   |
|                                                    |                                                    | configuring database parameters, and restoring DB  |
|                                                    |                                                    | instances.                                         |
|                                                    |                                                    | Users who have this right but not the **Tenant     |
|                                                    |                                                    | Guest** or **Server Administrator** right cannot   |
|                                                    |                                                    | use RDS and DDS.                                   |
|                                                    |                                                    | **NOTE**                                           |
|                                                    |                                                    | Users who have the **VPC Administrator**\ right    |
|                                                    |                                                    | can create VPCs or subnets.                        |
|                                                    |                                                    | Users who have the **CES Administrator** right     |
|                                                    |                                                    | can add or modify alarm rules for DB instances.    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| RTS Administrator                                  | Resource Template Service                          | Operation permissions:                             |
|                                                    |                                                    | All operations on RTS. To orchestrate a resource,  |
|                                                    |                                                    | users with this permission must also have the      |
|                                                    |                                                    | **Administrator** permission. For example:         |
|                                                    |                                                    | Users with this permission and the **Server        |
|                                                    |                                                    | Administrator** permission can create stacks for   |
|                                                    |                                                    | ECS, VPC, EVS, and IMS resources.                  |
|                                                    |                                                    | Users with this permission and the **ELB           |
|                                                    |                                                    | Administrator** permission can create an ELB       |
|                                                    |                                                    | resource stack.                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| SDRS Administrator                                 | Storage Disaster Recovery Service                  | Users with this permission can create, modify,     |
|                                                    |                                                    | delete, and query SDRS resources.                  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Security Administrator                             | Base                                               | Full permissions for IAM.                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Server Administrator                               | Base                                               | For the EVS service, users with this permission    |
|                                                    |                                                    | can create, modify, and delete EVS disks.          |
|                                                    |                                                    | For the ECS service, users with this permission    |
|                                                    |                                                    | can create, modify, and delete ECSs.This role must |
|                                                    |                                                    | be used together with the Tenant Guest role in the |
|                                                    |                                                    | same project.                                      |
|                                                    |                                                    | For the VPC service, users with this permission    |
|                                                    |                                                    | and the Tenant Guest permission can perform all    |
|                                                    |                                                    | operations on security groups, security group      |
|                                                    |                                                    | rules, ports, firewalls, elastic IP addresses      |
|                                                    |                                                    | (EIPs), and bandwidth.                             |
|                                                    |                                                    | For the IMS service, users with this permission    |
|                                                    |                                                    | can create, delete, query, and modify images.This  |
|                                                    |                                                    | role must be used together with the IMS            |
|                                                    |                                                    | Administrator role in the same project.            |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| SFS Administrator                                  | Scalable File Service                              | Users with both this permission and the **Tenant   |
|                                                    |                                                    | Guest** permission can create, delete, query,      |
|                                                    |                                                    | expand, and downsize the file system.              |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| SFS Turbo Administrator                            | Scalable File Service                              | Users with both this permission and the Tenant     |
|                                                    |                                                    | Guest permission can create, delete, query, and    |
|                                                    |                                                    | expand the SFS Turbo file system.                  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| SFS Turbo Viewer                                   | Scalable File Service                              | Read-only permissions. Users granted these         |
|                                                    |                                                    | permissions can only view file system data.        |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| SMN Administrator                                  | Simple Message Notification                        | Permissions to:                                    |
|                                                    |                                                    | Create, modify, delete, and view topics.           |
|                                                    |                                                    | Create, delete, and view subscriptions.            |
|                                                    |                                                    | Create, modify, delete, and view message           |
|                                                    |                                                    | templates.                                         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| SWR Administrator                                  | Software Repository for Container                  | All SWR operation permissions, including pushing   |
|                                                    |                                                    | and pulling images, and granting permissions.      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Tenant Administrator                               | Base                                               | Administrator permissions for all services except  |
|                                                    |                                                    | IAM.                                               |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Tenant Guest                                       | Base                                               | Read-only permissions for all services except IAM. |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| TMS Administrator                                  | Tag Management Service                             | Users with this permission can create, modify, and |
|                                                    |                                                    | delete predefined tags.                            |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| VBS Administrator                                  | Volume Backup Service                              | Permissions to create backups, delete backups, and |
|                                                    |                                                    | restore data using backups. This permission        |
|                                                    |                                                    | depends on the **ServerAdministrator** and         |
|                                                    |                                                    | **Tenant Guest** permissions. The VBS              |
|                                                    |                                                    | administrator must have permissions to manage EVS  |
|                                                    |                                                    | disks and read images.                             |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| VPC Admin                                          | Virtual Private Cloud                              | All VPC operation permissions, including creating, |
|                                                    |                                                    | querying, modifying, and deleting VPCs, subnets,   |
|                                                    |                                                    | and security groups.                               |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| VPC Administrator                                  | Virtual Private Cloud                              | All operation permissions on VPCs, subnets, ports, |
|                                                    |                                                    | VPNs, and Direct Connect resources. A user with    |
|                                                    |                                                    | the VPC Administrator permission must have the     |
|                                                    |                                                    | Tenant Guest permission.                           |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| VPC Viewer                                         | Virtual Private Cloud                              | VPC real-only permission, such as querying VPCs.   |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| VPCEndpoint Administrator                          | VPC Endpoint                                       | Full permissions for VPCEP. This role must be used |
|                                                    |                                                    | together with the **Server Administrator**, **VPC  |
|                                                    |                                                    | Administrator**, and **DNS Administrator** roles   |
|                                                    |                                                    | in the same project.                               |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| WAF Administrator                                  | Web Application Firewall                           | Permissions to:                                    |
|                                                    |                                                    | Create and delete WAF instances.                   |
|                                                    |                                                    | Configure, enable, disable WAF instances.          |
|                                                    |                                                    | Modify the protection policies of WAF instances.   |
|                                                    |                                                    | Configure alarm notification for WAF instances.    |
|                                                    |                                                    | Query the WAF instance list and details.           |
|                                                    |                                                    | Authenticate the domain name of a WAF instance.    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Anti-DDoS Administrator                            | Anti-DDoS                                          | Permissions to enable, disable, and modify         |
|                                                    |                                                    | configurations. This permission depends on the     |
|                                                    |                                                    | **Tenant Guest** permission and must have          |
|                                                    |                                                    | permission to query EIPs in VPCs.                  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| DRS Administrator                                  | Data Replication Service                           | Basic permission, which must be added when DRS is  |
|                                                    |                                                    | used.Dependent on the Tenant Guest, Server         |
|                                                    |                                                    | Administrator, and RDS Administrator policies.     |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

