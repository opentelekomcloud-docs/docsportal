Sample Code
===========

Scenario
--------

This section describes how to call the API of a public cloud service by using Eclipse.

The following code shows how to sign a request and how to use an HTTP client to send an HTTPS request. The code is categorized into three classes:

-  **AccessService**: an abstract class that merges the GET, POST, PUT, and DELETE methods into the access method.

-  **Demo**: execution entry that simulates GET, POST, PUT, and DELETE requests.

-  **AccessServiceImpl**: implementation of the access method. The code required for API Gateway communication is included in the access method.

You can download the sample code package from https://apig-demo.obsEndpoint/java/SdkDemo.zip.

You can download the sample code package from https://apig-demo.obs.eu-de.otc.t-systems.com/java/SdkDemo.zip.

.. important::

   The JDK version cannot be earlier than 1.8.

Procedure
---------

1. Download the sample code package and decompress it.

2. Import the sample project to Eclipse.

..

   .. figure:: /_static/images/sample_code_select_project.png
      :alt: **Figure 1** Selecting an existing project

      **Figure 1** Selecting an existing project

   .. figure:: /_static/images/sample_code_select_project.png
      :alt: **Figure 2** Selecting the sample code file after decompression

      **Figure 2** Selecting the sample code file after decompression

   .. figure:: /_static/images/sample_code_project_structure.png
      :alt: **Figure 3** Structure of the project after importing

      **Figure 3** Structure of the project after importing

3. Edit the main method in the **Demo.java** file.

..

   Replace the bold texts with actual values. If you use other methods, such as POST, PUT, and DELETE, see the corresponding annotations.

   Replace the parameters in the URL, for example, **project_id**.

   For details on how to obtain your region name, service name, AK/SK, project ID, and domain ID, see `Obtaining Required
   Information <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html>`__.

   .. code-block:: java

      //TODO: Replace eu-de with the name of the region in which the service to be accessed is located.
      private static final String region = "eu-de";

      //TODO: Replace vpc with the name of the service you want to access. For example, ecs, vpc, iam, and elb.
      private static final String serviceName = "vpc";

      public static void main(String[] args) throws UnsupportedEncodingException
      {
      //TODO: Replace the AK and SK with those obtained on the My Credential page.
      String ak = "ZIRRKMTWPTQFQI1WKNKB";
      String sk = "Us0mdMNHk******YrRCnW0ecfzl";

      //TODO: To specify a project ID (multi-project scenarios), add the X-Project-Id header.
      //TODO: To access a global service, such as IAM, DNS, CDN, and TMS, add the X-Domain-Id header to specify an account ID.
      //TODO: To add a header, find "Add special headers" in the AccessServiceImple.java file.

      //TODO: Test the API
      String url = "https://vpc.eu-de.otc.t-systems.com/v1/{project_id}/vpcs/{vpc_id}";
      get(ak, sk, url);

      //TODO: When creating a VPC, replace {project_id} in postUrl with the actual value.
      //String postUrl = "https://vpc.eu-de.otc.t-systems.com/v1/{project_id}/cloudservers";
      //String postbody ="{\"vpc\": {\"name\": \"vpc\",\"cidr\": \"192.168.0.0/16\"}}";
      //post(ak, sk, postUrl, postbody);

      //TODO: When querying a VPC, replace {project_id} in url with the actual value.
      //String url = "https://vpc.eu-de.otc.t-systems.com/v1/{project_id}/vpcs/{vpc_id}";
      //get(ak, sk, url);

      //TODO: When updating a VPC, replace {project_id} and {vpc_id} in putUrl with the actual values.
      //String putUrl = "https://vpc.eu-de.otc.t-systems.com/v1/{project_id}/vpcs/{vpc_id}";
      //String putbody ="{\"vpc\":{\"name\": \"vpc1\",\"cidr\": \"192.168.0.0/16\"}}";
      //put(ak, sk, putUrl, putbody);

      //TODO: When deleting a VPC, replace {project_id} and {vpc_id} in deleteUrl with the actual values.
      //String deleteUrl = "https://vpc.eu-de.otc.t-systems.com/v1/{project_id}/vpcs/{vpc_id}";
      //delete(ak, sk, deleteUrl);
      }

4. (Optional) To call a service API of a sub-project or to add a self-defined header, perform the following steps:

   a. In the main method in the **Demo.java** file, replace **project_id** with the sub-project ID of the API.

      .. code-block:: java

         //TODO: Test the API
         String url = "https://vpc.eu-de.otc.t-systems.com/v1/{project_id}/vpcs/{vpc_id}";
         get(ak, sk, url);

   b. Locate the following lines in the **AccessServiceImpl.java** file, delete "//" to activate the code line, and replace the sub-project ID with the actual one.

      .. code-block:: java

         //TODO: Add special headers.
         //request.addHeader("X-Project-Id", "xxxxx");

   c. Repeat `4.b <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328008.html#apig-en-api-180328008__li11427145613263>`__ to add other
   self-defined headers.

5. Compile and run the API calling code.

   Find **Demo.java** in the left pane of the Package Explorer, right-click, and choose **Run AS** > **Java Application**.

   View the API call logs on the console.
