Glossary
========


.. glossary::

   Accelerated Engine Image
     Accelerated Engine Image (AEI) is a dynamic PR loading file of the FPGA chip.

   access control list
     An access control list (ACL) is a group of IP addresses or network segments. Users can only access the public cloud system from the IP addresses or network
     segments contained in the ACL.

   access frequency control
     Frequency of access to an interface is limited by an access control policy.

   access key
     An access key consists of an Access Key ID (AK) and a Secret Access Key (SK). Access keys (AK/SK) are used to verify the identity of a sender who initiates a
     request through APIs. Access keys and passwords have similar functions. Access keys can be generated and managed on the My Credential page.

   Accurate Access Protection
     Detection policies can be customized for common fields (such as URL, IP, Params, Cookie, Referer, User-Agent and Header) in HTTP requests. In addition,
     multi-logic detection policies are supported.

   ACK flood
     See :term:`ACK flood attack`.

   ACK flood attack
     In an ACK flood attack, the attacker sends a large number of ACK packets to the target server through a botnet. As a result, the packets cause link
     congestion with an excessive load, or requests with changing source addresses or destination ports sent at extremely high rates cause an abnormality in the
     forwarding device and then lead to network breakdown, or processing capability of the target server is exhausted and the server fails to provide services
     normally.

   Address record
     Address records (A records) are used to specify IP addresses for host names (or domain names). You can use A records to make different domain names point to
     different IP addresses.

   Advanced Encryption Standard
     The AES algorithm is a symmetric grouped password algorithm and one of the most popular symmetric key encription algorithm released by the U.S. National
     Institute of Standards and Technology (NIST) on November 26, 2001.

   advanced package
     Logical and functional stored procedures and functions provided by the database.

   AI Engine
     An AI engine is a framework that allows you to develop machine learning and deep learning model training jobs, such as TensorFlow and MXNet.

   Alarm
     An alarm is triggered based on an alarm rule. The alarm rule defines the actions that the system takes if a parameter value hits the specified threshold.

   AM
     See :term:`ApplicationMaster`

   anti-crawler
     WAF has a big crawler characteristics database used to detect crawlers (such as engine crawlers, script crawlers, and scanners).

   application programming interface
     An application programming interface is a particular set of rules and specifications that are used for communication between software programs.

   ApplicationMaster
     Manages the life cycle of applications.

   AS configuration
     A template listing specifications for the instances to be added to an AS group.

   AS policy
     A condition for triggering a scaling action.

   asynchronous replication
     An application initiates a data update (including insert, delete, and modify operations) request. After completing the update operation, the Master sends a
     response to the application immediately, and then replicates the data to the Slave. During the asynchronous replication, the Master does not need to wait for
     a response from the Slave. Therefore, the DB instance replicated in an asynchronous way often has a higher performance. However, since the data is not
     synchronized to the Slave in real time, if the Master fails when a latency occurs on the Slave, data may be inconsistent between the Master and Slave.

   Attaching a replication pair to a protected instance
     Indicates to attach the two disks in a replication pair to the two servers in a protected instance.

   authoritative DNS server
     An authoritative DNS server is authorized by an upper-level DNS server. It is the authoritative information source for a particular domain name.

   automated backup
     A full backup automatically created for a DB instance by RDS. Users can set the automated backup start time and backup retention period.

   availability priority
     During a primary/standby switchover, the switchover is performed even if data is inconsistent between the primary and standby DB instances and the
     synchronization delay is no more than 5 minutes, thereby ensuring service availability. If the delay is longer than five minutes, the system does not perform
     the primary/standby switchover and stop database services to prevent data loss.

   availability zone
     A physical region where resources use independent power supply and networks. AZs are physically isolated but interconnected through the internal network. To
     enhance application availability, you are advised to create instances in different AZs.

   backup
     backup consistency There are three types of backup consistency:
     Inconsistent backup: backs up files and disks in different points in time.
     Crash-consistent backup: captures data existing on disks upon backup and backs up files and disks at the same point in time, without backing up memory data
     and quiescing application systems. In such a manner, backup consistency of application systems is ensured. Though the application consistency is not
     ensured, disks, such as chkdsk, will be checked upon operating system re-startup to restore damaged data and log rollback will be performed on databases to
     keep data consistent.
     Application-consistent backup: backs up files and disks at the same point in time, including memory data, to ensure application system consistency.

   backup policy
     A policy used to automatically back up data by specifying the backup time, backup period, retention rules, and other items. After a backup target is
     associated with a backup policy, the system will automatically back up data and delete expired backups according to the policy.

   backup retention period
     retention period for automated backups. After the retention period expires, automated backups will be deleted automatically.

   backup storage
     The underlying storage resources used for storing backup data and logs of a database persistently.

   Bandwidth
     The bandwidth represents network usage, facilitating service charging.

   Bare Metal Server
     Bare Metal Server (BMS) features both the scalability of VMs and high performance of physical servers. It provides dedicated servers on the cloud that offer
     the computing performance and data security required by core databases, key application systems, high-performance computing (HPC), and Big Data.

   Bidirectional Forwarding Detection
     A fast and independent hello protocol that delivers millisecond-level link failure detection and provides carrier-class availability. After sessions are
     established between neighboring systems, the systems can periodically send BFD packets to each other. If one system fails to receive a BFD packet within the
     negotiated period, the system regards that the bidirectional link fails and instructs the upper layer protocol to take actions to recover the faulty link.

   black hole
     A black hole is a status where a server detects zero access traffic from the Internet because Internet access to the server has been blocked.

   Blacklist and Whitelist
     The IP address whitelist is a list of trusted IP addresses and traffic from these IP addresses is not subject to attack detection. The IP address blacklist
     is a list of malicious IP addresses and traffic from these IP addresses is subject to actions specified in detection policies.

   Block
     The smallest logical unit of storage in HDFS. Each HDFS file is stored as one or more blocks. All the blocks are stored on Data Nodes.

   Border Gateway Protocol
     A routing protocol for autonomous systems (ASs) that runs on top of TCP. BGP is the only protocol that can run a network as large as the Internet and process
     the many connections between unrelated routing domains. BGP is built on EGP. The main function of a BGP system is to exchange information about network
     reachability, such as AS information, with other BGP systems. This information effectively creates an AS interconnection topology and eliminates routing
     loops. In addition, policy decisions can be made at the AS level.

   Bring Your Own License
     If you have an OS or a software license (a license whose certified items include number of physical sockets and physical cores), you can migrate your
     services to the cloud platform using the BYOL feature. Then, you can continue to use your existing licenses without additional charges.

   bucket
     A container used to store objects. A bucket name must be unique.

   bucket policy
     A group of control policies that accept or reject requests to access buckets, and control the permissions of one or more users to access buckets and objects
     in buckets.

   Business Warehouse on HANA
     An SAP HANA application scenario where SAP HANA provides data analysis.

   CC attack
     See :term:`challenge collapsar attack`

   CCE
     See :term:`Cloud Container Engine`

   Cell
     A row and column tuple exactly specifies a cell in HBase. Cell content is uninterrpreted bytes.

   challenge collapsar attack
     A Challenge Collapsar (CC) attack is targeted at web servers or application programs by means of standard GET or POST requests used for obtaining
     information. If the requests involve Universal Resource Identifiers (URIs) of database operations or URIs consuming other system resources, server resources
     are exhausted and the target servers will be unable to respond normally.

   checkpoint
     A mechanism that stores data from the database memory to disks at a certain time. The database periodically stores the data of committed transactions and
     data of uncommitted transactions to disks. The data and redo logs can be used for database restoration if a database restarts or breaks down.

   Cloud Backup and Recovery
     Cloud Backup and Recovery allows users to back up cloud servers and disks. If there is a virus intrusion, accidental deletion, or software or hardware fault,
     data can be restored to any backup point.

   Cloud Container Engine
     Cloud Container Engine (CCE) is a scalable, high-performance container service. It is built on Docker technology and scales your applications within seconds.
     CCE also provides fast application shipping and deployment, automatic O&M, and other Docker container lifecycle management features.

   Cloud Eye
     Cloud Eye is a multi-dimensional resource monitoring platform. You can use Cloud Eye to monitor the utilization of service resources, track the running
     status of cloud services, configure alarm rules and notifications, and quickly respond to resource changes.

   Cloud Search Service
     Cloud Search Service is a fully managed, distributed search service. It is fully compatible with open-source Elasticsearch and provides users with structured
     and unstructured data search, statistics, and report capabilities.

   cloud service provider
     A company or an organization that provides cloud computing services.

   cluster (CSS)
     Cloud Search Service provides functions on a per cluster basis. A cluster represents an independent search service that consists of multiple instances.

   cluster (DWS)
     The smallest management unit in DWS. A cluster represents a separately running data warehouse. Users can manage the lifecycle of a cluster in DWS.

   code injection
     Code injection is an attack that exploits logic defects of web applications in input validation or code execution vulnerabilities of some script functions.

   cold backup
     A cold backup is performed when a system is stopped or being maintained. The backup data is completely the same as the data in the system at the point in
     time.

   column
     An equivalent concept of field. A database table consists of one or more columns.

   Column Family
     Column family is a predefined arbitrary set of columns and stored in HBase Schema. To create some column in family you should create family first. A column
     family regroups data of a same nature in HBase and has no constraint on the type. For each Row data in one Column family is physically stored at one server.
     Each Column family has is attributes like: Compression, Timestamps, Block Cache and etc.

   Column(MRS)
     Column is one of HBase Table dimensions. A column name has the form "family:label" where family and label can be arbitrary byte arrays. A table enforces its
     set of familys (called "column families").

   command injection
     Exploiting web application interfaces allowed to invoke system commands, attackers use commands generated at the server end by command splicing and blacklist
     bypassing to attack services.

   Command Line Interface
     A means of communication between a program and its user, based solely on textual input and output.

   Compression Unit
     Compression Unit (CU) is the smallest storage unit in a column-storage table.

   concurrency control
     A DBMS service that ensures data integrity when multiple transactions are concurrently executed in a multi-user environment. In a multi-threaded DWS
     environment, concurrency control ensures that database operations are safe and all database transactions remain consistent at any given time.

   config
     config is a special mongod that stores metadata of a DB instance. config is deployed as a replica set. To create a DB instance or modify metadata of a DB
     instance, config must be available.

   Container(MRS)
     Isolates CPU and memory resources on Java virtual machines (VMs).

   Core Node
     A core node in a MapReduce Service cluster processes data and stores process data in the HDFS.

   cross-origin resource sharing
     Cross-origin resource sharing (CORS) is a mechanism that allows many resources (such as, fonts and JavaScript) on a web page to be requested from another
     domain outside the domain from which the resource originated.

   cross-site request forgery
     Cross-site request forgery is another common web attack. Attackers forge data for targets to access. If the browsers of the targets maintain the
     authentication sessions with the destination sites, the targets unknowingly send requests forged by attackers to the destination sites when accessing the
     attacker-forged pages or URLs.

   cross-site scripting
     XSS is a type of web security vulnerability used by attackers to steal user information. Using the vulnerability, attackers inject malicious code into web
     pages. The code is executed to steal user information when users browse the web pages.

   CSBS
     Cloud Server Backup Service (CSBS) enables backup of entire Elastic Cloud Servers (ECSs), including VM specifications, system disks, and data disks. When an
     ECS becomes faulty, data can be restored from consistency backups of multiple Elastic Volume Service (EVS) disks to ensure maximum data security and
     accuracy.

   CSP
     See :term:`cloud service provider`

   CSS
     See :term:`Cloud Search Service`

   CU
     See :term:`Compression Unit`

   Customer Master Key
     A CMK is a key created with KMS and used to encrypt and protect DEKs.

   data control language
     A subset of SQL for setting or modifying database user or role rights.

   data definition language
     A subset of SQL for defining data structures and database objects.

   Data Definition Language(MRS)
     A language used to define the data structure and database objects in the HiveQL set. It consists of three types of syntax: CREATE, ALTER, and DROP. Derived
     from the Conference on Data Systems Languages (Codasyl) model, the DDL has become a subset of SQL.

   data dictionary
     A reserved table within a database which is used to store information about the database itself. The information includes database design information, stored
     procedure information, user rights, user statistics, database process information, database increase statistics, and database performance statistics.

   Data disk image
     A data disk image contains service data. It can be used to create EVS disks during ECS creation, or be used to create EVS disks that are attached to ECSs.
     Through data disk images, you can migrate your service data to the cloud.

   Data Encryption Key
     A DEK is used to encrypt users' data.

   Data Ingestion Service
     Data Ingestion Service (DIS) addresses the challenge of transmitting data within the cloud and from outside the cloud to inside the cloud. With DIS, you can
     build

   data manipulation language
     A subset of SQL for accessing data for database objects.

   Data Manipulation Language(MRS)
     An instruction set for accessing objects in databases. The core instructions in this set are INSERT, UPDATE, and DELETE, which respectively mean inserting,
     updating, and deleting. These instructions are indispensable for developing data-centered applications.

   data partitioning
     The action of dividing a table into parts (partitions) whose data does not overlap within a database instance. Tables can be partitioned by range, where the
     target storage location is mapped based on the range of the values in the column that is specified in the tuple.

   Data Plane Development Kit
     It is a collection of development platforms and interfaces for quickly processing data packets, and runs on Intel x86 platforms.

   data record
     A data record is the unit of data stored in a DIS stream. A data record is composed of a sequence number, partition key, and data blob. Data blobs are key
     data added by data producers to DIS streams. The payload of a data blob can be up to 1 MB before Base64 encoding.

   data replication
     In the primary/standby HA architecture, data will be replicated to a standby DB instance from a primary after data is committed to the primary DB instance.
     Data replications come in three types: forced synchronous replication, semi-synchronous replication, and asynchronous replication.

   Data Replication Service
     A stable, efficient, and easy-to-use cloud service for database online migration and synchronization. It simplifies data transmission processes and reduces
     transmission costs.

   Data Warehouse
     An integration center that stores a large amount of data. DWH is a core component of business intelligence (BI), which allows carriers to perform intelligent
     business analysis on users based on the massive user data stored in the data warehouse.

   Data Warehouse Service
     Data Warehouse Service is an online data processing database based on the public cloud infrastructure and platform and helps you mine and analyze massive
     sets of data.

   database
     A collection of data that is stored together and can be accessed, managed, and updated. Data in a view in the database can be classified into the following
     types: numerals, full text, digits, and images.

   database administrator
     A person who is responsible for managing databases. A DBA uses dedicated software to store and organize data. Their responsibilities include but are not
     limited to capacity planning, installation, configuration, database design, migration, performance monitoring, security, troubleshooting, and data backup and
     restoration.

   database instance
     A process and the database files that it controls. The cluster installs multiple database instances on one physical node. The GTM, CM, CN, and DN installed
     on cluster nodes are all database instances. A database instance is also called a logical node.

   database master password
     A string that defines the password for the database master user. The database master password is a string of 8 to 32 characters. It must contain uppercase
     letters, lowercase letters, digits, and special characters. You can use the following special characters: ~!@#%^*-_=+?

   database master user account
     A database master user account is different from the user cloud account and used only within the RDS instance environment to control access to users' DB
     instances. The database master user account is a native database user account used to connect to DB instances. For example, when creating a MySQL DB
     instance, root is the master user account by default and users can set the root password. After a DB instance is created, users can connect to the database
     using the database master user account. Subsequently, users can also create additional database user accounts to meet service requirements.

   database migration
     As services develop, a database needs to be migrated from an environment to another, for example, from a local data center to a cloud, or from a cloud to
     another cloud.

   database storage
     The underlying storage resources used for storing data and logs of a database permanently.

   database type
     Database types are classified into relational databases and non-relational databases.

   database user
     A user that accesses DDS. Currently, the default username is rwuser.

   DataNode
     One per node in the cluster, which manage storage attached to the nodes that they run on.

   Dataset
     A dataset is sample data stored in an OBS bucket and used for training models.ModelArts can manage the versions of datasets and switch different versions in
     different scenarios.

   DB engine
     A DB engine is a core service for storing, processing, and protecting data. It can be used to control access permissions and process transactions rapidly to
     meet enterprise requirements. Every DB instance supports DB engines.

   DB instance
     A DB instance is an isolated database environment in the cloud. It is a basic building block of RDS. A DB instance can contain multiple databases created by
     users and can be accessed using the same client tool and application as those used for accessing an isolated DB instance.

   DB instance class
     The DB instance class determines the computing and memory capacity of a DB instance. A user can change the CPU or memory of an available DB instance by
     changing its DB instance class.

   DB instance ID
     Each DB instance has a DB instance ID. This ID uniquely identifies a DB instance when a user uses the RDS console or RDS APIs. The DB instance ID must be
     unique for a user in a region.

   DB instance lifecycle
     A DB instance lifecycle starts from the time when the DB instance is created to the time when the DB instance is deleted. During a DB instance lifecycle,
     users can back up, restore, change instance classes, scale up storage space, reboot, or delete the instance.

   DB parameter group
     A database parameter group functions as a container for engine configuration values that can be applied to one or more DB instances. If users create a DB
     instance without specifying a DB parameter group, the default parameter group is used. The default parameter group contains the default values of the engine
     and database system optimized for the running DB instances. If users want their DB instances to run with their self-defined engine configuration values, they
     can simply create a new database parameter group, modify certain parameters, and associate the new DB parameter group to a DB instance. Once associated, all
     DB instances that use this particular DB parameter group get all the parameter updates to that DB parameter group.

   DBA
     See :term:`database administrator`

   DCL
     See :term:`data control language`

   DDL
     See :term:`data definition language`

   DDL(MRS)
     See :term:`Data Definition Language(MRS)`

   DDoS attack
     See :term:`distributed denial of service attack`

   DDS
     See :term:`Document Database Service`

   Dedicated Host
     Dedicated Host (DeH) is a service that provides dedicated physical hosts.You can create ECSs on a DeH to enhance isolation, security, and performance of your
     ECSs.

   Degraded
     The cluster goes into the state when some nodes in the cluster are faulty and cannot work properly, but the whole cluster runs properly.

   Detaching a replication pair from a protected instance
     Indicates to detach the two disks in a replication pair from the two servers in a protected instance.

   detection based on semantic analysis
     A syntax tree is built based on the semantic context to determine whether a load is an attack load.

   Development
     A HANA development scenario where development engineers configure and verify the compatibility between application software and SAP HANA and continuously
     optimize the application software.

   Direct Connect
     Direct Connect is a service that allows you to establish a dedicated network connection from your data center to the public cloud platform. You can establish
     network circuits between the cloud and your data center, office, or collocation environment. Direct Connect sets up private connections between the Direct
     Connect gateway and Virtual Private Clouds (VPCs) in the public cloud.

   DIS
     See :term:`Data Ingestion Service`

   Disabling protection
     Can be performed after the data synchronization is complete. Once the protection is disabled, the data synchronization stops, and the protection status of
     the protection group changes to Stopped.

   Disaster Recovery
     The recovery of data, access to data and associated processing through a comprehensive process of setting up a redundant site (equipment and work space) with
     recovery of operational data to continue business operations after a loss of use of all or part of a data center. This involves not only an essential set of
     data but also an essential set of all the hardware and software to continue processing of that data and business. Any disaster recovery may involve some
     amount of down time.

   distributed denial of service attack
     A denial-of-service (DoS) attack (a flood attack) is an attempt to use up the network or system resources of a computer to temporarily interrupt or stop
     services on the computer, thereby causing users unable to access the services normally. A DDoS attack is one in which two or more compromised computers are
     used to attack a single target, thereby causing denial of service for users of the targeted computer.

   DKIM
     DomainKeys Identified Mail (DKIM) is an email authentication method designed to detect email spoofing. It allows the receiver to check that an email claimed
     to have come from a specific domain was indeed authorized by the owner of that domain. It is intended to prevent forged sender addresses in emails, a
     technique often used in phishing and email spam. In technical terms, DKIM lets a domain associate its name with an email message by affixing a digital
     signature to it.

   DML
     See :term:`data manipulation language`

   DML(MRS)
     See :term:`Data Manipulation Language(MRS)`

   DN
     See :term:`DataNode`

   document
     An entity for Elasticsearch storage. Equivalent to the row in the RDB, the document is the basic unit that can be indexed.

   Document Database Service
     DDS is a database service compatible with the MongoDB protocol and is secure, highly available, reliable, scalable, and easy to use. It provides DB instance
     creation, scaling, redundancy, backup, restoration, monitoring, and alarm reporting functions with just a few clicks on the DDS console.

   document type
     Similar to the table in the RDB, the document type is used to distinguish between different data. One index can contain multiple document types. A document
     actually must be indexed to a document type inside an index.

   Domain Name Service
     Domain Name Service (DNS) provides highly available and scalable authoritative DNS resolution services and domain name management services. It translates
     domain names or application resources into IP addresses required for network connection. By doing so, visitors' access requests are directed to the desired
     resources.

   DR direction
     Indicates the data replication direction. The data replication is from the source AZ to the target AZ when users create a protection group. After users
     perform a planned failover, the data replication is from the target AZ to the source AZ.

   DR drill
     Is to verify that a target server can take over services from a source server once a failover is performed.

   DRS
     See :term:`Data Replication Service`

   DWS
     See :term:`Data Warehouse Service`

   Elastic Cloud Server
     An Elastic Cloud Server (ECS) is a computing server consisting of CPUs, memory, images, and Elastic Volume Service (EVS) disks that allow on-demand
     allocation and elastic scaling. ECSs integrate Virtual Private Cloud (VPC), virtual firewalls, and multi-data-copy capabilities to create an efficient,
     reliable, and secure computing environment. This ensures stable and uninterrupted operation of services.

   Elastic IP
     An elastic IP address (EIP) can be bound to any ECSs in your account rather than a specified ECS. Different from a static IP address, when an ECS or its AZ
     is unavailable, its EIP can quickly redirect to the Internet IP address of any ECS in your account.

   Elastic Load Balance
     Elastic Load Balance (ELB) is a service that automatically distributes incoming traffic across multiple Elastic Cloud Servers (ECSs) to balance their service
     load. It enables you to increase service capabilities and fault tolerance of your applications.

   Elastic Volume Service
     The Elastic Volume Service (EVS) offers scalable block storage for servers. With high reliability, high performance, and rich specifications, EVS disks can
     be used for distributed file systems, development and test environments, data warehouse applications, and high-performance computing (HPC) scenarios to meet
     diverse service requirements. EVS disks are sometimes just referred to as disks.

   Elasticsearch
     Elasticsearch is an open-source system that provides both the search engine and NoSQL database functions. It is built based on Lucene and can be used for
     full-text search, structured search, and near real-time analysis.

   Enabling protection
     Can be performed after a protection group is created, data synchronization stops, or a failover is performed. Once the protection is enabled, the data
     synchronization starts, and the synchronization progress is displayed on the web page. This action affects all the protected instances in the protection
     group.

   Enterprise Resource Planning
     A company-wide computer software system that is used to manage and coordinate all the resources, information, and functions of a business from shared data
     stores.

   Envelope Encryption
     Envelope encryption is an encryption method that enables data encryption keys to be stored, transmitted, and used in "envelopes", unlike the CMK method that
     directly encrypts and decrypts data.

   ETL
     See :term:`Extract-Transform-Load`

   Executor
     A process launched for an application on a worker node, that runs tasks and keeps data in memory or disk storage across them. Each application has its own
     executors.

   Exeml
     Auto Learning is the process of automating model design, parameter tuning and training, and model compression and deployment with the labeled data. The
     process is free of coding and does not require developers' experience in model development.

   Extract-Transform-Load
     A process of data transmission from the source to the target database.

   Failback
     The system forcibly sets services in the target AZ to the unavailable state and sets services in the source AZ ready-to-start. This action affects all the
     protected instances in the protection group. After the failback, you need to start the servers in the source AZ. In addition, data synchronization of the
     protection group stops after the failback. You need to enable protection to restore data synchronization.

   failover
     If an unexpected interruption occurs on a primary DB instance, RDS automatically switches to the standby DB instance to restore database operations quickly
     without intervention. The time required for completing a failover depends on the database activity and other conditions at the time the primary DB instance
     became unavailable. The failover time ranges from seconds to minutes. However, large transactions or lengthy recovery processes may increase the failover
     time.

   federated identity authentication
     Federated identity authentication allows users on different systems to access multiple systems through a single sign-on (SSO).

   federated user
     Users who access the public cloud system using federated identity authentication.

   field
     Minimum unit of a document. The field is similar to the column in the database.

   Field-Programmable Gate Array
     A gate-level programmable component that implements complex combination or timing logic by using Verilog- or VHDL-based circuit design, synthesis, and
     placing and routing.

   File System
     A file system provides users with shared file storage service through NFS. It can be used to access network files remotely. After users create shared
     directories in the management console, the file system can be mounted to multiple ECSs and is accessible through the standard POSIX interface.

   Firewall
     A firewall consists of one or more access control lists (ACLs). Based on inbound and outbound rules, the firewall determines whether data packets are allowed
     in or out of any associated subnet.

   FPGA Accelerated Cloud Server
     An elastic cloud server that is accelerated by field programmable gate arrays (FPGAs). It provides a tool and environment for developing and using FPGA. With
     it, you can easily develop FPGA accelerators and deploy FPGA-based services, and provide easy-to-use, cost-effective, agile, and secure FPGA cloud services.

   FS
     See :term:`File System`

   full backup
     A backup method used to back up all data space of Elastic Volume Service (EVS) disks used by a specific user.

   full data migration
     All data is migrated from a source database to a target during the database running process. If any changes occur on the source database during or after the
     migration, such as new data inserted to the source database, the changes will not be synchronized to the target database.

   Full-ECS image
     A full-ECS image is an image created from an entire Elastic Cloud Server (ECS), including its system disk and data disks, or an image created from a Cloud
     Server Backup Service (CSBS) backup. A full-ECS image contains the OS of the ECS, applications installed on the ECS, and all the data in the ECS disks.

   Gap data archiving
     For MySQL or PostgreSQL HA DB instances, when the switchover policy priority is availability first, the primary DB instance may have more data than the
     standby instance due to synchronization delay or other reasons before a switchover. After a switchover occurs, the primary DB instance is demoted to be
     standby and the standby DB instance is promoted to be primary. The data that has not be synchronized to the new primary DB instance (original standby) will
     be packaged and uploaded to OBS in SQL statements for users to download them.

   GaussDB NoSQL
     GaussDB NoSQL is a distributed, non-relational, multi-model NoSQL database service with decoupled compute and storage architecture. This high availability
     database is secure and scalable, can be deployed, backed up, or restored quickly, and includes monitoring and alarm management.

   GaussDB(for MySQL)
     GaussDB(for MySQL) is a next generation MySQL-compatible, enterprise-class distributed database service. It uses a decoupled compute and storage architecture
     and provides up to 128 TB of storage capacity. There is no need to deal with sharding and there is virtually no risk of data loss. It combines the high
     availability and performance of commercial databases with the cost-effectiveness of open source databases.

   GBK
     GBK is an extension of the GB2312-80 character set and uses the double-byte encoding scheme. Its encoding ranges from 8140 to FEFE (excluding xx7F) and
     contains 23940 bits in total (including 210,003 Chinese characters). GBK is fully compatible with the GB2312-80 standard, supports all Chinese, Japanese, and
     Korean characters in the international standard ISO/IEC10646-1 and Chinese standard GB13000-1, and contains all Chinese characters in the BIG5 code.

   GDS
     See :term:`General Data Service`

   General Data Service
     General Data Service (GDS) is a parallel data loading tool. When importing data to DWS, users need to deploy the tool on the server where the source data is
     stored so that DataNodes can use this tool to obtain data.

   Graphical user interface
     A visual computer environment that represents elements with graphical images.

   HA
     See :term:`high availability`

   Hadoop Distributed File System
     HDFS provides high-throughput data access and is applicable to the processing of large data sets. MRS cluster data is stored in HDFS.

   Hardware Development Kit
     It is an FP1-based hardware development suite.

   Hardware Security Module
     An HSM is a hardware device that produces, stores, manages, and uses keys in a secure manner. An HSM also provides encryption processing services.

   HBase
     HBase is a column-oriented distributed cloud storage system that features enhanced reliability, excellent performance, and elastic scalability. It applies to
     the storage of massive data and distributed computing. Users can use HBase to build a storage system capable of storing TB- or even PB-level data. With
     HBase, users can filter and analyze data with ease and get responses in milliseconds, rapidly mining data value.

   HDFS
     See :term:`Hadoop Distributed File System`

   Heat
     Heat is the main project in the OpenStack Orchestration program. It implements an orchestration engine to launch multiple composite cloud applications based
     on templates in the form of text files that can be treated like code.

   Heat Orchestration Template
     Heat Orchestration Template (HOT) is a template format supported by the heat, along with the other template format, i.e. the Heat CloudFormation-compatible
     format (CFN).

   HFile
     File format for HBase. A file of sorted key/value pairs. Both keys and values are byte arrays.

   high availability
     A system availability that keeps a service running properly without interruption.

   High Availability Extension
     A software package from SUSE for automatic active-standby failover control.

   High-Performance Analytic Appliance
     A high-performance real-time data computing platform based on in-memory computing technologies.

   High-Speed Network
     A high-speed network is an internal network among BMSs and provides high bandwidth for connecting BMSs in the same AZ. If you want to deploy services
     requiring high throughput and low latency, you can create high-speed networks. Currently, the BMS service supports high-speed networks with a maximum
     bandwidth of 10 Gbit/s.

   Hive
     A data warehouse tool running on Hadoop. Hive maps structured data files to a database table and provides simple SQL search function that converts SQL
     statements into MapReduce tasks.

   Hive Query Language
     Hive Query Language, a standard data query language used for Hive data warehouses.

   HiveQL
     See :term:`Hive Query Language`

   HMaster
     Also known as Master. HMaster manages the RegionServer in the HBase, including the load balancing of the RegionServer, and the split, distribution, and
     migration of Regions. In an HA mode, HMaster includes a primary HMaster and a secondary HMaster.

   hot backup
     A hot backup is performed when a system is properly running. The backup data may be different from the actual data of the system because the data in the
     system keeps being updated.

   hot update
     WAF policies are delivered in real time without affecting ongoing services.

   IB Network
     The IB network features low latency and high bandwidth and is used in a number of High Performance Computing (HPC) projects. It uses the 100 Gbit/s Mellanox
     IB NIC, dedicated IB switch, and controller software UFM to ensure network communication and management, and uses the Partition Key to isolate IB networks of
     different tenants (similar to the VLAN in the Ethernet).

   Identity and Access Management
     Identity and Access Management (IAM) is a security management service provided by the public cloud system. This service includes identity management,
     permission management, and access control functions.

   identity provider
     An identity provider (IdP) is a system that provides identity authentication to users. For example, IAM is the IdP for the public cloud system. In IAM, the
     IdP for federated identity authentication is the enterprise's own identity authentication system.

   Image file
     An image file is a template that can be used to create ECSs. It contains an OS and preinstalled applications.

   In-Memory Database
     An in-memory database (IMDB, also main memory database system or MMDB or memory resident database) is a database management system that primarily relies on
     main memory for computer data storage. It is contrasted with database management systems that employ a disk storage mechanism.

   incremental backup
     A backup method used to back up only data space modified since the last backup. The last backup can be either full backup or incremental backup. Incremental
     backup can be implemented only on a target that has been fully backed up.

   incremental data migration
     Includes full migration by default. After full migration initializes the target database, incremental migration collects and analyzes logs to establish data
     consistency between the source and target databases, minimizing downtime.

   index (CSS)
     Index, similar to "Database" in the relational database (RDB), stores Elasticsearch data. It refers to a logical space that consists of one or more shards.

   index (DWS)
     An ordered data structure in the database management system. An index accelerates querying and updating of data in database tables.

   Index(MRS)
     A data structure that improves the speed of data retrieval operations on a database table at the cost of slower writes and increased storage space. Indices
     can be created using one or more columns of a database table, providing the basis for both rapid random lookups and efficient access of ordered records.

   input/output operations per second
     The number of I/O operations completed per second. This metric is reported as the average IOPS for a given time interval. RDS reports read and write IOPS
     separately at one minute intervals. Total IOPS is the sum of the read and write IOPS. Typical values for IOPS range from zero to tens of thousands per
     second.

   intelligent decoding
     WAF intelligently identifies multi-layer obfuscation of multiple types of code and performs in-depth decoding to obtain the deep-rooted intents of attackers.

   Internet of Things
     The Internet of things is the network of physical devices, vehicles, home appliances and other items embedded with electronics, software, sensors, actuators,
     and network connectivity which enables these objects to connect and exchange data.

   Intraselect MPLS
     MPLS is an L3VPN service provided by T-System International.

   IOPS
     See :term:`input/output operations per second`

   IoT
     See :term:`Internet of Things`

   Job
     MRS provides users with an application execution platform, which enables users to submit applications they have developed to a MRS cluster, execute the
     applications, and obtain results. MRS also enables users to submit SQL statements online as well as query and resolve structured data.

   Job Parameters
     Job parameters are the running parameters specified when a training job is submitted. You can save complex parameters and reuse them during subsequent job
     creation.

   Key
     Identifies the tag.

   Key Management Service
     KMS is a secure and reliable key management hosting service used for centrally managing and safeguarding users' keys.

   Kibana
     Kibana is an open-source analytics and visualization platform and works with Elasticsearch. You can use Kibana to search, view, and interact with data stored
     in Elasticsearch indices. You can also visualize your data in a variety of charts, tables, and maps.

   leeching
     In leeching, the attacker uses a link to direct access requests to a file on your website instead of placing the file on their own server. Typically, the
     file is big and consumes a lot of bandwidth, for example, an image or video. In some sense, you are paying for the access traffic to the file. Therefore, you
     are not only unpaid for the occupied bandwidth, the access rate to your website is also affected seriously.

   license model
     License type associated with a DB engine.

   life cycle management
     Covers phases from creating an object to deleting the object and indicates a management means to automatically delete objects that meet specific conditions.

   local DNS server
     A local DNS server which performs domain name lookup is usually located on the network to which your computer is attached. If you are using an Internet
     Service Provider (ISP), your DNS server is at your ISP. If you are using the network at your college or your office, you probably have a local DNS server
     somewhere near you at the server room. When you are on your computer, you will at some point type in the name of a computer somewhere on your local network
     or on the Internet. Your resolver software running on your computer looks in its local cache. If it does not find an answer, it sends that computer name to a
     DNS server. Whenever your DNS server runs into a name it doesn't recognize (something it hasn't looked up yet), it goes to a pre-configured list of root DNS
     servers to look it up. The local DNS server will send a query to a root server. The root server will respond with a list of servers who have been delegated
     the responsibility of resolving the requested domain name. Your local DNS server then sends another query to those 'authoritative' servers, and usually gets
     an answer.

   logical backup
     A procedure in which the structured query language (SQL) is used to abstract data from a database and store the data into a binary file. Logical backup is a
     technology that uses software to export data from a database and stores the data into a file which is in a format different from the file in the original
     database. Logical backup can only be used for logical restoration (data import) and cannot be used for physical restoration based on storage characters of
     the original database. Generally, logical backup is used for incremental backup and only backs up data that has changed since the last backup.

   low performance
     A situation where some nodes in a cluster become unavailable, which affects the cluster performance

   manual backup
     A user-initiated full backup of a DB instance. A manual backup is always retained until you explicitly delete it manually.

   Map
     A processing model function that processes a key-value pair to generate a set of intermediate key-value pairs.

   mapping
     A mapping is used to restrict the type of a field and can be automatically created based on data. It is similar to the schema in the database.

   MapReduce
     As a programming model that simplifies parallel computing, MapReduce gets its name from two key operations: Map and Reduce. Map divides one task into
     multiple tasks, and Reduce summarizes the processing results of these tasks and produces the final analysis result. MRS clusters allow users to submit
     self-developed MapReduce programs, execute the programs, and obtain the result.

   MapReduce Service
     MapReduce Service builds a reliable, secure, and easy-to-use operation and maintenance (O&M) platform and provides storage and analysis capabilities for
     massive data, helping address enterprise data storage and processing demands. Users can independently apply for and use the hosted Hadoop, Spark, HBase and
     Hive services to quickly create clusters on a host and provide storage and computing capabilities for massive data that has low requirements on realtime
     processing.

   massively parallel processing
     Massively parallel processing (MPP) refers to cluster architecture that consists of multiple machines. The architecture is also called a cluster system.

   Master Node
     A master node in a MapReduce Service cluster manages the cluster, assigns MapReduce executable files to core nodes, traces the execution status of each job,
     and monitors DataNode running status.

   metadata
     Data that provides information about other data. Metadata describes the source, size, format, or other characteristics of data. In the data field, metadata
     helps to explain the content of a data warehouse.

   metadata file
     Metadata files are SAML 2.0-compliant interface files. They contain the interface addresses and certificate information required by the SAML2.0 protocol. Two
     such files are available, one for the identity provider (IdP) and the other for the service provider (SP). The IdP and SP set up a trust relationship by
     exchanging their metadata files and configuring data in the file of each other. The public cloud system (SP) communicates with the IdP server using the
     address and certificate in the metadata file.

   Metric
     A metric is used to measure resource performance of a specific dimension. For example, CPU usage of ECSs is one metric and memory usage of ECSs is another.

   migration comparison
     Comparison of migration items between source and target databases, facilitating cloud users making decisions.

   migration logs
     Logs generated during database migration, which can be classified into the following levels: alarm, error, and info.

   migration progress
     Migration progress includes:Progress of an on-going full migration in percentageSynchronization latency between source and target databases of an on-going
     incremental migration.

   ModelArts
     ModelArts is a one-stop development platform for AI developers. With data preprocessing, semi-automated data labeling, distributed training, automated model
     building, and model deployment on the device, edge, and cloud, ModelArts helps AI developers build models quickly and manage the lifecycle of AI development.

   mongod
     A major process in DDS. mongod mainly processes data requests and manages data access.

   mongos
     A router for data read and write, providing a unified interface for accessing DB instances.

   MPP
     See :term:`massively parallel processing`

   MRS
     See :term:`MapReduce Service`

   Multi Dimensional eXpressions
     A query language for online analytical processing (OLAP) databases, as Structured Query Language (SQL) is a query language for relational databases. It is
     also a calculation language, with its syntax similar to spreadsheet formulas.

   multi-pattern matching
     A highly efficient multi-mode matching algorithm is used for preorder characteristic detection of request traffic, which greatly improves the performance of
     the detection engine.

   MX record priority
     The priority in an MX record specifies the sequence for an email server to receive emails. A smaller value indicates a higher priority. If multiple MX
     records have been created, the DNS server of the email sender preferentially sends emails to the email server with the highest priority. Once this email
     server becomes faulty, the DNS server of the sender automatically sends emails to the email server with the second highest priority.

   My Credential
     My Credential contains a user's attribute information and security information, including their user ID, verified mobile number, verified email address,
     password, and access key.

   NameNode
     A master server that manages the file system namespace and regulates access to files by clients. In HA mode, both NameNode and Secondary NameNode are
     provided.

   Namespace
     A namespace is a logical grouping of tables analogous to a database in relation database systems.

   NAS
     See :term:`Network Attached Storage`

   NAT
     The NAT Gateway service offers the Network Address Translation (NAT) function for computing instances, such as Elastic Cloud Servers (ECSs), in a Virtual
     Private Cloud (VPC), allowing these computing instances to access the Internet using elastic IP addresses (EIPs).

   Network Address Translation
     A type of network connection in hosted networking that enables you to connect your virtual machines to an external network when you have only one IP network
     address and the host computer uses that address.

   Network Attached Storage
     NAS is a method of file sharing. With NAS, a storage system has its own file systems inside and provides the file access service through Network File System
     (NFS).

   Network File System
     Network File System (NFS) is a distributed file system protocol that allows different computers and operating systems to share data over a network.
     Application programs on client computers use NFS to access data on server disks. NFS is a method for sharing disk files between UNIX-like systems. SFS
     supports NFS v3 currently.

   Network Time Protocol
     Defines the time synchronization mechanism and synchronizes the time between the distributed time server and the client.

   network traffic
     Network transmit throughput: indicates the rate of network traffic to and from the DB instance in MB per second.

   NFS
     See :term:`Network File System`

   NM
     See :term:`NodeManager`

   NN
     See :term:`NameNode`

   Node
     Compute nodes in the GaussDB NoSQL cluster.

   node
     A basic metering unit in DWS. It includes user-specified computing and storage resources and virtual machines (VMs) where DWS programs are deployed.

   NodeManager
     Launches and monitors the compute containers on machines in the cluster.

   NoSQL database
     Data in a NoSQL Database is communicated and organized based on the non-relational data structure. Based on different data structures, NoSQL Database can be
     classified as the following types: key-value, column-oriented, document-oriented, and graphic databases. Common NoSQL databases include: Memcached, Redis,
     MongoDB, Cassandra, HBase, MemacheDB, and BerkeleyDB.

   Notebook
     Notebook is an online interactive code development and debugging tool powered on the open source Jupyter Notebook. It is widely used in the AI field.

   number of DB connections
     The number of client sessions that are connected to the DB instance.

   O2O
     See :term:`Online to Offline`

   object
     A basic data unit in object storage service. It consists of object data and object metadata that describes object attributes.

   Object Storage Service
     Object Storage Service (OBS), a cloud storage service, provides data storage that features easy extensibility, high security, proven reliability, and high
     cost efficiency. Users can manage and use objects through HTTP-based interfaces. It is applicable to large-scale data storage services.

   OBS Cold
     OBS Cold is applicable to archiving rarely-accessed (once a year) data. The application scenarios include data archive and long-term data retention for
     backup. OBS Cold is secure, durable, and inexpensive, which can replace tape libraries. However, it can take up to hours to restore data from OBS Cold.

   OBS Standard
     OBS Standard features low access latency and high throughput. It is applicable to storing frequently-accessed (multiple times per month) hot data or small
     files (less than 1 MB) requiring quick response. The application scenarios include big data, mobile applications, hot videos, and social media images.

   OBS Warm
     OBS Warm is applicable to storing semi-frequently accessed (less than 12 times a year) data requiring quick response. The application scenarios include file
     synchronization or sharing, and enterprise-level backup. It provides the same durability, access latency, and throughput as OBS Standard but at a lower
     price. However, OBS Warm has lower availability than OBS Standard.

   OLAP
     See :term:`Online Analytical Processing`

   Online Analytical Processing
     A technology that uses multidimensional structures to provide rapid data access for analysis. OLAP source data is generally stored in data warehouses in a
     relational database.

   online database migration
     Database migration without service interruption (or with service interruption at the minute level).

   Online Service
     A model can be deployed as a cloud service. You can directly access the service by calling the RESTful API, which is used for the inference of a single piece
     of data.

   Online to Offline
     Online to offline, or O2O, refers to a marketing mode that uses online marketing and purchase to drive offline operation and consumption. O2O pushes offline
     stores' messages and promotions to Internet users by providing discounts and service reservations to convert Internet users to offline customers. This is
     especially suitable for products and services that must be consumed in offline stores, for example, catering, fitness, movies and performances, beauty salon.
     In 2013, the O2P marketing mode appeared, that is, the localized O2O marketing mode, formally bringing O2O into the localization process.

   Online Transaction Processing
     A transaction-oriented processing system, which immediately sends original user data to the computing center for processing and provides the processing
     result within a short period of time. OLTP is a main application of traditional relational databases. It processes basic and routine transactions, such as
     banking transactions.

   Open Database Connectivity
     A data access application programming interface (API) that supports access to any data source for which an ODBC driver is available. ODBC is aligned with the
     American National Standards Institute (ANSI) and International Organization for Standardization (ISO) standards for a database call-level interface (CLI).

   Operating system
     A computer program that manages computer hardware and software resources.

   Page
     Minimum memory unit for row storage in the relationship object structure. The default size of a page is 8 KB.

   partition
     Data records in DIS streams are distributed into partitions. Partitions are the base throughput unit of a DIS stream. The total capacity of a stream is the
     sum of the capacities of its partitions. One partition supports the data read rate of 2 MB/sec and the data write rate of 1000 records/sec and 1 MB/sec. When
     creating a DIS stream, you are expected to specify the number of partitions needed within your stream.

   partition key
     A partition key is used to segregate and route records to different partitions of a DIS stream. A partition key is specified by your data producer while
     adding data to a DIS stream. For example, assuming you have a stream with two partitions (partition 1 and partition 2). You can configure your data producer
     to use two partition keys (key A and key B) so that all records with key A are added to partition 1 and all records with key B are added to partition 2.

   performance metrics
     Reflect metrics of DB instance performance, including CPU usage, memory usage, storage space utilization, network traffic, database connections, transaction
     rate/database throughput, submit latency, storage latency, storage IOPS, storage throughput, and storage queue length.

   permission
     Permissions are used to control which operations users can perform on which objects.

   physical backup
     A backup mechanism, in which database files in the operating system are replicated from one place to another place, generally from a disk to a tape. Physical
     backup includes cold backup and hot backup.

   Planned failback
     Source servers and disks belong to the target AZ, and target servers and disks belong to the source AZ. When servers in the source AZ are running properly,
     you can stop the servers in the target AZ and perform a planned failback, specifically, to migrate services from the target AZ to the source AZ and enable
     the source servers and disks.

   Planned failover
     Source servers and disks belong to the source AZ, and target servers and disks belong to the target AZ. When servers in the target AZ are running properly,
     you can stop the servers in the source AZ and perform a planned failover, specifically, to migrate services from the source AZ to the target AZ and enable
     the target servers and disks.

   policy
     A policy consists of one or more statements, each of which describes one set of permissions and grants permissions to a set of resources. You can flexibly
     define permissions in a policy as required. A policy can contain multiple operation permissions for multiple cloud services or a single operation permission
     for a single cloud service. IAM uses policies to implement fine-grained permission management.

   Predefined Tag
     TMS provides the predefined function and the predeifned tag can be used by all cloud resources of services that support the tag function.

   primary DB instance
     A DB instance that provides read and write services.

   private DNS server
     The private DNS server is used only in VPCs. It responds to requests to access private domain names and other cloud services such as OBS. It also forwards
     requests to access public domain names.

   Private image
     A private image is created from an ECS or an external image file and is visible only to its creator. Each private image contains an OS, preinstalled public
     applications, and the creator's private applications. Creating ECSs using a private image frees you from repeatedly configuring ECSs.

   Private Link Access Service
     PLAS enables public cloud platform users to establish exclusive connections from their on-premise networks to VPCs on the public cloud platform.

   private network address
     The internal access address is accessible only to clients that are in the same subnet as the Cloud Search Service cluster.

   private zone
     A private zone records information about how you want to route traffic for a domain and its subdomains within one or more VPCs.

   Production
     A HANA production scenario where HANA officially applies in the production environment.

   project
     A collection of accessible resources in services. An account can create multiple projects in a region and authorize users based on these projects.

   Protected instance
     Indicates a server and its replication server (target server). A protected instance belongs to one protection group. Therefore, the source and target AZs of
     the protected instance are the same as those of the protected instance's protection group.

   Protection group
     Used to manage a group of servers to be replicated. One protection group is for servers in one VPC. If you have multiple VPCs, you need to create multiple
     protection groups.

   Protection group status
     Indicates the status of a protection group when users perform an operation on the protection group, such as creating or deleting a protection group, enabling
     or disabling protection, or performing a failover or planned failover.?

   PTR record
     A PTR record is used for reverse DNS lookup and resolves an IP address to a domain name.

   public DNS server
     A public DNS server functions as a recursive name server providing domain name resolution for any host on the Internet. It obtains DNS records from
     authoritative DNS servers and returns the results to users, and caches the records. The commonly used public DNS servers include 114.114.114.114 and 8.8.8.8.

   Public image
     A public image is provided by the public cloud system. It contains a standard OS and preinstalled public applications, and is visible to all users. You can
     configure the application environment and required software based on your requirements.

   public zone
     A public zone records information about how you want to route traffic on the Internet for a domain, such as example.com, and its subdomains.

   Quality Assure
     A quality assurance scenario where SAP HANA functions, performance, and reliability are fully verified.

   query operator
     An iterator or a query tree node, which is a basic unit for the execution of a query. Execution of a query can be split into one or more query operators.
     Common query operators include scan, join, and aggregation.

   queue depth
     The number of I/O requests in the queue waiting to be serviced. These are I/O requests that have been submitted by the application but have not been sent to
     the device because the device is busy servicing other I/O requests. Time spent waiting in the queue is a component of Latency and Service Time (not available
     as a metric). This metric is reported as the average queue depth for a given time interval. RDS reports queue depth at one minute intervals. Typical values
     for queue depth range from zero to several hundred.

   RDB
     See :term:`relational database`

   RDD
     See :term:`Resilient Distributed Datasets`

   RDS
     See :term:`Relational Database Service`

   RDS DB instance
     An RDS DB instance is the minimum RDS management unit. An RDS DB instance represents a relational database that runs independently. Users can create and
     manage DB instances of various database engines in the RDS system. RDS DB instances come in three types: primary DB instances, standby DB instances, and read
     replicas.

   rds incremental backup
     RDS automatically backs up data updated after the last automated or incremental backup every five minutes.

   rds storage type
     RDS automatically backs up data updated after the last automated or incremental backup every five minutes.

   read replica
     An active copy of another DB instance. Any updates to the data on the source DB instance are replicated to the read replica DB instance using the built-in
     replication feature of DB Engine.

   read-only
     When a data warehouse enters read-only state, it responds only to reads. The warehouse becomes read-only in many situations, for example, when you create a
     cluster snapshot or when 90% of the cluster's storage capacity is used.

   read/write splitting
     Enable the master instance to handle INSERT, UPDATE, and DELETE operations while the slave instance to handle SELECT operations.

   record set
     A record set is a collection of resource records of the same type in a zone.

   recovery point objective
     Indicates recovery time objective. It is the target time on the recovery of interrupted key businesses to an acceptable level. RTO is set to minimize an
     interruption's impacts on the services.

   recovery time objective
     Indicates recovery point objective. It is a service switchover policy, minimizing data loss during DR switchover. The data recovery point is used as the
     objective to ensure that the data used for DR switchover is the latest backup data.

   Redistributing
     The cluster goes into the state when it detects that the service data volume on some nodes is signifi-cantly larger than that on other nodes. In this case,
     the cluster automatically redistributes data on all nodes.

   Redistribution-failure
     The cluster goes into the state when data redistribu-tion fails, but no data loss occurs.

   redo log
     A log that records operations on the database. Redo logs contain the information required for performing these operations again. If a database is faulty,
     redo logs can be used to restore the database to its pre-fault state.

   Reduce
     A processing model function that merges all intermediate values associated with the same intermediate key.

   region
     A collection of resources divided by geographic location. Permissions can be granted to IAM users based on regions.

   RegionServer
     RegionServer is a service of HBase on each working node. It manages Regions, uploads Region load information, and facilitates HMaster in distributed,
     coordinated management.

   relational database
     Tables in an RDB are communicated and organized based on the relational data structure. RDB simplifies complex data structures into simple binary relation
     (two-dimensional tables). A relational database contains multiple tables and each table is known as a relation. Data management is performed through data
     manipulation languages (DMLs) GROUP BY, JOIN, UNION, and SELECT \* FROM. Common relational databases include: Oracle, MySQL, MariaDB, Microsoft SQL Server,
     Access, DB2, PostgreSQL, Informix, and Sybase.

   Relational Database Service
     RDS is a managed service that makes it easy to create, configure, operate, and scale a relational database in the cloud.

   reliability priority
     During a primary/standby switchover, if data is inconsistent between the primary and standby DB instances, the switchover is not performed and the database
     stops providing services. The reliability priority policy ensures data consistency.

   Remote Desktop Protocol
     A proprietary protocol developed by Microsoft.

   Remote Gateway
     A remote gateway is the public IP address of the physical device on the peer end in an IPsec VPN tunnel. The remote gateway of each IPsec VPN tunnel must be
     unique.

   Remote Subnet
     A remote subnet is the destination IP addresses reachable through the tunnel. All IP packets destined for this subnet are sent along the IPsec VPN tunnel.
     Multiple remote subnets can be configured. However, the remote subnet cannot conflict with the subnet of the VPC where the VPN resides.

   replica
     A copy in a shard used for storing indices. It can be understood as a replica shard.

   replica set
     A replica set consists of a set of mongod processes and provides a collection of data nodes to ensure data redundancy and high availability (HA).

   Replication factor
     The number of copies of a file is called the replication factor of that file.

   Replication pair
     Indicates a disk and its replication disk (target disk). A replication pair belongs to one protection group and can be attached to a protected instance in
     this protection group.

   Resilient Distributed Datasets
     Resilient Distributed Datasets, a distributed memory abstraction that lets programmers perform in-memory computations on large clusters in a fault-tolerant
     manner.

   Resource Template Service
     Resource Template Service (RTS) helps you simplify cloud computing resource management and automate O&M. You can compile a template file and define a
     collection of cloud computing resources, dependencies between resources, and resource configurations based on the template specifications defined in the RTS
     service. Then you can automatically create and configure all resources in the template using the orchestration engine to simplify deployment and O&M.

   ResourceManager
     Manages the global assignment of compute resources to applications.

   RM
     See :term:`ResourceManager`

   Rollup
     Rollup is the process in which Cloud Eye calculates the maximum, minimum, average, sum, and variance values based on sample raw data collected in different
     periods.

   Route Table
     A route table contains a set of rules that are used to determine where network traffic is directed. You can add routes to a route table to enable other ECSs
     in a VPC to access the Internet through the ECS that has a bound EIP.

   Row
     Row Key is one of HBase Table dimensions. It is an arbitrary array of bytes. Table is sorted in lexicographical order by it's Row Key.

   Row key
     Row key is the HBase primary key. Tables in HBase are lexicographically sorted in ascending order based on row key.

   RS
     See :term:`RegionServer`

   Scalable File Service
     Scalable File Service (SFS) is high-performance file storage that is scalable on demand. SFS file systems support standard file access protocols and can be
     mounted to Elastic Cloud Servers.

   schema
     A database object set that includes the logical structure, such as tables, views, sequences, stored procedures, synonyms, indexes, clusters, and database
     links.

   Secondary NameNode
     Performs periodic checkpoints of the namespace and helps keep the size of file containing log of HDFS modifications within certain limits at the NameNode.

   Secure Shell
     A set of standards and an associated network protocol that allow establishing a secure channel between a local and a remote computer.

   Secure Sockets Layer
     A security protocol that works at a socket layer. This layer exists between the TCP layer and the application layer to encrypt/decode data and authenticate
     concerned entities.

   segment
     A segment in the database indicates a part containing one or more regions. Region is the smallest range of a database and consists of data blocks. One or
     more segments comprise a tablespace.

   semi-synchronous replication
     An application initiates a data update (including insert, delete, and modify operations) request. After completing the update operation, the Master
     replicates data to a Slave. When at least one Slave receives the binlog, writes it to relay-log, and flushes it to the disk, the Slave can return a response
     to the Master. Compared to strong synchronous replication, semi-synchronous improves data replication performance because the Master does not wait for the
     Slave to flush the binlog to the disk. However, since the Slave responds to the Master before the commitment is done, data may be inconsistent between the
     Master and Slave.

   sensitive file access
     Sensitive files, such as configuration files and permission management files of operating systems and application service frameworks, should not be accessed
     on the Internet; otherwise, service security is compromised.

   sequence number
     Each data record has a sequence number that is unique within its partition. The sequence number is assigned by DIS when a data producer calls PutRecord or
     PutRecords operation to add data to a DIS stream. Sequence numbers for the same partition key generally increase over time; the longer the time period
     between write requests (PutRecord or PutRecords requests), the larger the sequence numbers become.

   server-side request forgery
     SSRF is an attacker-made vulnerability that can be used to send requests from servers. Typically, targets of SSRF are internal systems inaccessible from the
     Internet. The causes of SSRF are that the server can obtain data from other servers and that users have not filtered and limited destination addresses when
     they can.

   service provider
     A service provider (SP) is a system that provides services to users. In IAM, the SP for federated identity authentication is the public cloud system.

   shard (CSS)
     In Cloud Search Service, a shard is a logical partition. In the Elasticsearch search engine, an index consists of several shards. Each shard contains one or
     more replicas.

   shard (DDS)
     In Document Database Service, each shard is a mongod process that stores a subset of data for a DB instance. All shards store all data for a DB instance.
     Generally, each shard is deployed as a replica set to ensure data redundancy and HA.

   shared-nothing architecture
     A distributed computing architecture, in which none of the nodes share a CPU or storage resources. This architecture has good scalability.

   Shuffle
     A process of outputting data from a Map task to a Reduce task.

   slow HTTP attack
     In a slow HTTP attack, after managing to establish a connection with an HTTP server, the attacker specifies a large content-length and sends packets at very
     low rates, such as one byte per one to 10 seconds, and maintains the connection. If the client builds more such connections, available connections on the
     server will be exhausted bit by bit, causing the server unable to provide services.

   Small Computer System Interface
     SCSI is an EVS disk device type. SCSI device type EVS disks support transparent SCSI command transmission, allowing ECS OSs to directly access the underlying
     storage media. Besides basic SCSI read/write commands, SCSI device type EVS disks also support advanced SCSI commands, such as SCSI persistent reservations.
     Such EVS disks are suitable for cluster application scenarios that ensure data security using the lock mechanism.

   snapshot
     A full backup of a cluster. Snapshots are stored in the storage space of Object Storage Service (OBS).

   snapshot restoration
     A snapshot can be used to restore a cluster to a newly created one that has the same specifications. Currently, you can restore a cluster only to a new one.

   Software Development Kit
     It is a collection of development tools that are used by software engineers to create application software for specific software packages, software
     frameworks, hardware platforms, and operating systems. Generally, the SDK is used for developing Windows applications. It can simply provide some API files
     for a programming language, but may also include complex hardware that can communicate with an embedded system.

   Software Repository for Container
     Software Repository for Container (SWR) provides easy, secure, and reliable management over Docker container images throughout their lifecycle, facilitating
     the deployment of containerized applications.

   solid-state drive
     SSDs are built on solid electronic storage chip arrays. Each SSD consists of a control unit and a storage unit (a flash and a DRAM chip). The interface
     specifications, definition, functions, and usage of an SSD are the same as those of a common hard disk. SSDs are widely applied in fields such as military,
     vehicles, industrial control, video surveillance, network surveillance, network terminals, electricity, medical, aeronautics, and navigation equipment.

   Source AZ
     Specifies the location of a server. It is specified when you create a protection group.

   source DB instance
     A source DB instance functions as the data source in data replication.

   spam
     The word "Spam" as applied to Email means "Unsolicited Bulk Email". Unsolicited means that the Recipient has not granted verifiable permission for the
     message to be sent. Bulk means that the message is sent as part of a larger collection of messages, all having substantively identical content.

   Spark
     MRS deploys and hosts Apache Spark clusters in the cloud, and Spark is a distributed and parallel data processing framework.

   Spark SQL
     Spark SQL is an important component of Apache Spark and subsumes Shark. It helps engineers who understand conventional databases but do not know MapReduce
     quickly get started.

   SPF
     Sender Policy Framework (SPF) is a simple email-validation system designed to detect email spoofing by providing a mechanism to allow receiving mail
     exchangers to check that incoming mail from a domain comes from a host authorized by that domain's administrators. The list of authorized sending hosts for a
     domain is published in the Domain Name System (DNS) records for that domain in the form of a specially formatted TXT record.

   SQL
     See :term:`Structure Query Language`

   SQL injection
     SQL injection is a common web attack. Attackers inject SQL statements into query character strings of background databases to deceive servers into executing
     the malicious SQL statements. Then, attackers can obtain sensitive information, add users, export files, or even gain the highest permissions on the
     databases or even the systems.

   SSD
     See :term:`solid-state drive`

   SSL
     See :term:`Secure Sockets Layer`

   Stack
     A stack is a collection of resources, which may include multiple ECSs, networks, and EVS disks. You can use a template to create a stack that includes a set
     of resources to accommodate the specified application framework or components included in the templates.

   Stage
     Each job gets divided into smaller sets of tasks called stages that depend on each other.

   standby DB instance
     A standby DB instance is a backup for the primary DB instance. It automatically takes over services from the standby DB instance in case of failures to
     enhance database availability. When creating a primary DB instance, users can determine whether to create a synchronous standby DB instance with the same
     specifications as the primary one.

   static website hosting
     A service mode in which users store static website files on object storage services, set buckets to the hosting mode, and visit static websites by accessing
     buckets in the object storage services.

   statistics
     Information that is automatically collected by databases, including table-level information (number of tuples and number of pages) and column-level
     information (distribution histograms of value ranges of columns). Statistics in databases are used to estimate the cost of query plans to find the plan with
     the lowest cost.

   storage capacity
     Size of the underlying storage resources that can be used to store indexes and logs.

   Storage Disaster Recovery Service
     Storage Disaster Recovery Service provides disaster recovery (DR) services for many public cloud services, such as Elastic Cloud Server, Elastic Volume
     Service, and Dedicated Storage Service.?

   storage space
     The space of underlying storage resources for storing data and logs of a database.

   storage type
     Storage resources are classified into different types based on their attributes. For example, storage resources can be classified into magnetic medium and
     solid state disks (SSDs) in terms of the storage medium, and into common I/O, high I/O, and ultra-high I/O storage resources in terms of the I/O level.

   stored procedure
     A group of SQL statements compiled to perform certain functions and stored in a large database system. Users can specify a name and parameters (if any) for a
     stored procedure to execute the procedure.

   strong synchronous replication
     An application initiates a data update (including insert, delete, and modify operations) request. After completing the update operation, the Master
     replicates data to a Slave immediately. After receiving the data, the Slave returns a success message to the Master. Only after receiving a message from the
     Slave, the Master can return a response to the application. Since data is replicated synchronously from the Master to the Slave, unavailability of the Slave
     will affect the operations on the Master, and unavailability of the Master will not cause data inconsistency.

   Structure Query Language
     Structure Query Language (SQL) is a standard database query language. It consists of DDL, DML, and DCL.

   Structured Query Language
     A programming language widely used for accessing, querying, updating, and managing data in a relational database.

   submit latency
     The elapsed time between the submission of a request and its completion. This metric is closely related with the storage write latency metric. A high storage
     write latency may cause a high submit latency.

   Suite on HANA
     An SAP HANA application scenario where SAP HANA is used as the database of the business suite (for example, ERP software).

   switchover policy
     Policy used to switch over the primary DB instance to the standby DB instance in the primary/standby HA architecture. The switchover policy priority can be
     reliability or availability. By default, reliability is selected.

   SWR
     See :term:`Software Repository for Container`

   SYN flood
     See :term:`SYN flood attack`

   SYN flood attack
     In a SYN flood attack, the malicious client (the attacker) uses forged SYN packets (the source addresses of which are fake or non-existent) to send
     connection requests to the target server. The target server acknowledges those requests by returning SYN-ACK. However, the client does not respond to the
     server with an expected ACK packet. As a result, the target server has a large number of half-open connections that last until timeout. Those connections
     exhaust server resources, causing the target server to fail to create normal TCP connections, as expected by the attacker.

   Synchronization status
     Indicates the status of the data replication between the source and target AZ.

   System disk image
     A system disk image contains an OS for running services and application software. It can be used to create system disks, and can also be directly used to
     create ECSs. Through system disk images, you can migrate your service running environment to the cloud.

   system table
     A table storing meta information about the database. The meta information includes user tables, indexes, columns, functions, and data types in a database.

   table
     A set of columns and rows. The value in each column represents data of a certain type. For example, if a table contains people's names, cities, and states,
     it has three columns: Name, City, and State. In every row in the table, the Name column contains a name, the City column contains a city, and the State
     column contains a state.

   Table(MRS)
     HBase Table is a three dimensional sorted map. It maps from Cartesian product of row key, column key and timestamp to cell value. All HBase data is stored in
     cell of tables.

   tablespace
     A tablespace is a logical storage structure that contains tables, indexes, large objects, and long data. A tablespace provides an abstract layer between
     physical data and logical data, and provides storage space for all database objects. When you create a table, you can specify which tablespace it belongs to.

   Tag
     Identifies cloud resources for purposes of easy categorization and quickly search. A tag is composed of a key-value pair. A key in a tag can have multiple
     values. A cloud resource must have a unique key.

   Tag Management Service
     A platform used for centrally managing tags and providing the tag planning function.

   Target AZ
     Specifies the location of a replication server. It is specified when you create a protection group. In this version, the source and target AZs must be
     different and in the same region.

   Task
     A task is an arithmetic unit bearing service logic and a unit of work that will be sent to one executor.

   TCP attack
     In Transmission Control Protocol (TCP) attacks, attackers send forged TCP packets to target servers, with abnormal flag settings intended to make the servers
     unresponsive to normal user requests.

   Template
     An RTS template is a user-readable, easy-to-write file that describes how to deploy a set of resources and install the required software. Templates specify
     the resources to use, the attributes to set, and the parameters required for automatic deployment of a specific application. Template files can be in the
     YAML or JSON format.

   Test
     A HANA test scenario where development engineers test application software and SAP HANA to verify the functions of application software after application
     software development is complete.

   throughput
     The number of bytes per second transferred to or from a disk. This metric is reported as the average throughput for a given time interval. RDS reports read
     and write throughput separately at one minute intervals using units of megabytes per second (MB/s). Typical values for throughput range from zero to the I/O
     channel's maximum bandwidth.

   Timestamp
     Different versions of the same data for the index, the timestamp type is 64-bit integer. Timestamp can be automatically assigned by the customer or by the
     explicit assignment when data is written to HBase.

   token
     A token contains user information such as the identity and permissions. A token is issued to a user after the user identity is authenticated.

   TPC Benchmark DS
     The TPC Benchmark DS (TPC-DS) is a decision support benchmark provided by the Transaction Processing Performance Council (TPC) that models several generally
     applicable aspects of a decision support system, including queries and data maintenance. The benchmark provides a representative evaluation of performance as
     a general purpose decision support system. For more information about the benchmark, visit http://www.tpc.org/tpcds/.

   TPC-DS
     See :term:`TPC Benchmark DS`

   traffic cleaning
     Traffic cleaning is a network security service used to precisely identify and discard abnormal traffic on a network to ensure passing of normal traffic.
     Traffic cleaning is mainly used to protect computers against DDoS attacks.

   Training
     A HANA training scenario where the users are trained for the deployed SAP HANA or the deployed SAP HANA is demonstrated.

   Training Job
     A training job is a task submitted by you to train a model. You can edit and develop the code logic of the task in the development environment. After job
     running, a model is outputted.

   transaction
     A logical unit of work performed within a database management system against a database. A transaction consists of a limited database operation sequence, and
     must have ACID features.

   transaction rate/database throughput
     Number of completed transactions in a specified period, generally expressed in transactions per minute (TPM) or transactions per second (TPS). Another term
     of Transaction Rate is Database Throughput. Do not confuse it with the disk throughput. They may be irrelevant. Databases achieving a high transaction rate
     may have little or disk throughput, for example, by reducing load by reading from their cache.

   True Random Number Generator
     A TRNG is a device that generates unpredictable random numbers by physical processes instead of computer programs.

   TTL
     TTL is short for time to live, which specifies the cache period of resource records on a local DNS server. When the local DNS server receives a resolution
     request of a domain name, it asks the authoritative DNS server of the domain name for the required resource record, and then caches the record for a period
     of time. During this period, if the local DNS server receives resolution requests of this domain name again, it does not request the record from the
     authoritative DNS server, but directly returns a result from the record in its cache. The time period during resource records are cached on the local DNS
     server is specified by the TTL value.

   UDP flood
     See :term:`UDP flood attack`

   UDP flood attack
     In a User Datagram Protocol (UDP) flood attack, the attacker sends a large number of typically large UDP packets over a botnet at very high rates, thereby
     exhausting server resources and causing servers unresponsive to normal user requests.

   user
     A user uses cloud services and corresponds to an employee, system, or application. Users have identity credentials (passwords and access keys) and can log in
     to the management console or access APIs.

   user group
     A group of users who share the same responsibilities. After a user is added to a user group, it has all of the permissions that are assigned to the group.
     User groups help improve the efficiency of permission management.

   User-defined VLAN
     You can use the Ethernet NICs (10GE defined in BMS specifications) not used by the system to configure a user-defined VLAN. The QinQ technology is used to
     isolate networks and provide additional physical planes and bandwidths. You can allocate VLAN subnets to isolate traffic in various scenarios including SAP
     HANA and VMware. User-defined VLAN NICs are in pairs. You can configure NIC bonding to achieve high availability.

   Value
     Indicates the concrete content of a tag.

   versioning
     Records and stores the versions of objects at different times in the system to trace and manage multiple object versions, so that data of a specific version
     can be recovered when an anomaly occurs.

   Very-High-Speed Integrated Circuit Hardware Description Language
     A hardware description language used in electronic design automation to describe digital and mixed-signal systems such as field-programmable gate arrays and
     integrated circuits. VHDL can also be used as a general purpose parallel programming language.

   Virtual Block Device
     VBD is an EVS disk device type, which is also the default device type for EVS disks. VBD device type EVS disks only support basic SCSI read/write commands.
     Such EVS disks are suitable for enterprise office applications and development and test environments.

   Virtual Network Interface Card
     A NIC virtualized from a physical NIC by the virtualization software. A vNIC works like a physical NIC for a virtual machine.

   Virtual Private Cloud
     A Virtual Private Cloud (VPC) is a secure, isolated, and logical network environment. You can create virtual networks in a VPC. The virtual networks provide
     the same network functions as those provided by a physical network, as well as providing advanced network services, such as elastic IP addresses and security
     groups.

   Volume Backup Service
     Volume Backup Service (VBS) backs up and restores Elastic Volume Service (EVS) disks. You can configure backup policies to implement periodic incremental
     backup of EVS disks and to store data across data centers so as to improve data reliability.

   VPC
     Indicates the VPC of the protection group. A VPC facilitates internal network management and configuration, allowing secure and quick modifications to
     networks. Servers in the same VPC can communicate with each other, but those in different VPCs cannot communicate with each other by default.

   VPC Peering
     A VPC peering connection is a networking connection between two VPCs that enables you to route traffic between them using private IP addresses. ECSs in
     either VPC can communicate with each other just as if they were in the same VPC. You can create a VPC peering connection between your own VPCs, or between
     your VPC and another tenant's VPC within the same region.

   WAL
     See :term:`write-ahead logging`

   WAL(MRS)
     See :term:`Write Ahead Log`

   Web Application Firewall
     Web Application Firewall (WAF) is designed to keep web services stable and secure. It examines all HTTP and HTTPS requests to detect and block attacks such
     as Structure Query Language (SQL) injections, cross-site scripting (XSS), webshell upload, command or code injections, file inclusions, sensitive file
     access, third-party vulnerability exploits, CC attacks, malicious crawlers, and cross-site request forgery (CSRF).

   webshell
     A webshell is an attack script. After intruding a website, an attacker mixes .asp, .php, .jsp, or .cgi files with normal web page files. Then, the attacker
     can access web backdoors using a browser. In other words, the attacker has obtained an environment to run his malicious commands to control the website
     server. For this reason, webshells are also called backdoor tools.

   wildcard DNS record
     A wildcard DNS record set is used to match requests for all subdomains in a zone. You specify the host name in a domain name to an asterisk (*) when creating
     a record set so that the DNS service can map subdomains to the specified IP address.

   World Wide Name
     A World Wide Name (WWN) or World Wide Identifier (WWID) is a unique identifier used in storage technologies including Fiber Channel, Advanced Technology
     Attachment (ATA) or Serial Attached SCSI (SAS). A WWN may be employed in a variety of roles, such as a serial number or for addressability.

   Write Ahead Log
     An efficient database algorithm. For the same amount of data, while using WAL log, database system during the transaction commits disk writes only about half
     of the traditional rollback log, greatly improving the efficiency of the database disk I/O operations, thereby improving the performance of the database.
     Each incremental data loads in HBase are written to WAL.

   write-ahead logging
     Write-ahead logging (WAL) is a standard method for logging a transaction. Corresponding logs must be written into a permanent device before a data file
     (carrier for a table and index) is modified.
