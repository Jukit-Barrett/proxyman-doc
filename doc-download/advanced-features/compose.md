# Compose new Request

## 1. What's it?

"Compose new Request" tool is a handy tool to help developers:

* Compose an HTTP/HTTPS Request and send it to your service. It's similar to Paw, Insomnia, and Postman.
* Quickly test your APIs without depending on your app client.
* Support Header, Query, URL, Form, JSON Body
* Support Raw Message
* Support multipart body
* Preset template: Empty Request, GET Request, Post Request with JSON or Form.

{% hint style="info" %}
You can reuse your request data for new requests. Please check out the [Edit & Repeat](https://docs.proxyman.com/advanced-features/edit-and-repeat) page.
{% endhint %}

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FKMaeS7lqansj0MX2Y8wK%2FScreenshot%202025-09-05%20at%2021.01.54.png?alt=media&#x26;token=c84e09d2-a3c7-46e1-b9d3-25566bad8a1c" alt=""><figcaption><p>Make a HTTPS Requests with Proxyman</p></figcaption></figure>

## 2. How to use

You can open the tool by either:

* Click on the Compose button on the main navigation bar
* Tools -> Compose

![Open the Compose Tool](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FIGNPhi6gMvEOZYunIvUA%2FScreen_Shot_2022-06-23_at_15_03_44.jpg?alt=media\&token=260f92a7-78d7-4790-a437-31f47a343937)

1. Enter the URL
2. Select HTTP Method
3. Modify the Header, Param, Body, Raw Message
4. Click the Send button.

![Compose JSON Body](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FiEGZEumelhi9RAkxfPAH%2FScreen_Shot_2022-06-23_at_15_07_35.jpg?alt=media\&token=ac87cc51-3849-4aff-9da5-64814d6ffc6c) ![Using Raw Message](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FvEQeGrMfgGXlcz8vpUIQ%2FScreen_Shot_2022-06-23_at_15_08_10.jpg?alt=media\&token=434a10dd-2b53-45ee-81e0-d1e69ebc513f)

## 3. Template

Proxyman also supports a few request templates.

* GET with Query
* Post with JSON
* Post with Form
* Post with multiparts
* Import from cURL

![Use preset template](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FwNaAyGBvUGZJ1YCA2Kcf%2FScreenshot%202025-02-01%20at%2010.45.59%E2%80%AFPM.jpg?alt=media\&token=ee860dd3-8095-40d7-92fc-2b282d9a1c77)

## 4. Import from cURL

You can import your cURL, which you can copy from a Network Tab in Google Chrome and make a request with the Compose Tool.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FbUYslRNNBCc6EtHDTHLZ%2FScreenshot%202025-02-01%20at%2010.42.21%E2%80%AFPM.jpg?alt=media&#x26;token=eadf666f-03e2-4957-8bc7-81fa3831da4d" alt=""><figcaption><p>import cURL</p></figcaption></figure>

{% hint style="success" %}
You can simply paste your cURL to the URL Text View, Proxyman will tries to parse your cURL
{% endhint %}

## 5. History Request

From Proxyman macOS 5.24.0, Proxyman will store your requests/responses in the History List.

* ✅ Useful to preview your previous Request/Response

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FNeDMfkGV3TDQoEwgOQp9%2FScreenshot%202025-08-25%20at%2014.02.04.jpg?alt=media&#x26;token=96cba38c-b30a-4380-a652-9d098c970e04" alt=""><figcaption><p>Request History in the Compose View</p></figcaption></figure>

## 6. Settings

* **SettingsRequest Timeout**: In Setting -> Tools Tab -> Request Timeout: Define a second that the Request will timeout. Use 0 to disable it. Available on Proxyman 4.13.0 or later
