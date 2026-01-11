# Request / Response Previewer

After installing the [Certificate](https://docs.proxyman.com/debug-devices/macos) and enable [HTTP Response](https://docs.proxyman.com/basic-features/ssl-proxying) on domains or clients, your network traffic would show up immediately inside the Proxyman window, separated into three main areas:

* The Source List on the left panel&#x20;
* The Flow List on the middle panel&#x20;
* The Flow Content on the right panel

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-M5k_8UnCbVU-a0Ksr1u%2F-M5kcU0AOTr014EyiUPT%2F01.png?alt=media\&token=9bce65ca-8c22-433e-902b-a309977ba9e2)

### Body Content Previewer

Depend on what the content of the Request or Response is: Proxyman will automatically show in separate tabs:

* **Header**: All headers (key-value table)
* **Cookies**: **Cookie** key in the header
* **Set-Cookie** for the Set-Cookie Header in the Response
* **Auth**: **Authentication** key in the header
* **Body**: The body of the message: Proxyman automatically formats and beautifies the body content depends on the **Content-Type,** such as JSON, PNG, GIF, Raw Data, ...
* **Query**: If the request has a query, all queries are presented.
* **Raw**: The RAW HTTP message.
* Protobuf Message
* MessagePack
* Multipart/form-data

### Custom Previewer Tab

It's possible to customize which Previewer Tab you would like to see

* Custom tabs will persistent on the Request/Response Panel
* Attempt to decode and beautify the content

{% content-ref url="custom-previewer-tab" %}
[custom-previewer-tab](https://docs.proxyman.com/basic-features/custom-previewer-tab)
{% endcontent-ref %}

![Custom Previewer Tab](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-Md01ISVIn5N9gt1kT_C%2F-Md01URMXqWeaY7AsRN1%2FScreen%20Shot%202021-06-25%20at%2009.39.55.png?alt=media\&token=0e66b6bc-cb2c-49bd-860f-ca056224914d)

### Layout mode

There are two way to order the Request / Response Panel: Vertical or Horizontal layout

![Request/ Response Panel](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-LmSUd_OpdDpUrjpkX-6%2F-LmSVFKeUuNPwG6HpV-Y%2Fhttp_response_vertical.png?alt=media\&token=d6d53954-50df-450a-af52-af459f5661c6)

![Previewer in Horizontal Layout](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-M5k_8UnCbVU-a0Ksr1u%2F-M5kdG7Ych9_JbU82Mm7%2FScreen%20Shot%202020-04-25%20at%2016.21.34.png?alt=media\&token=628d3d65-a04b-4293-8736-694b1eb81a81)

![Previewer in Vertical layout](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-M5k_8UnCbVU-a0Ksr1u%2F-M5kdOeUJerSyTDQLo45%2FScreen%20Shot%202020-04-25%20at%2016.21.55.png?alt=media\&token=82117838-42e8-47f1-b9de-30291225395e)

### Customize Workspace

You can use custom layout buttons on the top right corner of the app to display content as your preference

1. Collapse/Expand Source List Panel&#x20;
2. Open Request/ Response Panel in new window
3. Display Request/Response Panel in Horizontal layout
4. Display Request/Response Panel in Vertical layout

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-M5kgZfgX_GZuzjAbAQT%2F-M5khQdFnInkcHQX-Ci_%2F02.png?alt=media\&token=f6ff8a61-f333-4b80-91d8-24c98d3bd60d)

### Shortcuts

All sections are support **Copy (⌘C)** and multiple selections

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-LmSUd_OpdDpUrjpkX-6%2F-LmSXLCTr7qnOJvQv4rH%2FScreen%20Shot%202019-08-17%20at%2010.04.36.png?alt=media\&token=50f23788-9945-40f8-b41b-df178df72e2c)

Read more at our [Proxyman Keyboard Shortcuts](https://proxyman.io/blog/2019/08/Proxyman-keyboard-shortcuts.html) blog

### **Body Previewer**&#x20;

Body previewer automatically beautifies the content as well as offering handy minor features:

* **Tree View**: Represent the JSON in Tree View mode
* **Hex**: Show the body in Hex format
* **Export only body**: Able to export your body content to file. Suitable for Raw Data or binary data
* **Open With**: You can open the Body content with your favorite Editor. **Sublime Text** is mime 😍

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-LmSXcp2h6D33De4N0wo%2F-LmSXeS1vqgVfomWgdCG%2Fbody_previewer.png?alt=media\&token=8753aa59-aaf1-4000-aed2-54ce2a45b709)

### JSON Tree View mode

Proxyman supports native JSON Tree View mode, which displays a JSON Body. It allows the developer to:

* Search JSON by [JSON Path](https://docs.proxyman.com/basic-features/jsonpaths)
* Copy JSON Node like Google Developer Tool does.

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FxD1Lpl6PBL1gU4GwVpWo%2FScreen%20Shot%202021-10-15%20at%2016.14.44.png?alt=media\&token=b22d8a79-401a-4609-b17b-adca36609cd4)
