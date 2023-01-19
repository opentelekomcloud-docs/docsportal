.. _apig-en-api-180328009:

Obtaining Required Information
==============================

Obtain the required information before calling APIs.

Required Information
--------------------

.. table:: **Table 1** Required information

   +----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
   | **Item**                                           | **Parameter**                                      | **Description**                                    |
   +====================================================+====================================================+====================================================+
   | Service name                                       | serviceName                                        | Service name, for example, **iam**, **vpc**, and   |
   |                                                    |                                                    | **ecs**.                                           |
   +----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
   | Region/Endpoint                                    | ``-``                                              | Region and endpoint.                               |
   |                                                    |                                                    |                                                    |
   |                                                    |                                                    | See `Regions and                                   |
   |                                                    |                                                    | Endpoints <https://docs.otc.t-systems.com/en-us/en |
   |                                                    |                                                    | dpoint/index.html>`__.                             |
   +----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
   | Project ID                                         | project_id                                         | Project ID, which is configured in the URI in most |
   |                                                    |                                                    | cases.                                             |
   |                                                    |                                                    |                                                    |
   |                                                    |                                                    | For details about how to obtain the value of this  |
   |                                                    |                                                    | parameter, see :ref:`Obtaining a Project ID        |
   |                                                    |                                                    | <apig-en-api-180328009__section8415105514222>`.    |
   +----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
   | username/password                                  | username/password                                  | Username and password, which are used to obtain a  |
   |                                                    |                                                    | token in token authentication mode.                |
   +----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
   | AK/SK                                              | ak/sk                                              | AK/SK pair.                                        |
   |                                                    |                                                    |                                                    |
   |                                                    |                                                    | It is used in AK/SK authentication mode.           |
   |                                                    |                                                    |                                                    |
   |                                                    |                                                    | For details about how to obtain the value of this  |
   |                                                    |                                                    | parameter, see :ref:`Generating an AK and          |
   |                                                    |                                                    | SK <apig-en-api-180328005>`.                       |
   +----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
   | uri                                                | uri                                                | Request path and parameters.                       |
   |                                                    |                                                    |                                                    |
   |                                                    |                                                    | Obtain the URI according to the API reference      |
   |                                                    |                                                    | guide of each service.                             |
   +----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
   | Domain Name                                        | ``-``                                              | Account name, which is used to obtain a token in   |
   |                                                    |                                                    | token authentication mode.                         |
   |                                                    |                                                    |                                                    |
   |                                                    |                                                    | For details about how to obtain the value of this  |
   |                                                    |                                                    | parameter, see :ref:`Obtaining the Domain Name and |
   |                                                    |                                                    | Domain ID                                          |
   |                                                    |                                                    | <apig-en-api-180328009__section208398123112>`.     |
   +----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
   | Domain ID                                          | X-Domain-Id                                        | Account ID, which is used to:                      |
   |                                                    |                                                    |                                                    |
   |                                                    |                                                    | -  Obtain a token in token authentication mode.    |
   |                                                    |                                                    |                                                    |
   |                                                    |                                                    | -  Access global services, such as IAM, DNS, and   |
   |                                                    |                                                    |    CDN, in AK/SK authentication mode. You must     |
   |                                                    |                                                    |    specify a domain ID in the header.              |
   |                                                    |                                                    |                                                    |
   |                                                    |                                                    | For details about how to obtain the value of this  |
   |                                                    |                                                    | parameter, see :ref:`Obtaining the Domain Name and |
   |                                                    |                                                    | Domain ID                                          |
   |                                                    |                                                    | <apig-en-api-180328009__section208398123112>`.     |
   +----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
   | Sub-project ID                                     | X-Project-Id                                       | Sub-project ID, which is used in multi-project     |
   |                                                    |                                                    | scenarios.                                         |
   |                                                    |                                                    |                                                    |
   |                                                    |                                                    | For details about how to obtain the value of this  |
   |                                                    |                                                    | parameter, see :ref:`Obtaining a Project ID        |
   |                                                    |                                                    | <apig-en-api-180328009__section8415105514222>`.    |
   +----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

.. _apig-en-api-180328009__section8415105514222:

Obtaining a Project ID
----------------------

A project ID needs to be specified in the URIs of some APIs. Therefore, you need to obtain the project ID before calling APIs. The following procedure describes
how to obtain a project ID:

1. Log in to the management console.

2. Click the username and choose **My Credential** from the drop-down list.

..

   On the **My Credential** page, view project IDs in the project list.

   .. figure:: /_static/images/viewing_project_ids.jpg
      :alt: **Figure 1** Viewing project IDs

      **Figure 1** Viewing project IDs

   In multi-project scenarios, expand the region, and obtain your sub-project ID from the **Project ID** column.

.. _apig-en-api-180328009__section208398123112:

Obtaining the Domain Name and Domain ID
---------------------------------------

When you call APIs, your domain name and domain ID are required in some URLs. Obtain your domain name and domain ID on the console by performing the following
steps:

1. Log in to the management console.

2. Click the username and choose **My Credential** from the drop-down list.

..

   On the **My Credential** page, view the domain name and domain ID.

   .. figure:: /_static/images/viewing_domain_id.png
      :alt: **Figure 2** Viewing the domain name and domain ID

      **Figure 2** Viewing the domain name and domain ID
