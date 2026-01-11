# iOS设备

要在iOS设备 (iPhone，iPad) 中捕获HTTP/HTTPS消息，请导航到:

* ** 证书 ** ** 菜单 ** -> ** 在iOS上安装证书-> 物理设备... **

{% 提示样式 = "成功" %}
本设置指南适用于所有真实的物理设备，包括iPhone、iPad、Apple Watch、Apple TV和Vision PRO。
{% endhint %}

# # iOS设置指南

<figure><img src = "images/Screenshot_2025-10-28_at_21.29.31_65ce91bb.png" alt = "Install certificate to iPhone Setup Guide"><figcaption></figure>

让我们遵循指导方针:

1.在您的计算机上安装 ** Root Proxyman证书 **: 您可以按照 [macOS指南](https://docs.proxyman.com /调试设备/macos) 进行操作。
2.获取您的iOS设备-> 打开设置应用程序-> Wifi -> 选择当前Wifi -> 按照以下表格配置HTTP代理。

| 名称 | 值 |
| -------------- | ------------------------------------------------- |
| 服务器IP | 您当前的IP网络 |
| Port | 默认为Proxyman: 9090的当前端口 |
| 身份验证 | 否 |

{% 提示样式 = "info" %}
如果您在macOS或iOS设备上使用任何 ** VPN应用 **，请确保关闭所有VPN应用，因为它们与HTTPS代理配置冲突。
{% endhint %}

3 \。从您的iOS设备打开 ** Safari Web浏览器中的 <http:// proxy.man/ssl> 或 [http:// cert.proxyman.io](http:// cert.proxyman.io/)，以安装Proxyman证书。

{% 提示样式 = "info" %}
**<http:// proxy.man/ssl>** 或 **<http:// cert.proxyman.io>** 是一个本地网站，由本地Proxyman的HTTP服务器提供服务。如果您无法打开它，请忘记wifi，重新连接，并确保Proxyman应用程序正在打开。

如果你不能访问它。请在 [Github的repo](https://github.com/ProxymanApp/Proxyman) 打开支持票。
{% endhint %}

4 \。从iOS 10.3，我们必须在设置应用程序中显式安装和信任Proxyman CA

#### ** 安装Proxyman CA **

* ** iOS â ‰ ¥ 12.2 **: 在您的iPhone上-> 打开设置应用程序> 下载的配置文件> 选择代理CA> 安装

#### 信任代理人CA

* 设置应用程序> 常规> 关于> 证书信任设置> 打开Proxyman CA。

![安装并信任Proxyman证书](images/install_and_trust_proxyman_certificate_7c885557.png)

{% 提示样式 = "info" %}
请确保我们 ** 安装 ** 和 ** 信任 ** Proxyman CA在您的iOS设备上。如果您有任何问题，请在 **<support@proxyman.io>** 向我们发送电子邮件或将其撞到 [** Github **](https://github.com/ProxymanApp/Proxyman)
{% endhint %}

{% 提示样式 = "info" %}
如果您看不到您的iOS设备的任何流量，请查看此 [故障排除](https://docs.proxyman.com/troubleshooting/ 我的-ios设备-couldnt-connect--proxyman-via代理)
{% endhint %}

{% 提示样式 = "info" %}
请确保您 ** 删除您的iPhone上的证书 ** 时，你没有调试的Proxyman。否则，您的HTTP/HTTPS请求可能会被拦截并泄露您的敏感数据。
{% endhint %}

# # 教程

请参阅有关如何使用proxyman [在iOS设备上调试应用程序](https:// Proxyman.io/blog/2019/06/How-I-use-Proxyman-to-see-HTTP-requests-responses-on-my-iPhone.html) 的详细步骤。

### 厌倦了手动配置？

我们知道手动覆盖HTTP代理并安装和信任Proxyman证书是很痛苦的。让我们看看亚特兰蒂斯，这是一个原生的iOS框架，可以帮助你自动完成。

{% content-ref url = "../atlantis/atlantis-for-ios" %}
[Atlantis-for-ios](https://docs.proxyman.com/atlantis/ atlantis-for-ios)
{% endcontent-ref %}

# # Flutter应用程序？

如果您的应用程序是Flutter应用程序，您可能无法在Proxyman上看到网络流量。

Flutter不使用系统级代理，因此不会显示对Proxyman的请求。为此，您必须手动配置代码中使用的HTTP客户端以使用代理。

请按照 < https://flutterigniter.com/debugging-network-requests/> 中的解决方案 “让Charles使用Flutter” 进行操作

要查找您的本地IP，请转到证书菜单-> 在iOS上安装证书-> 物理设备并获取服务器IP和端口
