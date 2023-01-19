Overview of REST APIs
=====================

API Gateway provides RESTful APIs.

REST provides APIs to create, query, update, delete, and access service resources.

A REST API request/response pair is divided into the following parts:

-  Request URI

-  Request method

-  Request headers

-  Request body

-  Response headers

-  Response body

Request URI
-----------

A request URI consists of the following parts:

**{URI-scheme} :// {Endpoint} / {resource-path} ? {query-string}**

Although a request URI is a part of a request header, most programming languages or frameworks require the request URI to be separately transmitted, rather than
being conveyed in a request message.

.. _apig-en-api-180328002__t1797260c744a4e1a85d354f259cae55a:

.. table:: **Table 1** URI parameter description

   +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | **Parameter**                                                                 | **Description**                                                               |
   +===============================================================================+===============================================================================+
   | URI-scheme                                                                    | Protocol used to transmit the request.                                        |
   +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | Endpoint                                                                      | Domain name or IP address of the server where the RESTful service endpoint is |
   |                                                                               | hosted. You can obtain the value from `Regions and                            |
   |                                                                               | Endpoints <https://docs.otc.t-systems.com/en-us/endpoint/index.html>`__.      |
   +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | resource-path                                                                 | Path in which the resource requested by the API is located. The path is       |
   |                                                                               | provided by the URI module of APIs, for example, **v3/auth/tokens**.          |
   +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | Query string                                                                  | This is an optional parameter. For example, the value can be the API version  |
   |                                                                               | or resource selection criteria.                                               |
   +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

Request Method
--------------

HTTP method: the type of requested operation.

.. _apig-en-api-180328002__table26515221161:

.. table:: **Table 2** HTTP methods supported

   +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | **Method**                                                                    | **Description**                                                               |
   +===============================================================================+===============================================================================+
   | GET                                                                           | Requests a server to provide a specified resource.                            |
   +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | PUT                                                                           | Requests a server to update a specified resource.                             |
   +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | POST                                                                          | Requests a server to add resources or perform special operations.             |
   +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | DELETE                                                                        | Requests a server to delete a specified resource, for example, an object.     |
   +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | HEAD                                                                          | Similar to the GET method, the HEAD method requests a server to provide the   |
   |                                                                               | specified resource, but the server returns only the response header           |
   |                                                                               | (excluding the response body) to this request.                                |
   +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | PATCH                                                                         | Requests a server to update a part of a specified resource.                   |
   |                                                                               |                                                                               |
   |                                                                               | If the resource does not exist, the PATCH method may create a new resource.   |
   +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

Request Headers
---------------

Optional header fields: For example, such fields could be those required by a specified URI and HTTP method. :ref:`Table 3 <apig-en-api-180328002__t24b12299374a4f4ba9fbf5880aec2658>`
describes common HTTP request header fields.

.. _apig-en-api-180328002__t24b12299374a4f4ba9fbf5880aec2658:

.. table:: **Table 3** Common request headers

   +---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
   | **Header**                            | **Description**                       | **Remarks**                           | **Example**                           |
   +=======================================+=======================================+=======================================+=======================================+
   | Content-Type                          | Type (or format) of the message body. | Mandatory                             | application/json                      |
   +---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
   | X-Auth-Token                          | Token authentication information,     | Mandatory if token authentication is  | -                                     |
   |                                       | which can be obtained by following    | used.                                 |                                       |
   |                                       | the procedure in `Token               |                                       |                                       |
   |                                       | Authentication <https://docs.otc.t-sy |                                       |                                       |
   |                                       | stems.com/en-us/api/apiug/apig-en-api |                                       |                                       |
   |                                       | -180328003.html>`__.                  |                                       |                                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
   | X-Sdk-Date                            | Time at which the request was sent.   | Mandatory if AK/SK authentication is  | 20151222T034042Z                      |
   |                                       |                                       | used.                                 |                                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
   | Authorization                         | Signature authentication information, | Mandatory if AK/SK authentication is  | -                                     |
   |                                       | which comes from the request          | used.                                 |                                       |
   |                                       | signature result.                     |                                       |                                       |
   +---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+

Request Body (Optional)
-----------------------

A request body conveys information other than the request header and is generally sent in a structured format (for example, JSON or XML) defined by the
**Content-type** field.

**Response Headers**

A response header consists of an HTTP status code and additional response header fields.

-  HTTP status code: A status code consists of three digits (2xx to 5xx). 2xx indicates a success response. 4xx and 5xx indicate an error response. The status
   code returned can also be defined by the service.

-  Optional header fields: For example, **Content-type** could be one of such fields. :ref:`Table 4 <apig-en-api-180328002__tb5107e70c1d545de8b97ed913f602b83>` 
   describes common response header fields.

.. _apig-en-api-180328002__tb5107e70c1d545de8b97ed913f602b83:

.. table:: **Table 4** Response headers

   +----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
   | **Header**                                         | **Description**                                    | **Example**                                        |
   +====================================================+====================================================+====================================================+
   | Date                                               | A standard HTTP header, which indicates the date   | Mon, 12 Nov 2007 15:55:01 GMT                      |
   |                                                    | and time when a message is sent. The format of     |                                                    |
   |                                                    | this header field is defined in RFC 822.           |                                                    |
   +----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
   | Server                                             | A standard HTTP header, which contains the         | Apache                                             |
   |                                                    | information about the software that the server     |                                                    |
   |                                                    | uses to process requests.                          |                                                    |
   +----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
   | Content-Length                                     | A standard HTTP header, which indicates the size   | xxx                                                |
   |                                                    | of the response body, in decimal number of bytes.  |                                                    |
   +----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
   | Content-Type                                       | A standard HTTP header, which specifies the media  | application/json                                   |
   |                                                    | type of the response body sent to the recipient.   |                                                    |
   +----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

Response Body (Optional)
------------------------

A response body conveys information other than the response header and is generally sent in a structured format (for example, JSON or XML) defined by the
**Content-type** field.

**Initiating Requests**

A request can be initiated by using any of the following methods:

-  cURL

..

   cURL is a command line tool used to perform URL operations and transmit information. It serves as an HTTP client to send HTTP requests to the server and
   receive response messages. cURL is suitable for use in API tuning scenarios. For more information about cURL, visit https://curl.haxx.se/.

-  Code

..

   You can call APIs through code to assemble, send, and process requests.

-  REST client

..

   Mozilla Firefox and Google Chrome provide a graphical browser plug-in for REST clients to send and process requests. For Mozilla Firefox, see `Firefox
   RESTClient <https://addons.mozilla.org/en-US/firefox/addon/restclient/>`__. For Google Chrome, see
   `Postman <https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop>`__.
