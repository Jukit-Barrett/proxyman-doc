# I couldn't see any traffics on Proxyman

### 1. Problems

* After launching the app, the request list is empty
* There are no requests captured by Proxyman?
* I don't see any requests on the app
* I can see some request on my Mac, but no request on my remote devices (iOS, Android)

{% hint style="info" %}
For remote devices (iOS or Android), please check out this [troubleshoot](https://docs.proxyman.com/troubleshooting/my-ios-devices-couldnt-connect-to-proxyman-via-proxy).
{% endhint %}

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-M5oNQOA8eEMdsDo1W4b%2F-M5oNlGIE51483XhMSa4%2FScreen_Shot_2020-04-26_at_09_48_10.png?alt=media\&token=b8e3b7fc-181f-4b03-8d5e-6f2e33f14d7d)

### 2. Solution

### 2.1 Turn OFF all VPN apps on your Mac machine

Some VPN apps accidentally revert the HTTP Proxy in Network as soon as Proxyman overrides it. As a result, HTTP Traffic won't go through Proxyman port at 9090.

Close all VPN app if possible and relaunch Proxyman

### 2.2. Double-check HTTP Proxy in Network

Proxyman would override or revert the HTTP Proxy at the launch time or exit, but some apps could revert back.

Let open System Preference -> Network -> Wifi -> Proxies tab:

* Check the **Web Proxy (HTTP)** and **Secure Web Proxy (HTTPS)**
* Make sure the port is the same as the Proxyman port
* IP is **127.0.0.1**

Save and check the requests on Proxyman

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-M5oNQOA8eEMdsDo1W4b%2F-M5oPPHJI6eMwhUjoubn%2FScreen%20Shot%202020-04-26%20at%2009.54.53.png?alt=media\&token=83d8e206-5bfb-442e-a871-b2fea33fca35)

### 2.3 Install Proxyman Helper Tool

By default, Proxyman attempts to override the system HTTP Proxy by using `networksetup` CLI, but it might be failed in certain scenarios.

\=> Let's try to install Proxyman Helper Tool. This tool will override the system HTTP Proxy properly. Please open Proxyman Preference -> Advanced Tab -> Install Helper Tool

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MJPOMkRPevh8tQznx08%2F-MJPPWnJw44Jz-e57Mqi%2FScreen_Shot_2020-10-12_at_08_24_05.png?alt=media\&token=31598950-209a-414d-b018-ae6a20a133d7)

### 2.4 Some HTTP/HTTPS Requests are missing from Proxyman

Alamofire or URLSession might use the cached response for your request. As a result, the actual request doesn't hit the server. Thus, Proxyman could not capture and display it on the app.

Solution:&#x20;

* Disable the cache mechanism on URLSession or Alamofre.
* Use the [No Caching Tool](https://docs.proxyman.com/advanced-features/no-caching) (⌥⌘N)
