# Map Remote

## 1. What's it?

Map Remote (**⌘⌥R**) would help the developer to change the HTTP Request's location to a new destination server, per the configured rules, so the HTTP Response is transparently served from your client.

Map Remote also supports mapping from HTTP to HTTPS and vice-versa

![Map Remote Rules](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MC_ByEFfDEzSzI1C7Zz%2F-MC_DZnVSPfddI4tnDir%2FScreen%20Shot%202020-07-19%20at%2010.17.34.png?alt=media\&token=f468fd18-608d-4841-9c4b-fa47236b4f24)

{% hint style="info" %}
Check out common [Map Remote Config](#7.-common-usages) when mapping from HTTP <-> HTTPS.
{% endhint %}

{% hint style="info" %}
From Proxyman 4.3.0: Map Remote supports Websocket and Secure Websocket.
{% endhint %}

## 2. Benefits

* Use Production Endpoints on your Development website on certain endpoints without changing the source code
* Use Development Endpoints on your Production website
* Change certain request's URLs to different destinations
* Able to replace requests components, such as Protocol, Host, Port, Path, or Query on the fly

{% hint style="info" %}
To boost your productivity, you can use the [Scripting feature](https://docs.proxyman.com/scripting/script#1-whats-it) that allows you to achieve the same result as Map Remote by writing simple Javascript Code

For instance, [Snippet code to change Production to Localhost server](https://docs.proxyman.com/scripting/snippet-code#change-request-destination-schema-host-port-path)
{% endhint %}

## 3. Map Remote with GraphQL Requests

From Proxyman 2.27.0+, Map Remote can work with GraphQL Request by a specific QueryName. Please check out the following GraphQL Document.

{% content-ref url="graphql" %}
[graphql](https://docs.proxyman.com/advanced-features/graphql)
{% endcontent-ref %}

## 4. Using Scripting as Map Remote ✅

If you get difficult to set up a complicated Map Remote Rule, you might easily do it by using the [Scripting Tool](https://docs.proxyman.com/scripting/script#1-whats-it).

Please check out [Map Remote Snippet Code](https://docs.proxyman.com/scripting/snippet-code#8-map-remote-with-scripting) to learn how to use Scripting to achieve the same result as Map Remote.

For instance, it's straightforward to do the following by Scripting:

* Map v1 to v2 endpoints
* Map Production to Localhost
* Map Localhost to Production
* ...

## 5. Matching Rule

{% hint style="info" %}
Proxyman supports [Regular Expression](https://developer.apple.com/documentation/foundation/nsregularexpression#1965590) and Wildcard from the 2.3.0 version. [Check out here](https://docs.proxyman.com/basic-features/regex)
{% endhint %}

We can define matching rules by using [Wildcard or Regular Expression](https://docs.proxyman.com/basic-features/regex).

For matched requests, Proxyman attempts to:

* Replace Protocol, Host, Port, Path, and Query if it available
* If the component is empty, it won't change the matched request's component

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MC_ByEFfDEzSzI1C7Zz%2F-MC_GHgRHPy8AUEjilO4%2FScreen%20Shot%202020-07-19%20at%2010.17.44.png?alt=media\&token=c380ce78-9b3f-4ee8-be9e-6e6ee31d3e76)

{% hint style="info" %}

* Leave the Text Field blank to keep it unchanged from the matched request
* The wildcard is not allow
  {% endhint %}

### Debugging

To determine what Map Remote matches your URL, you can open The Request -> Summary Tab:

1. Select your request
2. Summary Tab -> Debugging Tools
3. Check the Map URL

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FTzEwgRO7nyDgIKosKmVt%2FCleanShot%202023-02-15%20at%2009.23.58%402x.jpg?alt=media&#x26;token=ebb58d8c-e24a-4871-8e07-aa86719a0407" alt=""><figcaption><p>How to debug the Map Remote</p></figcaption></figure>

### Preserve Host Header

By default, Proxyman attempts to override the Host Header to match with the new Host in Remote Map. It's crucial to successfully make a request.

If you would like to preserve the original Host Header, please check ON in the "Preserve Host Header" checkbox when creating a new entry. Proxyman will preserve the Host value.

## 6. How to use

* Right Click on selected Request -> Tools -> Map Remote: Proxyman will fill in the necessary data from the selected request

![Create a Map Remote](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-M5kcNLYKkRb4y_kT34H%2F-M5kcjUlp-pVHTWFPxse%2FScreen%20Shot%202020-04-25%20at%2016.18.59.png?alt=media\&token=a017a353-ca92-46f3-be11-5e93ff3b9300)

## 7. Common Usages

### 7.1 Map Localhost (HTTP) to Production (HTTPS)

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FR7NQOMFyCWhHRUfDeFF0%2FScreenshot%202023-02-15%20at%2009.34.02.png?alt=media&#x26;token=b1494d3a-6ac6-4f67-bee9-625a51ca2f33" alt=""><figcaption><p>Map Remote Config</p></figcaption></figure>

**Result:**

| Original URL                                           | To URL                                               |
| ------------------------------------------------------ | ---------------------------------------------------- |
| <http://localhost:3000>                                | <https://proxyman.io>                                |
| <http://localhost:3000/pricing>                        | <https://proxyman.io/pricing>                        |
| <http://localhost:3000/v1/user?id=123\\&name=proxyman> | <https://proxyman.io/v1/user?id=123\\&name=proxyman> |
| **POST** <http://localhost:3000/login>                 | **POST** <https://proxyman.io/login>                 |

### 7.2 Map Production (HTTPS) to localhost (HTTP)

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FlU5CIPBw57UrmzIKqG46%2FScreenshot%202023-02-15%20at%2009.39.50.png?alt=media&#x26;token=6f97c5ae-4b29-4a1a-b9b3-70b0e448c58f" alt=""><figcaption><p>Map Remote Config</p></figcaption></figure>

| Original URL                                         | To URL                                                 |
| ---------------------------------------------------- | ------------------------------------------------------ |
| <https://proxyman.io>                                | <http://localhost:3000>                                |
| <https://proxyman.io/v1/user?id=123\\&name=proxyman> | <http://localhost:3000/v1/user?id=123\\&name=proxyman> |
| **POST** <https://proxyman.io/login>                 | **POST** <http://localhost:3000/login>                 |

### 7.3 Map certain URL to another host

* Rule: **<https://proxyman.io/v1/user>** (for instance)
* Select **Any** and **Wildcard**
* **Un-Check Include all subpaths of this URL:** Un-check means it doesn't map other subpaths

**Map To:**

* Protocol: **https**
* Host: New Host (e.g staging.proxyman.io)
* Port: **443** (your local port)
* Leave Path and Query Empty

**Result:**

| Original URL                                         | To URL                                                       |
| ---------------------------------------------------- | ------------------------------------------------------------ |
| <https://proxyman.io>                                | <https://proxyman.io> (does not map the rule)                |
| <https://proxyman.io/v2/setting>                     | <https://proxyman.io/v2/setting> (does not map the rule)     |
| <https://proxyman.io/v1/user?id=123\\&name=proxyman> | <https://staging.proxyman.io/v1/user?id=123\\&name=proxyman> |

### 7.4 Map Websocket from localhost to Production

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FPykBG136twG3JAI6sD66%2FScreenshot%202023-02-15%20at%2009.29.05.png?alt=media&#x26;token=00035108-d6b0-462e-9e68-735b3cd6d023" alt=""><figcaption><p>Map Remote Config</p></figcaption></figure>

| Original URL                   | To URL                               |
| ------------------------------ | ------------------------------------ |
| ws\://localhost:4000           | wss\://ws.postman-echo.com           |
| ws\://localhost:4000/websocket | wss\://ws.postman-echo.com/websocket |

### 7.5 Map Websocket from Production to Localhost

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FNXK51fNuurLw5j3ob8qE%2FScreenshot%202023-02-15%20at%2009.38.19.png?alt=media&#x26;token=fd1dfa8a-477d-4369-b4a1-a6060b93ed71" alt=""><figcaption><p>Map Remote Config</p></figcaption></figure>

| Original URL                         | to URL                         |
| ------------------------------------ | ------------------------------ |
| wss\://ws.postman-echo.com           | ws\://localhost:3000           |
| wss\://ws.postman-echo.com/websocket | ws\://localhost:3000/websocket |
