Token Authentication
====================

Scenario
--------

If API requests are authenticated using tokens, the request header must contain **X-Auth-Token** (token information).

This section describes how to call an API to complete token authentication.

Procedure
---------

1. Send **POST https://**\ *IAM endpoint*\ **/v3/auth/tokens** to obtain the endpoint of IAM and the region name in the message body.

..

   See `Regions and Endpoints <https://docs.otc.t-systems.com/en-us/endpoint/index.html>`__.

   An example request is as follows:

   .. note::

      Replace the texts in italic with actual ones. For details, see *Identity and Access Management API Reference*.

      Log in to the management console, click your username in the upper right corner, and choose **My Credential** from the drop-down list. On the **My
      Credential** page, obtain your username, domain name, and project ID.

   .. code-block:: json

      {
        "auth": {
          "identity": {
            "methods": [
              "password"
            ],
            "password": {
              "user": {
                "name": "username", //Obtain your username from the My Credential page.
                "password": "password",
                "domain": {
                  "name": "domainname" //Obtain your domain name from the My Credential page.
                }
              }
            }
          },
          "scope": {
            "project": {
              "id": "0215ef11e49d4743be23dd97a1561e91" //Obtain your project ID from the My Credential page.
            }
          }
        }
      }

2.  Obtain the token. For details, see section "Obtaining the User Token" in the *Identity and Access Management API Reference*. If the request is successful, the
value of the X-Subject-Token header in the response is the token.

   The following figures illustrate how to use Postman to manually obtain a token.

   .. figure:: /_static/images/token_authentication_example_request.png
      :alt: **Figure 1** Example request

      **Figure 1** Exmple request

   .. figure:: /_static/images/obtain_x-subject-token.png
      :alt: **Figure 2** Obtain **X-Subject-Token** from the header of the response message.

      **Figure 2** Obtain **X-Subject-Token** from the header of the response message.

3.  Call a service API, add the **X-Auth-Token** header with the token obtained in
`2 <https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328003.html#apig-en-api-180328003__li2615608112249>`__.
