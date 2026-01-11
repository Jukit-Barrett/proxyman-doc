# Breakpoint for iOS Tutorial

## M**odify HTTP(s) Request & Response on your iPhone with Proxyman Breakpoint Tool**

Since version 2.0.0, Proxyman has introduced a new feature that enables developers to manipulate the Request & Response data on the fly without changing any logic from your client.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FBIZoWcR4stO85CRcpmxs%2F1.png?alt=media&#x26;token=6c91591e-bb3b-4c14-88cc-2dbd9ec5861b" alt=""><figcaption></figcaption></figure>

This mini tutorial demonstrates how we can modify HTTP(s) Requests/Responses on iOS devices with Proxyman Breakpoint Tool, for example:

* Modify the Request URL (including the Scheme, Host, Path, Port) and HTTP Method
* Modify HTTP Headers of Request/Response
* Modify Query from Requests
* Modify HTTP Body of Request/Response
* Modify Response HTTP Status Code

## Prerequisites

* Already downloaded the latest version of Proxyman on AppStore: <https://apps.apple.com/us/app/proxyman/id1551292695>
* Already installed and trusted Proxyman Certificate on iOS device (If you’re new to Proxyman, please follow [this tutorial](https://proxyman.io/posts/2021-10-17-Getting-Started-With-Proxyman-For-iOS) on how to start intercepting HTTP traffic on your iPhone).

## Create Breakpoint Rules

There are 3 ways that we can define a Breakpoint rule:

1. From Setting screen

* Go to Setting → Breakpoint → Tap on the + button.
* From here we will need to manually fill in all required fields for the Rule, including Title, Method, Matching URL, and include Subpaths or not.
* We are also able to select if this rule is applied for upcoming Requests, Responses or both.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2F5S4NyNWNB3xFvEJc08zr%2Fimage.png?alt=media&#x26;token=d4210feb-66b7-45ce-84c4-f05003d088f5" alt=""><figcaption></figcaption></figure>

2. From "Waiting Breakpoint" screen

* Tap on Waiting Breakpoint icon → Create Breakpoint Rule.
* Then we will need to manually create the Rule (similar to the previous option).

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FxlSs0vWcERciw078gyrF%2Fimage.png?alt=media&#x26;token=ee2968a9-c897-4304-9b21-6a7fb4473266" alt=""><figcaption></figcaption></figure>

3. From the Menu context

* Long tap on the Request → Add to Breakpoint List.
* It will automatically fill in all fields to define the Rule based on the selected Request.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FQNBr7U0CDx115BSJ2zs6%2Fimage.png?alt=media&#x26;token=c435835e-625d-4002-8dfa-d6006b032af8" alt=""><figcaption></figcaption></figure>

In this example, the Breakpoint Rule will apply to both upcoming Requests/ Responses. Let’s make a Request to see how it works.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FEpsjclwDCDZQ7hjGg6Q0%2Fimage.png?alt=media&#x26;token=33dbcbe4-98a7-487c-bd8e-957f662ede49" alt=""><figcaption></figcaption></figure>

## Modify HTTP(s) Requests

Once we make a Request with the matching URL, Proxyman will stop it and notify us that there are waiting breakpoints. From the Home screen, we can tap the small icon to see the waiting Breakpoint list and select a Breakpoint to start modifying the Request Content.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FJJC63T0lDdXd092MbXPw%2Fimage.png?alt=media&#x26;token=8b68af10-38b6-4e84-93f6-b7d2656d0bba" alt=""><figcaption></figcaption></figure>

#### Modify URL + Method

We can freely manipulate the HTTP Method, URL, and Query,. The URL will be auto-updated as the queries change and vice versa.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2F9mVthwRmJf5DWqU1l756%2Fimage.png?alt=media&#x26;token=d9ba8a2f-9156-4ede-a6b0-e40916a9893a" alt=""><figcaption></figcaption></figure>

#### Modify Body

If we alternate the Body with a new data type, Proxyman will auto-detect the Content-Type and update Headers for us.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2F7GfNV7zNrQfhmjn7DwRo%2Fimage.png?alt=media&#x26;token=80159dd2-ac02-4759-aa84-7b1ff5511858" alt=""><figcaption></figcaption></figure>

## Execute, abort, continue Breakpoint

When you're happy with the change, you can execute the Request/ Response by selecting the option from the top right menu. To keep the original Request, you can use the Continue button or cancel it with the Abort option.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FEvLV3vQCd1maOUfvAXXZ%2Fimage.png?alt=media&#x26;token=64c6a7c9-0237-4b82-8357-4043ff119d29" alt=""><figcaption></figcaption></figure>

Since our Breakpoint rule is applied for both Request and Response, you will find the Response added to waiting breakpoints list once you hit the “Execute” button.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FfyYSzntonxkmLbpD7TFj%2Fimage.png?alt=media&#x26;token=92c65c2a-8be6-4d60-9d52-fcbedfb5fa16" alt=""><figcaption></figcaption></figure>

Now you can change the HTTP Status Code, update Headers or alternate the Body with new content for Response (similar to modifying Request Breakpoint)

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2F6HJlMZouZ9Rf4Biq7XOK%2Fimage.png?alt=media&#x26;token=61f4963f-e9a2-415b-bfc4-090e9574acd4" alt=""><figcaption></figcaption></figure>

Nicely done! If you look into the flow list, you will find a small blue icon to indicate that this flow has been modified.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FAuspFYIailtEHGC27hVe%2Fimage.png?alt=media&#x26;token=a35c9593-caa4-44b5-8d11-b9da9beec27c" alt=""><figcaption></figcaption></figure>

As you can see, both the Request and Response content has been updated as expected.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2Fcl0SHf0RIWtAuJnScERy%2Fimage.png?alt=media&#x26;token=cf18c528-9673-4802-8459-d667eece41ff" alt=""><figcaption></figcaption></figure>

**NOTES**:

* When you create a new rule, both Breakpoint Tool and Rule will be enabled by default (you can switch it ON/OFF as needed).
* Make sure to check the VPN status (1), the Breakpoint Tool status (2), and the Breakpoint Rule status (3) are all ENABLED so that the Breakpoint Tool can work.
* If the first rule matches the Requests/ Responses, other rules will not be applied.
* As you’re editing the Request, the Response tab will be disabled. As you’re editing the Response, the Request tab will be displayed in read-only mode.

## What’s next

Breakpoint allows you to modify the Request/Response on the fly, but it requires a lot of manual works. If you'd like to make it automated, you might check out our [Map Local tool](https://docs.proxyman.io/proxyman-ios/tutorial-for-ios/map-local-for-ios-tutorial) tutorial to automatically map a local file as a Response.
