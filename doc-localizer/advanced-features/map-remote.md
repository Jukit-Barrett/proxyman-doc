# Map Remote

## 1. What's it?

Map Remote (**⌘⌥R**) would help the developer to change the HTTP Request's location to a new destination server, per the configured rules, so the HTTP Response is transparently served from your client.

Map Remote also supports mapping from HTTP to HTTPS and vice-versa

![Map Remote Rules](images/Screen_Shot_2020-07-19_at_10.17.34_7449acb1.png)

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

![](images/Screen_Shot_2020-07-19_at_10.17.44_1ca66054.png)

{% hint style="info" %}

* Leave the Text Field blank to keep it unchanged from the matched request
* The wildcard is not allow
  {% endhint %}

### Debugging

To determine what Map Remote matches your URL, you can open The Request -> Summary Tab:

1. Select your request
2. Summary Tab -> Debugging Tools
3. Check the Map URL

<figure><img src="images/CleanShot_2023-02-15_at_09.23.58_2x_9e3ba336.jpg" alt=""><figcaption><p>How to debug the Map Remote</p></figcaption></figure>

### Preserve Host Header

By default, Proxyman attempts to override the Host Header to match with the new Host in Remote Map. It's crucial to successfully make a request.

If you would like to preserve the original Host Header, please check ON in the "Preserve Host Header" checkbox when creating a new entry. Proxyman will preserve the Host value.

## 6. How to use

* Right Click on selected Request -> Tools -> Map Remote: Proxyman will fill in the necessary data from the selected request

![Create a Map Remote](images/Screen_Shot_2020-04-25_at_16.18.59_f096341f.png)

## 7. Common Usages

### 7.1 Map Localhost (HTTP) to Production (HTTPS)

<figure><img src="images/Screenshot_2023-02-15_at_09.34.02_7971930f.png" alt=""><figcaption><p>Map Remote Config</p></figcaption></figure>

**Result:**

| Original URL                                           | To URL                                               |
| ------------------------------------------------------ | ---------------------------------------------------- |
| <http://localhost:3000>                                | <https://proxyman.io>                                |
| <http://localhost:3000/pricing>                        | <https://proxyman.io/pricing>                        |
| <http://localhost:3000/v1/user?id=123\\&name=proxyman> | <https://proxyman.io/v1/user?id=123\\&name=proxyman> |
| **POST** <http://localhost:3000/login>                 | **POST** <https://proxyman.io/login>                 |

### 7.2 Map Production (HTTPS) to localhost (HTTP)

<figure><img src="images/Screenshot_2023-02-15_at_09.39.50_eeb43a98.png" alt=""><figcaption><p>Map Remote Config</p></figcaption></figure>

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

<figure><img src="images/Screenshot_2023-02-15_at_09.29.05_dfab043a.png" alt=""><figcaption><p>Map Remote Config</p></figcaption></figure>

| Original URL                   | To URL                               |
| ------------------------------ | ------------------------------------ |
| ws\://localhost:4000           | wss\://ws.postman-echo.com           |
| ws\://localhost:4000/websocket | wss\://ws.postman-echo.com/websocket |

### 7.5 Map Websocket from Production to Localhost

<figure><img src="images/Screenshot_2023-02-15_at_09.38.19_8919a042.png" alt=""><figcaption><p>Map Remote Config</p></figcaption></figure>

| Original URL                         | to URL                         |
| ------------------------------------ | ------------------------------ |
| wss\://ws.postman-echo.com           | ws\://localhost:3000           |
| wss\://ws.postman-echo.com/websocket | ws\://localhost:3000/websocket |
