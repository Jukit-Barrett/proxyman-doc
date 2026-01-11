# iOS Simulator

In order to capture the HTTP/HTTPS message from your iOS Simulator devices, please navigate to:

* **Certificate** **Menu** -> **Install Certificate on iOS -> Simulators**

## 1. iOS Simulator Setup Guide

![Automatically install the Certificate to iOS Simulators](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FOTHyl34jcJKoxLlftmAv%2FScreen%20Shot%202022-07-11%20at%2008.15.26.png?alt=media\&token=6c20e89e-e37c-4bc0-a115-bf12ca60c25b)

{% hint style="info" %}
It works for iOS, iPadOS, tvOS and watchOS.
{% endhint %}

The following photo describes three steps:

1. Install **Root Proxyman Certificate** on your machine: You can follow the [macOS Guide](https://docs.proxyman.com/debug-devices/macos).
2. Install Proxyman Certificate to all available simulators, which you have opened at least one time.
3. **Reset the Simulator**: Proxyman tries to reset all simulators, so it will load the new Certificate.

{% hint style="info" %}
From Proxyman 2.19.0+, Proxyman uses the [simctl](https://nshipster.com/simctl/) command line to perform tasks.&#x20;

**simctl** is built-in on your installed Xcode, which is more modern and reliable than the legacy approach (Use Python custom scripts).
{% endhint %}

{% hint style="info" %}
This step only installs on Simulators, which you have open at least one time

For instance, if you would like to debug on iPhone X Simulator, please make sure to **open** the iPhone X Simulator first, then **install** the Certificate in Step 2&#x20;
{% endhint %}

### Xcode Preview (SwiftUI)

If you're using Xcode Preview for SwiftUI, you can install the certificate into the Xcode Preview Simulator by following:

1. Open Xcode with Previewer Mode (SwiftUI).
2. Open Proxyman -> Certificate Menu -> Install for iOS -> Simulator
3. Click on the Advanced button -> Install for Xcode Preview

You can read more at: <https://github.com/ProxymanApp/Proxyman/issues/1568#issue-1610877870>

### Manually Install

In Proxyman v4.16.0 or later, you can manually install the certificate to your iOS Simulator in case the Automatic Solution doesn't work.

1. Certificate Menu -> Install Certificates for iOS -> Simulators
2. In Step 2, click on the ↓ button (Next to the Prepare Simulators button) -> Install Manually…

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FwyIzDnapd10ppD45YJEj%2FScreenshot%202024-11-01%20at%2020.14.39.jpg?alt=media&#x26;token=2de174a8-18aa-4c4a-9af6-042b997ac05f" alt=""><figcaption><p>Install certificate manually</p></figcaption></figure>

3. Drag and drop the certificate to your iOS Simulator

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FLG9nNR54513dcoCfEK4k%2FScreenshot%202024-01-07%20at%2014.43.13.png?alt=media&#x26;token=28aee8d4-f520-42c2-9943-12c9609758eb" alt="" width="563"><figcaption><p>Manually Install the certificate</p></figcaption></figure>

4. Open your iOS Simulator -> Setting app -> General -> About -> Certificate Trust Setting -> Find Proxyman CA Certificate and switch it ON
5. Done

## 2. Troubleshooting

### 1. Unable to install the Certificate

If you get errors when clicking on Step 2, please open Xcode -> Preferences -> Location tabs -> Select your Xcode in the Command Line Tools.

![Make sure you have the Xcode Command Line](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2Fur9sOsIVGGJmQiPFslqK%2FScreen_Shot_2022-07-11_at_08_12_33.png?alt=media\&token=c42927bd-bc3f-4518-b03f-6751ae4943ee)

### 2. Get SSL Error from HTTPS Response

* Opening the Setting app -> General -> About -> Certificate Trust Settings and verifying that Proxyman Certificate is installed and trusted.

![Proxyman Certificate is installed and trusted properly](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MV039NT2Fefr24GMsvz%2F-MV04a_0MtTevA03M6fq%2FScreen%20Shot%202021-03-05%20at%2013.32.25.png?alt=media\&token=35fc01cc-2a36-425f-aa80-e83b8ce9fea2)

If it's not installed:

* Open the iOS Simulator Setup (Certificate Menu -> Install Certificate on iOS -> Simulator) and click on the 2nd button.
* Or Try the following step to manually install the Certificate.

### 3. Some HTTP/HTTPS Requests are missing from Proxyman

Alamofire or URLSession might use the cached response for your request. As a result, the actual request doesn't hit the server. Thus, Proxyman could not capture and display it on the app.

Solution:&#x20;

* Disable the cache mechanism on URLSession or Alamofre.
* Use the [No Caching Tool](https://docs.proxyman.com/advanced-features/no-caching) (⌥⌘N)

## Manually Install the Certificate by exporting the certificate

If you cannot install the certificate, you can **manually** do it:

1. Open Proxyman -> Certificate Menu -> Export -> Root Certificate as DER -> Save to Desktop Folder
2. Open the Simulator **drag the certificate and drop it** on the Simulator screen
3. Open Setting app (on the Simulator) -> General -> Device Management -> Select the Certificate -> Install
4. Setting app -> General -> About -> Certificate Trust Settings and verifying that Proxyman Certificate is installed and trusted.
5. Done ✅

### Tutorial

See detailed steps to [debug an application on iOS Simulator ](https://proxyman.io/blog/2019/07/Debugging-on-iOS-Simulator-with-Proxyman.html)with Proxyman
