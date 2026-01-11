# 我的远程设备 (iOS/Android) 无法连接到Proxyman？

# # ** 1.** 问题

*❌在Wifi设置中更改代理配置后，我的iOS或Android设备无法访问互联网。
*❌我无法从 **<http:// cert.proxyman.io>** 或 **<http:// proxy.man/ssl>** 下载证书

{% 提示样式 = "info" %}
对于Android，请按照 [第二部分](# android-设备和android-模拟器)
{% endhint %}

# #2.解决方案: iOS设备

请确保仔细检查以下步骤:

### 0.iOS 16物理设备/模拟器的问题

来自Proxyman用户的一些报告称，** Proxyman ** 和 ** Charles Proxy ** 无法捕获来自iOS 16设备/模拟器的任何流量，即使他们配置了HTTP代理。

这是一个来自iOS的错误，我们必须等待苹果团队来修复它。

解决方法:

#### iOS 16物理设备:

* 忘记网络并尝试再次连接。
* 使用 [亚特兰蒂斯框架](https://github.com/ProxymanApp/atlantis) 捕获交通
* 使用iOS 15设备

#### iOS 16模拟器:

* 使用iOS 15模拟器
* 使用 [亚特兰蒂斯框架](https://github.com/ProxymanApp/atlantis) 来捕获交通。

{% content-ref url = "ios-16-devices-issues" %}
[ios-16-devices-issues](https://docs.proxyman.com/troubleshooting/ ios-16-devices-issues)
{% endcontent-ref %}

### 1.确保您的Mac设备和iOS/Android设备位于同一网络中

如果它们在不同的网络上，则无法相互连接。

### 2.确保服务器IP和端口号必须与Proxyman匹配

![](images/IMG_4110_5f885ce6.png)

![](图片/Screen_Shot_2020-03-10_at_20_37_01_9713a7dd.png)

### 3.从macOS和iOS/Android设备关闭所有VPN应用程序

默认情况下，VPN应用将 ** 强制 ** 所有流量通过VPN服务器而不是Proxyman代理服务器 (在9090处)。因此，没有出现在Proxyman应用程序的请求。

关闭所有VPN应用程序将修复它:

* 对于 ** iOS ** 设备: 导航到设置-> 常规-> VPN，并确保VPN状态为 ** 关闭 **
* 对于 ** Android ** 设备: 在设置应用程序上找到VPN设置并将其关闭
* 对于 ** macOS **: 退出所有VPN应用

### 4.防火墙设置 (macOS)

默认情况下，防火墙可能会阻止所有传入mac的流量。因此，您的远程设备可能无法连接到Proxyman。

在 ** macOS ** 上: 导航到 ** 系统首选项-> 安全和隐私-> 防火墙选项卡-> 选项 **

** 验证: **

* 阻止所有传入的连接是 ** 关闭 **
* Proxyman应用程序 ** 允许传入连接 **
* 如果没有Proxyman应用程序，请点击 + 按钮添加Proxyman应用程序
* 自动允许内置软件接收传入的连接是 ** 上 **
* 自动允许下载的签名软件接收传入的连接是 ** 上 **

![macOS上的防火墙设置] (图片/Screen_Shot_2020-03-10_at_20_46_17_ac98dabc.png)

### 4.防火墙设置 (Windows 10/11)

Windows 10/11可能会阻止Proxyman，并且iPhone/Android设备无法连接到该应用程序。要修复它:

1.搜索并打开 “Windows Defender防火墙” 应用程序-> 单击左侧面板上的 “高级设置”
2.选择 “入站规则”
3.找到Proxyman.exe -> 双击打开设置
4.在常规选项卡中选择 “允许连接”
5.单击 “好”

<figure><img src = "images/CleanShot_2023-01-05_at_09.26.50_2x_8e46c689.png" alt = ""><figcaption><p> 在Windows防火墙上允许Proxyman </p></figcaption></figure>

### 5.如果您使用的是公司网络，请让安全团队打开Proxyman的端口9090

默认情况下，某些公司会阻止某些端口。因此，您的iOS设备无法9090访问Proxyman的端口。

### 6.使用Safari上的专用浏览器打开 <http:// cert.proxyman.io> 或 <http:// proxy.man/ssl>

### 7.我仍然无法连接。

如果您按照上述所有步骤进行操作，并且所有配置均正确，但尚未解决您的案例。

请尝试 ** 打开/关闭您的Wifi，忘记Wifi网络 (iOS)，** 和 ** 重新启动计算机 **。

### 8.还是不行？(仅限iOS应用程序)

手动覆盖HTTP代理，在iOS设备上安装和信任Proxyman很难。我们理解这一点。让我们试试亚特兰蒂斯，这是一个iOS框架，可以帮助你自动做到这一点。

{% content-ref url = "../atlantis/atlantis-for-ios" %}
[Atlantis-for-ios](https://docs.proxyman.com/atlantis/ atlantis-for-ios)
{% endcontent-ref %}

# # Android设备和Android模拟器

### 1.在Wifi设置中设置HTTP代理后，我无法打开 <http:// Proxy.man/ssl>

* [请遵循上述故障排除](# 1-make-sure-your-mac-device-and-ios-devices-are-on-the-same-network)☝️
* 在模拟器中仔细检查Wifi连接。它必须是连接状态 (不限制连接或没有互联网)

如果发生，请尝试 ** 忘记网络 ** 并 ** 重新连接Wifi。**

<div align = "center"><img src = "images/Screen_Shot_2020-09-29_at_8_52_45_PM_b4fbc533.png" alt = "" width = "375"></div>

### 2.使用API 30 + 安装并信任适用于Android的Proxyman CA

从Android模拟器API 30 +，它需要额外的步骤来信任Proxyman证书

* 从Google Chrome打开 <http:// proxy.man/ssl> 以下载证书
* 设置应用程序-> 安全-> 加密和凭据-> 安装证书-> CA证书-> 无论如何安装并在存储中选择CA Proxyman证书

您可以通过打开可信凭据-> 用户选项卡进行验证

![信任证书] (图片/Screen_Shot_2020-09-29_at_9_00_46_PM_92f669c2.png)

### 3.我的Android物理设备或模拟器连接不稳定。

它可能会费到Android设备/模拟器，唯一的方法可能修复它是将DNS从您的Mac或Android设备更改为 ** 8.8.8.8 **

* ** 在macOS上 **: 打开系统首选项-> 网络-> 选择Wifi -> 高级-> 选择DNS选项卡-> 在DNS服务器表上输入 ** 8.8.8.8 **
* ** 在Android设备上 **: 打开Wifi设置-> 将DNS设置为 ** 8.8.8.8 **

阅读更多 < https://github.com/ProxymanApp/Proxyman/issues/ 636>

![](图片/Screen_Shot_2020-10-12_at_08_18_35_96037bf5.png)

### 4.找不到 “adb” 命令!使用Android模拟器自动脚本时

如果您尝试覆盖Android模拟器，并得到以下错误:

'''
adb命令行找不到!
'''

请安装 “adb” 命令行，然后重试!

* [如何安装亚行](https://docs.proxyman.com /调试-设备/android-设备/自动-脚本-用于-android-模拟器 #4-如何-它-工作)

### 5.如果您使用Android模拟器进行调试，并且不知道如何安装和信任Proxyman证书，请考虑使用 [Android模拟器的自动脚本](https://docs.proxyman.com /调试-设备/android-设备/自动-脚本-for-android-模拟器)
