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

![Side By Side Mode](images/Screen_Shot_2022-03-27_at_09.30.03_a25d9ed6.png)

#### Unified Mode

![Unified Mode](images/Screen_Shot_2022-03-27_at_09.31.53_63460157.png)

### 3. Open with 3rd-party diff tools

* File Merge: Required Xcode to install
* Kaleidoscope: You have to install the `ksdiff` in the Kaleidoscope's preference.
