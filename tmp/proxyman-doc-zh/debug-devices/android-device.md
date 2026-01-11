# Android设备和模拟器

为了从您的物理Android设备或Android模拟器捕获和解密HTTP/HTTPS请求/响应，请导航到:

* ** 证书 ** ** 菜单 ** -> ** 在Android上安装证书-> 设备 **
* ** 证书菜单-> 在Android上安装证书-> 模拟器 **

{% 提示样式 = "info" %}
查看 [关于如何设置Android设备和模拟器的迷你教程](https://docs.proxyman.com /调试-设备/android-设备/示例-android-项目)
{% endhint %}

{% 提示样式 = "info" %}
对于 ** Android模拟器 **，让我们查看 [Android模拟器的自动脚本](https://docs.proxyman.com /调试设备/自动脚本-用于android-模拟器 # 1-whats-it)
{% endhint %}

# #1.Android设置指南

如果您想从物理或模拟器Android设备捕获和解密HTTP/HTTPS流量，请按照设置指南中的所有步骤操作:

<figure><img src = "images/Screenshot_2023-08-26_at_09.50.35_faa659bd.png" alt = "" width = "563"><figcaption><p> Android设备安装指南 </p></figcaption></figure>

1.证书菜单-> 在Android上安装证书-> ** 设备 **
2.在您的计算机上安装 ** Root Proxyman证书 **: 您可以按照 [macOS指南](https://docs.proxyman.com /调试设备/macos) 进行操作。
3.获取您的Android设备或模拟器-> 打开设置应用程序-> Wifi -> 选择当前Wifi -> 通过以下表格配置HTTP代理。

| 名称 | 值 |
| -------------- | ------------------------------------------------- |
| 服务器IP | 您当前的IP网络 |
| Port | 默认为Proxyman: 9090的当前端口 |
| 身份验证 | 否 |

{% 提示样式 = "info" %}
某些三星设备在设置HTTP代理后无法访问互联网。请尝试忘记当前网络并重新连接。

如果 ** 您正在使用任何VPN应用 **，请确保将其关闭，因为某些VPN应用与HTTP/HTTPS代理配置冲突。
{% endhint %}

3 \。从Android设备上的本机web浏览器打开 <http:// proxy.man/ssl> 或 <http:// cert.proxyman.io> 以安装Proxyman证书。

### ** Android 11，Android 12或更高版本: **

* 从Google Chrome应用访问 <http:// proxy.man/ssl> 以下载证书。
* 从Android 11或更高版本，您必须在设置应用程序中手动安装证书。
* 设置应用程序-> 安全-> 加密和凭据-> 安装证书-> 选择 “CA证书”-> 选择Proxyman CA证书在您的存储。

### ** Android 10及以下版本: **

* 只要您访问 <http:// proxy.man/ssl>，您的Android设备将自动下载并安装它。确保选择 ** VPN和应用部分 **。

{% 提示样式 = "info" %}
** 在Android 12 + 上 **，如果您遇到此警告 “无法安装证书: 此文件不能用作VPN和app用户证书”，请尝试选择 “CA证书”。

参考: <https://stackoverflow.com/a/ 70261393/3127477>
{% endhint %}

{% 提示样式 = "info" %}
**<http:// proxy.man/ssl>** 是一个本地网站，从本地Proxyman的HTTP服务器提供服务。如果您无法打开它，请忘记wifi，重新连接，并确保Proxyman应用程序正在打开。
{% endhint %}

4 \。在Android 11和Android 12上。让我们通过打开可信凭据-> 用户选项卡进行验证。

确保您可以看到 ** Proxyman CA ** 证书，如下面的屏幕截图所示。

![验证是否正确安装了Proxyman CA证书] (图像/Screen_Shot_2020-09-29_at_9_00_46_PM_a27a0bd6.png)

5 \。打开您的应用程序源代码: 添加以下两个 “xml” 文件。

* 添加 ** res/xml/network \_security \_config.xml **

{% code title = "network \_security \_config.xml" %}

''' 标记
<network-security-config>
<debug-overrides>
<trust-anchors>
<!-- 仅可调试时信任用户添加的CAs -->
<证书src = "user" />
<证书src = "system" />
</trust-anchors>
</debug-overrides>

<base-config cleartextTrafficPermitted = "true">
<trust-anchors>
<证书src = "system" />
<证书src = "user" />
</trust-anchors>
</base-config>
</network-security-config>
'''

{% endcode %}

* 添加到 ** AndroidManifest.xml **

{% code title = "manifest.xml" %}

''' 标记
<？xml version = "1.0" encoding = "utf-8"？>
<清单...>
<应用程序android:networkSecurityConfig = "@ xml/network_security_config" ... >
...
</application>
</manifest>
'''

{% endcode %}

{% 提示样式 = "info" %}
在 [网络安全配置] 中查找更多信息 ( https://developer.android.com/training/articles/ security-config.html)
{% endhint %}

{% 提示样式 = "info" %}
确保您 ** 在发布版本中删除这些配置 **。如果没有，您的HTTP/HTTPS请求可能会被拦截，并在生产构建中泄漏您的敏感数据。
{% endhint %}

6 \。如果是Android模拟器，请重新启动模拟器

7 \。完成了…

# # ** 2.故障排除 **

请查看此 [故障排除部分。](https://docs.proxyman.com /调试-设备/示例-android-项目 #4-故障排除)

# #3.示例Android项目

如果你一直在努力配置XML设置，让我们看看这个简单的项目，我们已经配置:

Github链接: <https://github.com/ProxymanApp/ okhttp-android-sample>

{% content-ref url = "android-设备/sample-android-project" %}
[示例-android-项目](https://docs.proxyman.com /调试-设备/android-设备/示例-android-项目)
{% endcontent-ref %}

# #4.React原生Android应用

如果您在Android应用程序中使用React Native，请查看 [React Native页面](https://docs.proxyman.com /调试设备/react-native)。

# #5.拦截嵌入WebView的流量

一些Android应用程序嵌入了WebView，需要额外的步骤来拦截HTTPS流量。

1.确保您能够看到来自Android应用的其他HTTPS流量。这意味着您已经正确设置了证书
2.注入以下代码到您的WebView

'''java
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {
WebView.setWebContentsDebuggingEnabled(true);
}

// 以下两行有助于禁用资产缓存
webView.getSettings().setAppCacheEnabled(false);
webView.getSettings().setCacheMode(WebSettings.LOAD_NO_CACHE);
'''

3 \。在您的计算机上打开一个新的Chrome标签，然后导航到 “Chrome: // inspector”

4 \。当您打开WebView时，视图将出现在您的Chrome选项卡中，然后您只需单击 “检查” 即可开始使用远程调试器。

# #6.使用根设备进行SSL代理

> 信用为 [Shirshak](https://github.com/shirshak55)

如果您的Android版本低于7，则无需执行此步骤。Google增加了额外的安全性，不允许middle应用程序在Android 6之后进行攻击。即无法对android应用程序进行MITM攻击。

我们不承担任何责任的生根手机造成的问题。所以请遵循指南在您自己的风险。

1.根您的手机与 'magisk' 框架。
2.安装根文件浏览器，以便您可以在受限制的系统文件夹中复制和粘贴文件。
3.在命令行中键入以下脚本

'''bash
$ cd ~/.proxyman
// 我们将证书复制到另一个文件名，以便以后可能需要它
$ cp proxyman-ca.pem温度pem
$ hash = $(openssl x509-通知PEM -subject_hash_old-在temp.pem | head -1中)
$ mv temp.pem "$ hash.0"
'''
4.如果你去 '~/.proxyman' 文件夹，你必须注意一个以数字开头的文件名
5.将该文件复制到您的Android。
6.使用根文件浏览器将该文件传输到/system/etc/security/cacerts/
7.享受代理。

{% 提示样式 = "info" %}

1.使用Android手机时，将网关设置为任何错误的IP，以便您可以确保所有流量仅来自proxy man代理。
2.我们可以使用macOS共享功能创建移动热点。从Android手机，您可以轻松使用Proxyman代理。它要好得多，因为有时路由器可以阻止移动设备和macOS之间的请求。
{% endhint %}

# # 额外资源

* Mitmproxy有一个关于如何在Android模拟器上安装Proxyman证书的有用教程: <https://docs.mitmproxy.org/stable/ howto-install-system-trusted-ca-android/>
