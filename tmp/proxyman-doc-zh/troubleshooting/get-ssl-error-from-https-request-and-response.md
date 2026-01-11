# 来自HTTPS请求/响应的SSL错误

# #1.问题

* 您无法在Proxyman应用程序上看到任何HTTPS流量
* 您从HTTPS请求和响应中获得SSL错误。
* 你得到 ** SSL握手失败 **

![](图片/Screen_Shot_2020-04-25_at_19.52.38_e60fe67b.png)

# #2.解决方案

SSL握手失败的原因有很多，请通过以下步骤来解决问题。

# #2.1移动设备

### iOS设备

* 按照这个 [iOS设置指南](https://docs.proxyman.com /调试设备/ios设备) -> 确保你已经安装和信任您的设备上的Proxyman CA证书。
* 如果你拦截一些流行的应用程序 (例如Facebook，Instagram的，苹果，Whatsapp的，...): 他们是由SSL固定保护-> 不可能拦截他们。
* 验证您的iOS应用程序没有SSL Pinning。如果是，请禁用它。

### iOS模拟器

按照这个 [iOS模拟器设置指南](https://docs.proxyman.com /调试设备/ios模拟器) -> 确保您已经安装和信任您的设备上的Proxyman CA证书。

### 安卓设备

* 按照这个 [Android设备设置指南](https://docs.proxyman.com /调试设备/android设备) -> 确保您已经安装和信任您的设备上的Proxyman CA证书。
* 验证第5步是否已完成 (通过将您的域添加到两个文件: ** res/xml/network \_security \_config.xml ** 和 ** AndroidManifest.xml **)
* 如果你试图拦截Android应用程序，你不是一个所有者-> 这是不可能的拦截->❌

### Android模拟器

* 按照这个 [Android模拟器安装指南](https://docs.proxyman.com /调试-设备/android-设备/自动脚本-为android-模拟器) -> 确保您已经安装和信任您的设备上的Proxyman CA证书。
* 验证第5步是否已完成 (通过将您的域添加到两个文件: ** res/xml/network \_security \_config.xml ** 和 ** AndroidManifest.xml **)
* 如果你试图拦截Android应用程序，你不是一个所有者-> 这是不可能的拦截->❌

### React Native app

* 如果您的应用是React Native应用，请遵循 [React Native指南](https://docs.proxyman.com /调试设备/react native)。

### 颤振

* 请遵循 [Flutter设置指南](https://docs.proxyman.com /调试设备/flutter)

如果您已经尝试并验证了上述所有步骤，但仍然收到SSL错误？

### 验证您能够看到HTTPS请求/响应从 < https://google.com > 没有任何错误

1.获取您的设备
2.打开网络浏览器 (iOS上的Safari或Android上的Google Chrome)
3.访问 **<https://google.com>**
4.在适用于macOS的Proxyman应用程序上的此域上选择 “启用SSL代理”
5.验证您是否能够看到HTTPS响应。

####✅成功

1.您可以看到 < https://google.com> HTTPS响应，这意味着您正确设置了证书-> 这很好✅
2.问题可能来自您的应用程序。让我们再次尝试您的域/应用程序-> 如果SSL错误仍然发生，这个应用程序受到SSL固定保护的可能性很高。
3.如果你认为它不是一个SSL固定的情况下，请打开 [Github](https://github.com/ProxymanApp/Proxyman/issues) (请注明什么设备，操作系统版本，应用程序名称等) 的票

####❌失败!

* 似乎Proxyman证书未在您的设备中正确安装或信任。请返回 [2.1移动设备](#2.1-移动设备) 部分并按照它进行操作。
* 如果您验证一切都已完成，但SSL错误仍然发生，请在 [Github](https://github.com/ProxymanApp/Proxyman/issues) 上打开票证 (请提及什么设备，操作系统版本，应用程序名称等)

##2.2 Macbook或Windows PC

我从以下位置收到SSL错误:

* ** Mac设备 (Macbook，Mac Mini，Mac Studio)** -> 在Macbook上安装并信任证书-> 遵循 [macOS指南](https://docs.proxyman.com /调试-设备/macos)
* ** Windows ** -> 在Windows机器上安装并信任证书-> 遵循 [Windows指南](https://docs.proxyman.com/proxyman-windows)
* Java -> 遵循 [Java VM指南](https://docs.proxyman.com /调试设备/java)
* Firefox -> 遵循 [Firefox指南](https://docs.proxyman.com /调试设备/firefox)
* Python -> 遵循 [Python指南](https://docs.proxyman.com /调试设备/python)
* Ruby -> 遵循 [Ruby指南](https://docs.proxyman.com /调试设备/ruby)

{% 提示样式 = "警告" %}
默认情况下，某些网络库 (Ruby，NodeJS，Python，Golang) 不信任自签名证书。我们必须明确地告诉库信任证书。

\=> 要修复它，请谷歌 ** “\ <您的框架/库> 自签名证书”，** 在StackOverflow上找到了一些答案。
{% endhint %}

##2.3 SSL固定？

* 您仍然无法在您的应用程序上看到HTTPS响应，似乎您的应用程序受到 [ssl-pinning](https://en.wikipedia.org/wiki/ HTTP_Public_Key_Pinning) 的保护，从而阻止MitM应用程序看到内容。所有流行的应用程序 (Facebook，Apple，Instagram，Messenger等) 都具有此功能。
* 请暂时 ** 禁用ssl-pinning **，然后重试。

阅读更多关于ssl-pining: <https://www.raywenderlich.com/1484288-preventing-man-in-the-middle-attacks-in-ios-with-ssl-pinning>

{% 提示样式 = "info" %}
如果你已经尝试了一切，但不确定什么是错的？请打开 [Github ticket](https://app.gitbook.com/o/-LlPtWiscJCRFiRPxWvB/s/- LlPt_6BePnJ3oK3saP1/)。

还请提及: Proxyman macOS/Windows，Proxyman版本，您的iOS/Android设备等.
{% endhint %}
