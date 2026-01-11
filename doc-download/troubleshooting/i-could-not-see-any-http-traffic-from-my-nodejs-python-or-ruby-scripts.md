# I could not see any HTTP traffic from my NodeJS, Python, or Ruby scripts

## 1. Problem:

* I have NodeJS, Ruby, Python, or Golang scripts/servers, which make an internal HTTP/HTTPS request -> However, I don't see any traffic from the Proxyman app.

For example:&#x20;

* NodeJS: I'm using the [axios](https://github.com/axios/axios) library (NodeJS) to call a RESTFUL API from my production server (e.g. <https://mycompany.com/v1/data>). However, there is no traffic recorded from the Proxyman app.
* I'm using net/http from Golang, but no requests appear on Proxyman
* ... so all

## 2. New Automatic Solution (v4.7.0 or later) ✅

Proxyman v4.7.0 or later can capture HTTP/HTTPS traffic from Python/Ruby/NodeJS/Golang with 1-click.

* 1-click solution: No need to manually set HTTP Proxy config or trust the self-signed certificate.
* Support many network libraries from NodeJS, Python, Ruby, and Golang

### 2.1 How to use:

1. Open Proxyman -> Setup Menu -> Automatic Setup
2. Click on "Open New Terminal"

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2F4CIEVKhzglYi5T3YHVLT%2FScreenshot%202025-03-18%20at%2010.54.37.jpg?alt=media&#x26;token=295c1e9f-10ce-4766-ab65-e08d24f79858" alt=""><figcaption><p>Start pre-configured Terminal</p></figcaption></figure>

3. Accept the Apple Script permission prompt if needed
4. The New Terminal app is launched -> You can start your Python Backend Server, or Run scripts => Proxyman automatically captures all traffic.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FtsBq8JdHXuQU1vL31PYZ%2FCleanShot%202025-03-18%20at%2009.56.44%402x.jpg?alt=media&#x26;token=df25804a-c39b-4c87-9422-b52ab338b7a3" alt=""><figcaption><p>Capture HTTPS traffic from Ruby, Python, NodeJS and Golang Server/Scripts</p></figcaption></figure>

3. Done ✅

## 3. Other Problems

### 3.1 I could not see any `fetch()`request from NextJS - Server Side Component

* Solution on this blog: <https://proxyman.com/posts/2024-06-10-Capture-HTTPS-From-NextJS-Server-Components>
