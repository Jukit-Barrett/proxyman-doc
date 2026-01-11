# Firefox

# #✅新解决方案 (Proxyman v5.19.0或更高版本-推荐)

使用Proxyman v5.19.0 +，Proxyman可以通过单击设置从Firefox捕获HTTPS请求/响应。

1.转到设置菜单-> 自动设置
2.在Web浏览器部分-> 单击⬇️ 箭头按钮-> 选择Firefox

<figure><img src = "images/Screenshot_2025-04-28_at_09.53.27_216ff162.jpg" alt = ""><figcaption><p> 如何使用Proxyman从Firefox浏览器捕获HTTPS请求/响应 </p></figcaption></figure>

3.新的Firefox实例将打开
4.✅完成。来自Firefox的所有流量将被Proxyman捕获

此设置将使Firefox或Google Chrome:

* 自动设置Proxyman到Proxyman
* 自动安装和信任Proxyman证书

{% 提示样式 = "成功" %}
适用于Google Chrome和Firefox
{% endhint %}

# #❌旧解决方案 (Proxyman v5.18.0或ealier)

为了拦截来自Firefox的HTTPS流量，需要额外的步骤将Proxyman CA安装到Firefox的信任存储中。

### 1.在macOS计算机上安装Proxyman CA

在Java vm上安装Proxyman CA之前，我们必须在您当前的计算机上正确安装它。

查看macOS指南:

{% content-ref url = "macos" %}
[macos](https://docs.proxyman.com /调试-设备/macos)
{% endcontent-ref %}

如果您已完成此步骤，则可以跳到下一步。

### 2.在Firefox上设置代理

* 打开Firefox的首选项面板 (CMD +，)
* 搜索代理并打开代理设置
* 选择自动使用系统代理或手动硬编码代理IP和端口

![](图片/Screen_Shot_2020-09-19_at_14_33_17_bb072cd4.png)

### 3.将Proxyman CA安装到Firefox

1.在Firefox上打开 “http:// proxy.man/ssl”，并将证书下载到您的下载文件夹中

{% 提示样式 = "info" %}
<http:// proxy.man/ssl> 是用于增强安全性的本地HTTP服务器。访问此域时，请确保Proxyman应用程序处于打开状态。
{% endhint %}

2 \。打开Firefox的首选项 (CMD +，) 并打开查看证书窗口

![](图片/Screen_Shot_2020-06-23_at_10_27_27_de05a673.png)

3 \。打开 “授权” 选项卡并选择 “导入” 按钮

![](图片/Screen_Shot_2020-06-23_at_10_27_35_05163f39.png)

4 \。选择Proxyman CA，您已下载并信任所有。

![](图片/Screen_Shot_2020-06-23_at_10_37_52_8d3b3949.png)

5 \。重新加载您需要拦截的页面。享受!
