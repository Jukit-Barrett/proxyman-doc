# Diff

### 1. What's it?

During using Proxyman, you might face the situation to find the difference between requests and responses. The Diff tool would help you to:

* Diff two Requests or Response, include the URL, Method, Status Code, Headers, and the Text-based body.
* Render as Side-by-Side or Unified.
* Light and Dark Theme.
* Export as a unified file.
* Open the diff by 3rd-party applications, such as FileMerge.
* Highlight and add comments.

{% hint style="info" %}
This feature is only available for macOS 11.2 and later.
{% endhint %}

### 2. How to use it?

1. Select your requests on the main table view.
2. Right-Click -> Tools -> Add to Diff pool (Or using ⌘Y)
3. On the Diff window, select Left and Right Panel.
4. Proxyman performs the diff operation and displays it.

#### Side-by-Side mode

![Side By Side Mode](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2F8EScHubheb71QvKA8L0A%2FScreen%20Shot%202022-03-27%20at%2009.30.03.png?alt=media\&token=e824bef6-f357-46c6-986e-a874f5f16e76)

#### Unified Mode

![Unified Mode](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2Fnnud51Dmklg6gNuUYFY5%2FScreen%20Shot%202022-03-27%20at%2009.31.53.png?alt=media\&token=d85f3fd1-1517-4fb6-8097-d00fcdf8d08c)

### 3. Open with 3rd-party diff tools

* File Merge: Required Xcode to install
* Kaleidoscope: You have to install the `ksdiff` in the Kaleidoscope's preference.
