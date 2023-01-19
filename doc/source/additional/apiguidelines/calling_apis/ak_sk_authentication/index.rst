AK/SK Authentication
====================

When you use API Gateway to send requests to underlying services, the requests must be signed using the AK and SK.

.. note::

   AK is a unique identifier that is associated with a secret access key; the access key ID and secret access key are used together to sign requests
   cryptographically.

   SK is a key that is used in conjunction with an access key ID to cryptographically sign requests. Signing a request identifies the sender and prevents the
   request from being altered.

The AK/SK authentication process is as follows:

1. A standard request is created.

2. A to-be-signed string is created using the request and other related information.

3. A signature is calculated using the AK/SK and to-be-signed string.

4. The generated signature is added as a header or a query parameter in the HTTP request.

5. After receiving the request, API Gateway performs
   `1 <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328004.html#apig-en-api-180328004__li889518531076>`__ to
   `3 <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328004.html#apig-en-api-180328004__li198402221915>`__ to calculate a signature.

6. The new signature is compared with the signature generated in
   `3 <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328004.html#apig-en-api-180328004__li198402221915>`__. If they are consistent, the request
   is processed; otherwise, the request is rejected.

:ref:`Figure 1 <apig-en-api-180328004__fig104904517537>` shows the process of calling APIs through AK/SK authentication.

.. _apig-en-api-180328004__fig104904517537:

.. figure:: /_static/images/api_calling_process_flow.png
   :alt: **Figure 1** API calling process flow

   **Figure 1** API calling process flow

.. note::

   -  If a failure occurs in any step, the failure will be returned to the client application.

   -  The cached token is valid for 15 minutes by default.

.. toctree::

   generating_an_ak_and_sk
   signing_a_request
   sample_code
