# Custom Previewer Tab

## 1. What's it?

You can customize the Custom Previewer Tabs, which always render one format at once time.

This handy tool might help you to fix the following issues:

* Format the BODY as **JSON**, but the Content-Type isn't `application/json`
* Format the body as **Protobuf**, but the Content-Type isn't `application/x-protobuf`
* Render HTML Page on the Web View
* **Beautify** the minified files (HTML, CSS, JS)
* Multipart/form-data
* Try to format the body as the selected type regardless of the `Content-Type`
* Convert MessagePack (msgpack) to JSON
* [Code Generator](https://docs.proxyman.com/advanced-features/code-generator) to Swift, Node, Javascript, cURL, ...
* GraphQL Query Prettier

<div data-full-width="false"><figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FQS5DmASN352ZCEhDybUH%2FScreenshot%202024-06-27%20at%2015.01.33.png?alt=media&#x26;token=b852b3ea-d443-41c7-98f7-7d43e2c29b1e" alt="" width="563"><figcaption><p>Select Custom Tabs for Request / Response Panel</p></figcaption></figure></div>

{% hint style="info" %}
The selected custom tabs will be appended to the right side of the Request or Response view&#x20;
{% endhint %}

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2F8Si69osmNYVI79U5igeE%2FCleanShot%202024-06-27%20at%2015.04.11%402x.jpg?alt=media&#x26;token=24b4d6d6-546f-4636-bec9-4236b3886131" alt=""><figcaption><p>Display Custom Tabs</p></figcaption></figure>

## 2. How to use it?

You can either access the Custom Previewer Window:

1. Click on the "+" button on the Request/Response bar or (from the Tools Menu -> Custom Previewer Tab...)
2. Click the checkbox to show/hide your custom Tab
3. The New Tab will appear on the Request or Response Panel ✅

### 2.1 Server-Sent Events and OpenAI Tabs

From Proxyman 5.22.0 or later, Proxyman supports

* Server-Sent Events from OpenAI endpoints: Auto prettify the inline JSON of the data event
* OpenAI Tab: Auto accumulate the content and show the final result, similar to the output of your chat view.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2Ff91nElaK93AiZfFIA9F5%2F1.jpg?alt=media&#x26;token=70d6c8e1-96a5-4845-9248-8a33197381b6" alt=""><figcaption><p>Capture OpenAI Endpoints</p></figcaption></figure>

## 3. ⚡️ Advance: Create a custom Tab with the Scripting Tool

* ✅ Show your own data on your tab
* It is useful if you want to decode your Body or display a partial body to your custom tab

### How to use:

1. the Click on the "+" button on the Request/Response bar or (from the Tools Menu -> Custom Previewer Tab...)
2. Select the \`Add Custom Tab\` button
3. Select the Request / Response panel and set a name for your tab

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2F5n0TQEJYkZsvnLWgAFAk%2FScreenshot%202024-06-27%20at%2015.01.51.png?alt=media&#x26;token=ab0a5dc7-09d7-4347-810d-c896df4ee25b" alt=""><figcaption></figcaption></figure>

4. Click on the "..." button to show the Javascript Code

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2F126T05MtmP31imNqEufD%2F343035426-24d2901d-10e3-4fa0-a472-579df7385358.jpg?alt=media&#x26;token=63eba6be-1927-4355-9c0b-8be2cf07b91b" alt=""><figcaption><p>Show the Javascript Code</p></figcaption></figure>

5. Tools -> Scripting -> Add new Rule -> Use this code to display your own data

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2F53QsgUDH9BoykmkyvvJB%2F343035431-1a336092-5c50-4e23-afbb-9a41f9679bb9.jpg?alt=media&#x26;token=456de21a-499a-44c8-99d5-2bd2245e7722" alt=""><figcaption><p>Write your code to display data</p></figcaption></figure>

6. Done

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FQluL2BFeo0yziUnxuWGC%2F343035436-dc7e6346-9ac6-4601-b07a-8294de2c4a02.jpg?alt=media&#x26;token=513c916e-4071-4881-b84c-672fa2ef6664" alt=""><figcaption><p>Display your data on a new tab</p></figcaption></figure>

## 4. Examples

#### Force render JSON TreeView

Proxyman supports JSON Tree View for better visualization

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MNNUVf__D4R6oOlrvwH%2F-MNNUbxHWsWRMr_boEpI%2FJSON.png?alt=media\&token=6708b360-f0b2-449d-9e5e-3baa95fdde44)

We can show/hide a certain column by Right-Click on the Column Header

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MNNUVf__D4R6oOlrvwH%2F-MNNUzgYXIXmb4RYSGpL%2FJSON_Col.png?alt=media\&token=ea0ef6f3-1e6c-4c11-bf2f-eb984ea18990)

#### Force render HTML Page

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MCAH07dTC9-sFn_jhCs%2F-MCAKf7af-qiy4s1Q-Eb%2FScreen_Shot_2020-07-14_at_10_19_51.png?alt=media\&token=db01c567-18aa-4db9-a3a7-123587a28bef)

#### Beautify the Javascript files

![Beautify JS Body](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MCAH07dTC9-sFn_jhCs%2F-MCAKqYypND8C0vo8X5N%2FScreen_Shot_2020-07-12_at_08_40_52.png?alt=media\&token=c931a177-5aab-478e-9d7b-2daf53ed8076)
