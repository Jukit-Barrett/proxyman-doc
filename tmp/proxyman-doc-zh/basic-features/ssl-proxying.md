# SSL代理

# #1.SSL代理列表

Proxyman应解密其SSL连接的域或应用程序的列表。它使用户能够以纯文本检查HTTPS请求/响应。

### 包含列表和排除列表

您可以定义规则:

* ** 包含列表 **: 拦截来自应用程序/域的流量，如果它在包含列表中
* ** 排除列表 **: 忽略来自排除列表中的应用程序/域的所有流量

![SSL代理列表](images/ssl_proxying_8759e4d3.png)

{% 提示样式 = "info" %}
⌘ 提出快速打开SSL代理列表。
{% endhint %}

### 应用程序/域/通配符

Proxyman支持多种格式来定义规则:

* ** 由应用程序 **: 拦截从这个应用程序的所有流量
* ** 按域 **: 拦截来自该域的所有流量
* ** 通配符 **: 如果它匹配通配符正则表达式

对于示例:

| 通配符 | 描述 |
| --------------------------- | ---------------------------------------------------------- |
| \ * | 解密所有HTTPS流量 |
| \ * .domain.com，\ * .apple.com | 例如v1.domain.com，data.domain.com，health.apple.com，... |
| v？.domain.com | 例如v1.domain.com，v2.domain.com，... |

{% 提示样式 = "info" %}
在拦截任何HTTPS请求之前，必须设置Proxyman证书。您可以按照 [macOS设置指南](https://docs.proxyman.com /调试设备/macos) 正确安装和信任证书。
{% endhint %}

### 如何在特定域或应用程序上启用SSL代理

* 右键单击左侧面板上的应用程序或域-> 启用SSL代理

<figure><img src = "images/domain_65fe25fd.jpeg" alt = ""><figcaption><p> 将域名添加到SSL代理列表 </p></figcaption></figure>

* 右键单击主表上的请求-> 启用SSL代理
* 选择请求并在响应面板上启用SSL代理。

<figure><img src = "images/2_e3fabb78.jpeg" alt = ""><figcaption><p> 启用整个应用或单个域 </p></figcaption></figure>
