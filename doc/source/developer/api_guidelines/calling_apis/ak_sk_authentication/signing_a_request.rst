Signing a Request
=================

.. _apig-en-api-180328006__li17137133433914:

1. Introduce the API Gateway signing SDK in the project.

   a. Download the API Gateway signing tool from the following link:

..

   https://apig-demo.obs.eu-de.otc.t-systems.com/java/java-sdk-core.zip

   b. Decompress the downloaded package to obtain a **.jar** file.

   c. Add the decompressed **.jar** file to a project, for example, Eclipse, as a dependency package. See the following figure.

   .. figure:: /_static/images/sdkdemo_properties.png

2. Sign the request.

..

   The signing method is integrated into the **.jar** file added in
   :ref:`1 <apig-en-api-180328006__li17137133433914>`. Before sending the request, sign
   the requested content. The signature obtained is included in the HTTP header of the request.

   For details, see :ref:`Sample Code <apig-en-api-180328008>`.

   .. important::

      The JDK version cannot be earlier than 1.8.
