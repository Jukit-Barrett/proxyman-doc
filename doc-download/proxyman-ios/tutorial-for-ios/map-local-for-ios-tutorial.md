# Map Local for iOS Tutorial

## M**anipulate HTTP(s) response on iPhone using Proxyman Map Local Tool**

Since version 2.0.0, Proxyman has introduced Map Local Tool which enables developers to use the content of local files as a response to your requests, as they match with your rules.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2F6ZkLy5DOt15zfy8h9Rzf%2Fimage.png?alt=media&#x26;token=d07770db-26f5-4cb4-bfdc-a75947157a81" alt=""><figcaption></figcaption></figure>

Map Local Tool could significantly boost your speed development and provide the capability to rapidly test on several edge-cased without explicitly updating the data in your server. It’s also the must-have tool for QAs or Developers if you would like to test the app’s behavior with various responses. Some of the testing scenarios:

* Define a Response and use it as a Response for matched Requests
* Quickly try new parameters in responses.
* Test the app’s behaviors with different parameters in the responses.
* Test the UI layout with unusual content.
* Quickly reproduce the bug with specific parameters in responses.
* Mock Fake API with a local File: It's useful for developers would try out the testing APIs which are not in production.

## Prerequisites

* Already downloaded the latest version of Proxyman on AppStore: <https://apps.apple.com/us/app/proxyman/id1551292695>
* Already installed and trusted Proxyman Certificate on iOS device (If you’re new to Proxyman, please follow [this tutorial](https://proxyman.io/posts/2021-10-17-Getting-Started-With-Proxyman-For-iOS) on how to start intercepting HTTP traffic on your iPhone).

## Create Map Local Rules

There are 2 ways that we can define a Breakpoint rule:

1. From Setting screen

* Go to Setting → map Local → Tap on + button.
* From here we will need to manually fill in all required fields for the Rule, including Title, Method, Matching URL, and include Subpaths or not.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FqBB6jjw5emTe4sQ5BYXT%2Fimage.png?alt=media&#x26;token=34ae2ba7-78a7-4aa5-962e-8f3f29f24aa5" alt=""><figcaption></figcaption></figure>

2. From the Menu context

* Long tap on the Request → Add to Map Local List.
* It will automatically fill in all fields to define the Rule based on the selected Request.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FP4m6fwmDFFajCiM7XFor%2Fimage.png?alt=media&#x26;token=778aced2-f42f-4733-af3f-bbff9d6e0b40" alt=""><figcaption></figcaption></figure>

#### Modify Header, Status Code and Body

From the Map Local Editor screen, we can freely manipulate the Headers, Status Code and Body data. If we alternate the Body with the new data type, Proxyman will auto-detect the Content-Type and update Headers for us.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FKpKjXE8Lb8rKElzA1VbI%2Fimage.png?alt=media&#x26;token=da5cfafe-853b-47f0-bdfb-220ca74a7946" alt=""><figcaption></figcaption></figure>

## Manipulate Response with Map Local Tool

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FUOsK4RcZW2hkNf12zj39%2Fimage.png?alt=media&#x26;token=59fc799c-5ea7-4ac8-b811-fc0c8be49096" alt=""><figcaption></figcaption></figure>

And you’re all set, it’s time to make another request to see how it works.

If the URL of incoming requests are matching with the **pre-defined matching Rule**, and the Local file is valid => The body response of those matching requests is automatically replaced with the content of the local file.

If the requests are not matching any rules, the entire Response's content remains on the server.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FEc0h4lMACaiTWXE5nfc4%2Fimage.png?alt=media&#x26;token=bf9e5161-be5a-4438-a184-6018415bab7e" alt=""><figcaption></figcaption></figure>

Nicely done! If you look into the flow list, you will find a small blue icon to indicate that this flow has been modified. As you can see, both the Response content has been updated with the local file.

## What’s next

Map Local tool allows you to try various types of responses to test the layout or content from your devices, thus boosting your debugging productivity, but limited by the capability of modifying Response content only. If you'd like to modify the Request content, you might want to check out our [Breakpoint tutorial](https://docs.proxyman.io/proxyman-ios/tutorial-for-ios/breakpoint-for-ios-tutorial) that enables us to manipulate both the Request and Response on the fly without changing any logic from your client.
