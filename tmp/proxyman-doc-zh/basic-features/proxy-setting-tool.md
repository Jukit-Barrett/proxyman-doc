# Proxyman代理帮助工具

# # Proxyman代理帮助工具

默认情况下，Proxyman将尝试使用 [networksetup](https://www.unix.com/man-page/osx/8/networksetup/) 命令行覆盖您的HTTP/HTTPS代理配置。但是，** networksetup ** 是启动或退出应用程序的瓶颈。

Proxyman提供了一个更好的解决方案: ** Proxyman代理帮助工具 **，这是一个 [特权帮助工具macOS](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/AccessControl.html#// apple_ref/doc/uid/TP40002589-SW2)，以覆盖网络代理在 ** 高性能 **。[ ](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/AccessControl.html#// apple_ref/doc/uid/TP40002589-SW2)

{% 提示样式 = "info" %}
您可以通过使用或不使用代理设置工具启动应用程序来注意到性能差异。
{% endhint %}

在第一次启动时，Proxyman将显示安装Proxyman代理帮助工具的弹出窗口。您可以跳过它并稍后在 ** 首选项 ** -> ** 高级 ** 选项卡中安装它。

<figure><img src = "images/Screen_Shot_2022-10-25_at_10.11.32_dd343b23.png" alt = ""><figcaption></figure>

{% 提示样式 = "info" %}
安装后，您可以在 “/Library/PrivilegedHelperTools/com.proxyman.NSProxy.Helpertools” 中找到帮助工具。

如果Proxyman发布了代理设置帮助工具的新更新，则需要重新安装。
{% endhint %}

### 需要用户权限才能使用macOS 13 Ventura或更高版本

MacOS Ventura或更高版本需要获得许可才能正常工作。

要授予权限，请按照以下步骤操作:

1.打开系统设置-> 常规-> 登录项
2.找到Proxyman并打开 â œ…

<figure><img src = "images/Screenshot_2022-11-20_at_21.10.43_556cc05e.png" alt = ""><figcaption><p> 将权限授予Proxyman辅助工具 </p></figcaption></figure>

### 来宾或非管理员用户

如果您是来宾或非管理员用户，“networksetup” CLI将失败，并且在安装Proxyman代理帮助工具之前无法更改HTTP/HTTPS代理配置。

Proxyman代理帮助工具具有特权权限，可以覆盖各种用户的代理配置。

如果您是来宾或非管理员用户，我们强烈建议您安装Proxyman Helper工具，以使UX更加流畅。

### 卸载代理帮助工具

您可以在 ** 首选项 ** -> ** 高级 ** 选项卡-> ** 卸载 ** 代理设置工具中卸载代理帮助工具，也可以直接在 '/Library/PrivilegedHelperTools/com.proxyman.NSProxy.Helpertools' 中删除它

# # 通过命令行安装代理帮助工具

在macOS 4.12.0或更高版本中，您可以在没有GUI的情况下安装帮助工具。

'''
sudo /Applications/Proxyman.app/Contents/MacOS/proxyman -- install-privileged-components
'''

# # Changelog

# #版本1.6.0 (Proxyman 5.11.0或更高版本)

* 修正: 当应用程序关闭时，Proxyman无法恢复PAC URL

### ** 版本1.5.0 **

* 修复了Proxyman v1.5.0或更早版本 (2019) 可以连接到帮助工具 (v1.4.0) 并在未经用户同意的情况下覆盖系统代理的安全漏洞。此修复将添加一些约束来验证传入的连接。(调用者必须经过Apple公证，由Proxyman LLC证书签名，启用库验证和启用强制硬标志)。(CVE-2023-45732)

从NCC集团贷记 ** Scott Leitch **。

### ** 版本1.4.0 **

* 符合新的macOS 13 Ventura辅助工具要求
* 在登录项目上显示应用程序图标和应用程序名称

<figure><img src = "images/197530484-0f897b6f-7905-4d65-bdc3-86d2fc8abebe_72f7ab7a.png" alt = ""><figcaption><p> 显示正确的Proxyman图标和应用程序名称 </p></figcaption></figure>

{% 提示样式 = "info" %}
在macOS Ventura上，辅助工具、启动守护程序和启动代理将添加到后台的允许中，即使Proxyman仅在前台运行也是如此。

[Twitter] 上正在进行讨论 ( https://twitter.com/siracusa/status/ 1583914093437935616？s = 46 \ & t = C1XB91IkDFkG697Ab8T9Dg)，macOS应该修复它。
{% endhint %}

安装1.4.0后，由于首选项的缓存层，登录项可能不会更新。

<figure><img src = "images/Screen_Shot_2022-10-25_at_10.00.04_be43b109.png" alt = ""><figcaption><p> 无效缓存 </p></figcaption></figure>

要修复它:

1.打开终端应用程序-> 运行: 'sfltool resetbtm'
2.重新启动macOS
3.完成

### ** 版本1.3.0 **

* 记住并恢复到以前的代理设置。

### 版本1.2.0:

* 优雅地恢复HTTP代理配置，如果Proxyman崩溃。

### 故障排除

如果您在安装帮助工具时遇到此错误:

该操作可以™t完成。(CFErrorDomainLaunchd错误9。)

请遵循此解决方案: <https://cloud.tencent.com/developer/article/ 1816504>

参考: <https://github.com/ProxymanApp/Proxyman/issues/ 1113>
