# I could not see any requests from my localhost server

## 1. Problem

I develop a local NodeJS, Ruby, or Python Backend at **<http://localhost:3000>**, but when I visit **<http://localhost:3000>** from Google Chrome or Safari, there is no traffic on the Proxyman app.

**Why does this happen?** By default, on macOS, all localhost requests don't go through the System HTTP Proxy. Therefore, there is no traffic recorded by the Proxyman app.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FoMIYOFiGojtc8gDuKPhQ%2Fcapture_http_localhost_chrome_2.jpeg?alt=media&#x26;token=20ccba33-5a02-412d-b50d-0683ae1865bb" alt="Proxyman can not capture any http localhost traffic"><figcaption></figcaption></figure>

## 2. Solution

### 2.1 ✅ New Solution for v6.3.0

From Proxyman macOS v6.3.0, Proxyman can:

* Capture `http://locahost:3000` or any localhost traffic in Google Chrome / Firefox without modifying the /etc/host file
* Works with a single click
* Tutorial: <https://proxyman.com/posts/how-to-capture-http-localhost-traffic-from-google-chrome>

### How to do it

1. In Proxyman app -> Go to the Setup Menu -> Automatic Setup -> Click on the "Google Chrome" button
2. New Google Chrome will appear
3. Done. Visit <http://localhost:3000> and Proxyman can capture it

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2F202Ww1pkI0lKkmSwkzgh%2Fcapture_http_localhost_chrome_1.jpeg?alt=media&#x26;token=ab79aa40-2b97-401d-8475-a30467d93fea" alt="capture HTTPS traffic from Google Chrome with Proxyman"><figcaption></figcaption></figure>

## 2.2 Old solution

There are two solutions to fix it: You should follow either one of the following solutions.

### Solution 1: Map **localhost** to the domain name in `/etc/hosts`&#x20;

1. Open `etc/hosts` file with Vim or VS Code.

```
$ sudo vim /etc/hosts
```

2\. Add Domain Name with both **IPv4** and **IPv6** (You can change the `proxyman.debug` with your name)

```
127.0.0.1 proxyman.debug
::1 proxyman.debug
```

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FYl0L3IBWwwG0MXIHxK6i%2FScreenshot%202023-09-01%20at%2022.11.30.png?alt=media&#x26;token=a6c5c1ae-0cc7-42fc-9f05-49c090f4fbb4" alt=""><figcaption><p>Add proxyman.debug in /etc/host</p></figcaption></figure>

3\. Save the file with `sudo` permission

4\. Access your localhost server by **<http://proxyman.debug:3000>** (replace 3000 with your localhost ports)&#x20;

6\. Enjoy debugging!

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-M5khYgr9Ma-4XAPDv1_%2F-M5kkqMh_FCLKY6nHCUw%2FScreen%20Shot%202020-04-25%20at%2016.55.18.png?alt=media\&token=4ccc7500-8491-421b-be95-a4e74c10059d)

{% hint style="info" %}
If you use a `local` as a suffix, e.g. proxyman.local, make sure to remove the \`\*.local\` from the Bypass Proxy List ([Instruction](https://docs.proxyman.io/troubleshooting/.local-doesnt-appear-in-proxyman#2-solution)).
{% endhint %}

### Solution 2: Use **localhost.proxyman.io** instead of **localhost**

Proxyman uses Cloudflare and sets the DNS of **localhost.proxyman.io** to 127.0.0.1 (localhost). As a result, Proxyman can capture the local traffic as usual ✅&#x20;

For example:

<table data-header-hidden><thead><tr><th width="374">Old URL</th><th>New URL</th></tr></thead><tbody><tr><td>Old URL</td><td>New URL</td></tr><tr><td>localhost:3000</td><td>localhost.proxyman.io:3000</td></tr><tr><td>localhost:8080</td><td>localhost.proxyman.io:8080</td></tr><tr><td>...</td><td>...</td></tr></tbody></table>
