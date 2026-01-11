# No Caching

### 1. What's it?

Prevent the server or client from caching your Request or Response, and you always get the latest change from the server.&#x20;

No Caching tools will affect all HTTP Request and Response, which enabled SSL Proxying.

### 2. What's for?

* If you would like to **see the latest HTTP Response changes** from the Server or Client and ignore all caching layers

### 3. How it works

No Caching tool will manipulate all requests by adding or removing caching HTTP Headers, which are described in the following table.

| HTTP Message | Remove                                       | Add                                                  |
| ------------ | -------------------------------------------- | ---------------------------------------------------- |
| Request      | **If-Modified-Since** and **If-None-Match**  | **Pragma: no-cache** and **Cache-control: no-cache** |
| Response     | **Expires**, **Last-Modified,** and **ETag** | **Expires: 0** and **Cache-Control: no-cache**       |

### 4. How to use

* Enable in **Tool Menu -> No Caching**&#x20;

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-M5kUoPHDivENZr4LN56%2F-M5kVwl9fEys53qNNwEW%2FScreen%20Shot%202020-04-25%20at%2015.45.37.png?alt=media\&token=30790a7b-e5de-48f2-a361-ea7c272b44f6)

![No Caching Status on the bottom right of Proxyman app](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-M5kUoPHDivENZr4LN56%2F-M5kWUcDLjQdfVToZaRN%2FScreen%20Shot%202020-04-25%20at%2015.48.05.png?alt=media\&token=720528e0-e89c-4413-aae2-0d89c8cb26aa)

{% hint style="info" %}
**⌥⌘N:** Toggl the No Caching Tool.
{% endhint %}
