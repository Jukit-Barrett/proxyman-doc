# iOS Device

To capture HTTP/HTTPS messages in iOS devices (iPhone, iPad), please navigate to:

* **Certificate** **Menu** -> **Install Certificate on iOS -> Physical Devices...**

{% hint style="success" %}
This setup guide works with all real physical devices, including iPhone, iPad, Apple Watch, Apple TV, and Vision PRO.
{% endhint %}

## iOS Setup Guide

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FrabpvrtnJJK5GGEEtiqu%2FScreenshot%202025-10-28%20at%2021.29.31.png?alt=media&#x26;token=6205aab8-0de0-43fa-905f-cdb6272a9355" alt="Install certificate to iPhone Setup Guide"><figcaption></figcaption></figure>

Let's follow the guidelines:

1. Install **Root Proxyman Certificate** on your machine: You can follow the [macOS Guide](https://docs.proxyman.com/debug-devices/macos).
2. Get your iOS Device -> Open Settings app -> Wifi -> Select the current Wifi -> Configure the HTTP Proxy by following the next tables.

| Name           | Value                                             |
| -------------- | ------------------------------------------------- |
| Server IP      | Your current IP Network                           |
| Port           | The current port of Proxyman: 9090 is the default |
| Authentication | No                                                |

{% hint style="info" %}
If you're using any **VPN apps** on macOS or iOS devices, please ensure that you close all VPN apps, as they conflict with the HTTPS Proxy configuration.
{% endhint %}

&#x20; 3\. Open <http://proxy.man/ssl> or [http://cert.proxyman.io](http://cert.proxyman.io/) in **Safari Web Browser with Private Tab** from your iOS device to install the Proxyman Certificate.

{% hint style="info" %}
**<http://proxy.man/ssl>** or **<http://cert.proxyman.io>** is a local website, which is served from the local Proxyman's HTTP server. If you can't open it, please forget the wifi, reconnect, and make sure the Proxyman app is opening.

If you can't access it. Please open the support ticket at [Github's repo](https://github.com/ProxymanApp/Proxyman).
{% endhint %}

&#x20;   4\. From iOS 10.3, we have to explicitly install & trust the Proxyman CA in the Settings app

#### **Install Proxyman CA**

* **iOS ≥ 12.2**: On your iPhone -> Open Settings app > Profiles Downloaded > Select Proxyman CA > Install

#### Trust Proxyman CA

* Setting app > General > About > Certificate Trust Settings > Switch ON on Proxyman CA.

![Install and Trust Proxyman Certificate](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-LmSbviLZSr1v9NT_Rcz%2F-LmSeU4alrXa9cAA3od-%2Finstall_and_trust_proxyman_certificate.png?alt=media\&token=f4278b1a-79b7-40cc-8eea-f07def334adf)

{% hint style="info" %}
Please make sure we **install** and **trust** the Proxyman CA on your iOS Device. If you have any problem, shoot us an email at **<support@proxyman.io>** or bump it to [**Github**](https://github.com/ProxymanApp/Proxyman)
{% endhint %}

{% hint style="info" %}
If you cannot see any traffic from your iOS Devices, please check out this [troubleshooting](https://docs.proxyman.com/troubleshooting/my-ios-devices-couldnt-connect-to-proxyman-via-proxy)
{% endhint %}

{% hint style="info" %}
Make sure that you **delete the certificate on your iPhone** when you're not debugging by Proxyman. If not, your HTTP/HTTPS requests can be intercepted and leak your sensitive data.
{% endhint %}

## Tutorial

See detailed steps on how to [debug an application on iOS device](https://proxyman.io/blog/2019/06/How-I-use-Proxyman-to-see-HTTP-requests-responses-on-my-iPhone.html) with Proxyman.

### Tired of manual config?

We understand that manually overriding the HTTP Proxy and installing and trusting Proxyman Certificates is painful. Let's check out Atlantis, which is a native iOS framework that helps you do it automatically.

{% content-ref url="../atlantis/atlantis-for-ios" %}
[atlantis-for-ios](https://docs.proxyman.com/atlantis/atlantis-for-ios)
{% endcontent-ref %}

## Flutter app?

You might not be able to see the Network Traffic on Proxyman if your app is a Flutter app.

Flutter does not use a system-level proxy, so requests to Proxyman will not be displayed. To do this, you must manually configure your HTTP client used in the code to work with a proxy.

Please follow the solution "Getting Charles to work with Flutter" in <https://flutterigniter.com/debugging-network-requests/>

To find out your local IP, please go to Certificate Menu -> Install Certificate on iOS -> Physical device and get the Server IP and Port
