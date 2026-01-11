# iOS模拟器

为了从您的iOS模拟器设备捕获HTTP/HTTPS消息，请导航到:

* ** 证书 ** ** 菜单 ** -> ** 在iOS上安装证书-> 模拟器 **

# #1.iOS模拟器设置指南

![自动将证书安装到iOS模拟器] (图片/Screen_Shot_2022-07-11_at_08.15.26_62f83677.png)

{% 提示样式 = "info" %}
它适用于iOS，iPadOS，tvOS和watchOS。
{% endhint %}

下图描述了三个步骤:

1.在您的计算机上安装 ** Root Proxyman证书 **: 您可以按照 [macOS指南](https://docs.proxyman.com /调试设备/macos) 进行操作。
2.将Proxyman证书安装到所有可用的模拟器，您至少打开过一次。
3. ** 重置模拟器 **: Proxyman尝试重置所有模拟器，因此它将加载新证书。

{% 提示样式 = "info" %}
从Proxyman 2.19.0 + 开始，Proxyman使用 [simctl](https://nshipster.com/simctl/) 命令行执行任务。

** simctl ** 内置在您安装的Xcode上，比传统方法 (使用Python自定义脚本) 更现代，更可靠。
{% endhint %}

{% 提示样式 = "info" %}
此步骤仅安装在模拟器上，您至少已打开一次

例如，如果您想在iPhone X模拟器上进行调试，请确保先 ** 打开 ** iPhone X模拟器，然后 ** 安装 ** 步骤2中的证书
{% endhint %}

### Xcode预览 (SwiftUI)

如果您使用的是Xcode Preview for SwiftUI，则可以通过以下方式将证书安装到Xcode Preview模拟器中:

1.使用预览器模式 (SwiftUI) 打开Xcode。
2.打开Proxyman -> 证书菜单-> 安装iOS -> 模拟器
3.点击高级按钮-> 安装Xcode预览

您可以在以下位置阅读更多信息: <https://github.com/ProxymanApp/Proxyman/issues/ 1568 # issue-1610877870>

### 手动安装

在Proxyman v4.16.0或更高版本中，您可以手动将证书安装到iOS模拟器，以防自动解决方案不起作用。

1.证书菜单-> 安装iOS证书-> 模拟器
2.在步骤2中，单击 ↓ 按钮 (准备模拟器按钮旁边) -> 手动安装…

<figure><img src = "images/Screenshot_2024-11-01_at_20.14.39_c7c865d2.jpg" alt = ""><figcaption><p> 手动安装证书 </p></figcaption></figure>

3.将证书拖放到您的iOS模拟器

<figure><img src = "images/Screenshot_2024-01-07_at_14.43.13_2d2df0ec.png" alt = "" width = "563"><figcaption><p> 手动安装证书 </p></figcaption></figure>

4.打开你的iOS模拟器-> 设置应用程序-> 常规-> 关于-> 证书信任设置-> 找到Proxyman CA证书并将其打开
5.完成

# #2.故障排除

### 1.无法安装证书

如果您在单击步骤2时出现错误，请打开Xcode -> 首选项-> 位置选项卡-> 在命令行工具中选择您的Xcode。

![确保你有Xcode命令行] (图片/Screen_Shot_2022-07-11_at_08_12_33_db768e2b.png)

### 2.从HTTPS响应获取SSL错误

* 打开设置应用程序-> 常规-> 关于-> 证书信任设置，并验证Proxyman证书是否已安装并受信任。

![已正确安装并信任Proxyman证书] (图像/Screen_Shot_2021-03-05_at_13.32.25_2f2ddcb6.png)

如果未安装:

* 打开iOS模拟器设置 (证书菜单-> 在iOS上安装证书-> 模拟器)，然后单击第二个按钮。
* 或尝试以下步骤手动安装证书。

### 3.Proxyman缺少某些HTTP/HTTPS请求

Alamofire或URLSession可能会为您的请求使用缓存的响应。因此，实际的请求不会命中服务器。因此，Proxyman无法捕获并在应用程序上显示它。

解决方案:

* 禁用URLSession或Alamofre上的缓存机制。
* 使用 [无缓存工具](https://docs.proxyman.com /高级功能/无缓存) (⌘ ⌘ n)

# # 通过导出证书手动安装证书

如果无法安装证书，可以 ** 手动 **:

1.打开Proxyman -> 证书菜单-> 导出-> 根证书作为DER -> 保存到桌面文件夹
2.打开模拟器 ** 拖动证书并将其 ** 放在模拟器屏幕上
3.打开设置app (在模拟器上) -> 常规-> 设备管理-> 选择证书-> 安装
4.设置应用程序-> 常规-> 关于-> 证书信任设置，并验证Proxyman证书是否已安装并受信任。
5.完成✅

### 教程

使用proxyman查看 [在iOS模拟器上调试应用程序](https:// Proxyman.io/blog/2019/07/Debugging-on-iOS-Simulator-with-Proxyman.html) 的详细步骤
