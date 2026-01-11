# Content Filter

Proxyman offers the Primary and Secondary Filters to quickly filter out the Requests or Responses you're looking for.

{% hint style="info" %}
**⌘F: Open** Filter Bar quickly

**ESC** to close the Filter Bar
{% endhint %}

![Multiple Filters Selection (Hold CMD key and Click)](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MWPWuYgIo6i6gTJSUIl%2F-MWPX5yS4YA7CuixaXhZ%2F111282473-9e95ab00-8670-11eb-8d05-6e2c641a82bb.png?alt=media\&token=79d34d92-3eb8-4e52-b406-140085e30c93)

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MWPWuYgIo6i6gTJSUIl%2F-MWPYdeG67U8YQg8xfyU%2FScreen_Shot_2021-03-22_at_22_29_07.png?alt=media\&token=ebd757b9-16c6-4362-9c50-7825716bc1ee)

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MMIpB1h4e4aRQJKKSDY%2F-MMIpKKAFLhXu7K35zgZ%2FCleanShot%202020-11-17%20at%2008.31.48%402x.png?alt=media\&token=8aeb9103-cac0-42f0-b01d-062bb9f0b706)

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MMIpB1h4e4aRQJKKSDY%2F-MMIpSwCM9NRjZsf8y-r%2FCleanShot%202020-11-17%20at%2008.31.52%402x.png?alt=media\&token=57846212-6b13-4b14-bb05-480b4ad6b915)

### Primary Filter:&#x20;

| Filter    | Description                                       |
| --------- | ------------------------------------------------- |
| All       | All Requests and Responses                        |
| HTTP      | Only HTTP                                         |
| HTTPS     | Only HTTPS                                        |
| WebSocket | Only WebSocket and Secure WebSocket               |
| JSON      | Content-Type is application/json or JSON contents |
| XML       | Only XML                                          |
| Form      | Only Form Body in Request / Response              |
| JS        | Only JavaScript content                           |
| CSS       | Only CSS content                                  |
| Document  | Documents content: HTML, ...                      |
| Media     | Image contents: PNG, JPG, GIF, ...                |
| Other     | Other contents which no matching with the above.  |
| Font      | All font family                                   |
| GraphQL   | GraphQL Request (has suffix `/graphQL`)           |

### Status Filters:

| Filter | Description              |
| ------ | ------------------------ |
| 1xx    | Status Code from 100-200 |
| 2xx    | Status Code from 200-300 |
| 3xx    | Status Code from 300-400 |
| 4xx    | Status Code from 400-500 |
| 5xx    | Status Code from 500     |

{% hint style="info" %}
Hold CMD key and Click to select multiple Types
{% endhint %}

### Secondary Filter:

#### Content:

* URL
* Query String
* Request Header
* Response Header
* Method
* Status Code
* Comment
* Color

#### Matching:

* Contains
* Not Contains
* Start With
* End With
* Equal
* Not Equal
* Regex

### Header, Query, Auth, Form Filter

From Proxyman 2.34.0+, we can quickly filter the Header, Query, Auth, Form from the selected Request and Response.

1. Click on the view (e.g. Header of the Request)
2. Use Hotkey: CMD + F or Right-Click -> Show Filter to open the filter

![Filter Header, Query, Auth Form content](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FGPUIjUQipzWKwvRAl8bq%2FScreen_Shot_2021-10-14_at_22_59_20.png?alt=media\&token=05a7c277-e8b5-4a76-8a1f-eaeb5f1de1a2)
