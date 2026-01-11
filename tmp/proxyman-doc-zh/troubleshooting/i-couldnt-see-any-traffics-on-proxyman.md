# 我在Proxyman上看不到任何流量

### 1.问题

* 启动应用程序后，请求列表为空
* 没有被Proxyman捕获的请求？
* 我没有看到应用程序上的任何请求
* 我可以在我的Mac上看到一些请求，但在我的远程设备 (iOS，Android) 上没有请求

{% 提示样式 = "info" %}
对于远程设备 (iOS或Android)，请查看此 [疑难解答](https://docs.proxyman.com/troubleshooting/ my-ios-设备-couldnt-connect-to-proxyman-via-代理)。
{% endhint %}

![](图片/Screen_Shot_2020-04-26_at_09_48_10_dc091250.png)

### 2.解决方案

### 2.1关闭Mac机器上的所有VPN应用程序

一旦Proxyman覆盖它，一些VPN应用程序就会意外恢复网络中的HTTP代理。因此，HTTP流量在9090时不会通过Proxyman端口。

如果可能，关闭所有VPN应用程序并重新启动Proxyman

### 2.2。双重检查网络中的HTTP代理

Proxyman会在启动或退出时覆盖或还原HTTP代理，但某些应用程序可能会还原。

让打开系统首选项-> 网络-> Wifi -> 代理选项卡:

* 检查 ** Web代理 (HTTP)** 和 ** 安全Web代理 (HTTPS)**
* 确保端口与Proxyman端口相同
* IP是 ** 127.0.0.1 **

保存并检查Proxyman上的请求

![](图片/Screen_Shot_2020-04-26_at_09.54.53_d97db6f6.png)

### 2.3安装Proxyman帮助工具

默认情况下，Proxyman尝试使用 “networksetup” CLI覆盖系统HTTP代理，但在某些情况下可能会失败。

\=> 让我们尝试安装Proxyman帮助工具。此工具将正确覆盖系统HTTP代理。请打开Proxyman首选项-> 高级选项卡-> 安装帮助工具

![](图片/Screen_Shot_2020-10-12_at_08_24_05_65c0dac5.png)

### 2.4 Proxyman缺少某些HTTP/HTTPS请求

Alamofire或URLSession可能会为您的请求使用缓存的响应。因此，实际的请求不会命中服务器。因此，Proxyman无法捕获并在应用程序上显示它。

解决方案:

* 禁用URLSession或Alamofre上的缓存机制。
* 使用 [无缓存工具](https://docs.proxyman.com /高级功能/无缓存) (⌘ ⌘ n)
