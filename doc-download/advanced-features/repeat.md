# Repeat

### 1. What's it?

Repeat tool is a useful tool for quickly making a new HTTP request with the same HTTP Header and Body for seeing the new response without changing from your browsers or clients.

### 2. What's it for?

* Quickly make an HTTP/HTTPS Request for testing the newest response from the server.
* It's useful for developers to test the change of the server without repeating the request manually.

{% hint style="info" %}
Repeat tool only supports HTTP/HTTPS Requests. Repeat on WS/WSS traffic might be failed.
{% endhint %}

{% hint style="info" %}
Repeated requests can be modified by the Breakpoint, Map Local, and Scripting tool if it matches any rules.
{% endhint %}

### 3. How to use

* Right-Click on a single or multiple Request(s) -> **Repeat**

![Quickly repeat the current requests](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FIqaM1b6s9R5KYortG3rV%2FScreen_Shot_2022-06-23_at_14_49_23.jpg?alt=media\&token=930e9a0a-5e71-47bd-809f-462072ea3755)

{% hint style="info" %}
⌘ ⏎ : Repeat the current selected request.
{% endhint %}

### &#x20;4. Settings

* **Request Timeout**: In Setting -> Tools Tab -> Request Timeout: Define a second that the Request will timeout. Use 0 to disable it. Available on Proxyman 4.13.0 or later
