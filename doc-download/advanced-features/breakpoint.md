# Breakpoint

### 1. What's it?

Breakpoint is a handy tool to help developers to edit the content of the Request and Response **on the fly**.

It's possible to set a breakpoint on both **Request** or **Response.**

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MEVxm7C1KsUVgql_NPM%2F-MEVyVnIP9VAXgkb-LUN%2FScreen%20Shot%202020-08-12%20at%2011.39.46.png?alt=media\&token=ff9f8d86-60e6-4130-a83a-2da8324842e8)

{% hint style="info" %}
If you're using [Atlantis Framework](https://docs.proxyman.com/atlantis/atlantis-for-ios), you could not use Breakpoint. Please consider using a normal proxy.
{% endhint %}

### 2. Main features

Breakpoint tool allows the developer to stop an ongoing Request or incoming Response to modify its data.

* Modify the Request URL, including the Scheme, Host, Path, Port, HTTP Method (Available on Proxyman 2.35.4+)
* Modify HTTP Headers of Request/Response
* Modify Query or Form entry from Requests.
* Modify Authorization/Cookie/Set-Cookie Headers.
* Modify HTTP Body  of Request/Response
* Change Response HTTP Status Code.

![Breakpoint on Response](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MhvV4r0O2ZZtJx7eDhO%2F-MhvVZiTBRRVnS8Z50yB%2FScreen%20Shot%202021-08-25%20at%2011.12.06.png?alt=media\&token=30144dc0-8a03-41a9-acf5-aa6fc49bd699)

![Breakpoint on the Request URL (Scheme, Host, Port, Path and Query)](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FibeqdjhWzlVYHcrfDIUt%2FScreen_Shot_2021-12-20_at_15_06_05.png?alt=media\&token=80446083-949b-4d70-ba48-6fa6ebccaccf)

#### Breakpoint Actions

| Action  | Meaning                                               |
| ------- | ----------------------------------------------------- |
| Cancel  | Cancel a breakpoint and continue the Request/Response |
| Abort   | Abort the connection and return 503 status code       |
| Execute | Make a request/response with a new change             |

{% hint style="info" %}
Check out Breakpoint Tutorial: [Breakpoint to intercept and edit the requests/response on iOS app](https://proxyman.io/blog/2019/09/Use-Breakpoint-to-intercept-and-edit-request-response-on-iOS-app.html)
{% endhint %}

### 3. Breakpoint with Raw Message

From build 3.1.0, we can modify the Request / Response by using the Raw Message.

\[WIP]

### 4. Breakpoint by the Scripting Tool ✅&#x20;

If you would like to do Breakpoint in an Automatic way, you should use the [Scripting](https://docs.proxyman.com/scripting/script#1-whats-it) tools, which you can achieve the same result that Breakpoint can do, but in a flexible way by writing Javascript Code.

Please check out this [Snippet Code](https://docs.proxyman.com/scripting/snippet-code#2-common-on-request-and-response) to understand how to use Scripting for Breakpoint.

### 5. Breakpoint with GraphQL Requests

From Proxyman 2.27.0+, Breakpoint can work with GraphQL Request by a specific QueryName. Please check out the following GraphQL Document.

{% content-ref url="graphql" %}
[graphql](https://docs.proxyman.com/advanced-features/graphql)
{% endcontent-ref %}

### 6. How to use

You can simply create a Breakpoint rule by:

1. Right-Click on the Request -> Tools -> Breakpoint
2. Proxyman will open a Breakpoint Window and fill the Matching Rule.&#x20;
3. Select Breakpoint on Request or Response or both.
4. Click Add to create a rule.
5. Try sending a Request again -> Proxyman will open a Breakpoint and you can modify the data.
6. Click on the Execute Button to send a request/response.
