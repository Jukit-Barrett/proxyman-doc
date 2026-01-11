# Map Remote

# #1.什么事？

Map Remote (** ⌘ r **) 将帮助开发人员根据配置的规则将HTTP请求的位置更改为新的目标服务器，因此HTTP响应是透明地从您的客户端提供的。

Map Remote还支持从HTTP到HTTPS的映射，反之亦然

![映射远程规则] (图像/Screen_Shot_2020-07-19_at_10.17.34_7449acb1.png)

{% 提示样式 = "info" %}
从HTTP <-> HTTPS映射时，请查看常见的 [Map Remote Config](#7.-common-usages)。
{% endhint %}

{% 提示样式 = "info" %}
从Proxyman 4.3.0: 地图远程支持Websocket和安全Websocket。
{% endhint %}

# #2.好处

* 在某些端点上的开发网站上使用生产端点，而无需更改源代码
* 在您的生产网站上使用开发端点
* 更改某些请求的url到不同的目的地
* 能够替换请求组件，例如协议，主机，端口，路径或即时查询

{% 提示样式 = "info" %}
为了提高您的工作效率，您可以使用 [脚本功能](https://docs.proxyman.com/scripting/script# 1-whats-it)，它允许您通过编写简单的Javascript代码来实现与Map Remote相同的结果

例如，[将生产更改为本地主机服务器的代码片段](https://docs.proxyman.com/scripting/ 代码片段-代码 # change-request-destination-schema-host-port-path)
{% endhint %}

# #3.使用GraphQL请求映射远程

从Proxyman 2.27.0 +，Map Remote可以通过特定的QueryName处理GraphQL请求。请查看以下GraphQL文档。

{% content-ref url = "graphql" %}
[graphql](https://docs.proxyman.com /高级功能/graphql)
{% endcontent-ref %}

# #4.使用脚本作为地图远程✅

如果您很难设置复杂的地图远程规则，则可以使用 [脚本工具](https://docs.proxyman.com/scripting/script# 1-whats-it) 轻松完成。

请查看 [地图远程代码片段](https://docs.proxyman.com/scripting/ 代码片段-代码 # 8-map-remote-with-scripting)，了解如何使用脚本实现与地图远程相同的结果。

例如，通过脚本执行以下操作很简单:

* 将v1映射到v2端点
* 将生产映射到本地主机
* 将本地主机映射到生产
*...

# #5.匹配规则

{% 提示样式 = "info" %}
Proxyman支持 [正则表达式](https://developer.apple.com/documentation/foundation/nsregularexpression# 1965590) 和2.3.0版本的通配符。[查看这里](https://docs.proxyman.com /基本功能/正则表达式)
{% endhint %}

我们可以通过使用 [通配符或正则表达式](https://docs.proxyman.com /基本特征/正则表达式) 来定义匹配规则。

对于匹配的请求，Proxyman尝试:

* 替换协议、主机、端口、路径和查询 (如果可用)
* 如果组件为空，则不会更改匹配请求的组件

![](图片/Screen_Shot_2020-07-19_at_10.17.44_1ca66054.png)

{% 提示样式 = "info" %}

* 将文本字段留空，以使其与匹配的请求保持不变
* 通配符不允许
{% endhint %}

### 调试

要确定哪些Map Remote与您的URL匹配，您可以打开请求-> 摘要选项卡:

1.选择您的请求
2.摘要选项卡-> 调试工具
3.检查地图URL

<figure><img src = "images/CleanShot_2023-02-15_at_09.23.58_2x_9e3ba336.jpg" alt = ""><figcaption><p> 如何调试地图远程 </p></figcaption></figure>

### 保留主机标头

默认情况下，Proxyman尝试覆盖主机标头以与远程映射中的新主机匹配。成功提出请求至关重要。

如果要保留原始主机标头，请在创建新条目时选中 “保留主机标头” 复选框。Proxyman将保留主机值。

# #6.如何使用

* 右键单击选定的请求-> 工具-> 地图远程: Proxyman将从选定的请求中填写必要的数据

![创建地图遥控器] (图像/Screen_Shot_2020-04-25_at_16.18.59_f096341f.png)

# #7.常用用法

### 7.1将本地主机 (HTTP) 映射到生产 (HTTPS)

<figure><img src = "images/Screenshot_2023-02-15_at_09.34.02_7971930f.png" alt = ""><figcaption><p> 地图远程配置 </p></figcaption></figure>

** 结果: **

| 原始URL | 到URL |
| ------------------------------------------------------ | ---------------------------------------------------- |
| <http:// localhost:3000> | <https:// proxyman.io> |
| <http:// localhost:3000/定价> | <https:// proxyman.io/定价> |
| <http:// localhost:3000/v1/user？id = 123 \\& name = proxyman> | <https:// proxyman.io/v1/user？id = 123 \\& name = proxyman> |
| ** POST ** <http:// localhost:3000/login> | ** POST ** <https:// proxyman.io/login> |

### 7.2将生产 (HTTPS) 映射到本地主机 (HTTP)

<figure><img src = "images/Screenshot_2023-02-15_at_09.39.50_eeb43a98.png" alt = ""><figcaption><p> 地图远程配置 </p></figcaption></figure>

| 原始URL | 到URL |
| ---------------------------------------------------- | ------------------------------------------------------ |
| <https:// proxyman.io> | <http:// localhost:3000> |
| <https:// proxyman.io/v1/user？id = 123 \\& name = proxyman> | <http:// localhost:3000/v1/user？id = 123 \\& name = proxyman> |
| ** POST ** <https:// proxyman.io/login> | ** POST ** <http:// localhost:3000/login> |

### 7.3将某个URL映射到另一个主机

* 规则: **<https:// proxyman.io/v1/user>** (例如)
* 选择 ** 任意 ** 和 ** 通配符 **
* ** 取消检查包括此URL的所有子路径: ** 取消检查意味着它不映射其他子路径

** 映射到: **

* 协议: ** https **
* 主机: 新主机 (例如staging.proxyman.io)
* 端口: ** 443 ** (您的本地端口)
* 保留路径和查询为空

** 结果: **

| 原始URL | 到URL |
| ---------------------------------------------------- | ------------------------------------------------------------ |
| <https:// proxyman.io> (不映射规则) |
| <https:// proxyman.io/v2/setting> (不映射规则) |
| <https:// proxyman.io/v1/user？id = 123 \\& name = proxyman> | <https:// staging.proxyman.io/v1/user？id = 123 \\& name = proxyman> |

### 7.4将Websocket从本地主机映射到生产

<figure><img src = "images/Screenshot_2023-02-15_at_09.29.05_dfab043a.png" alt = ""><figcaption><p> 地图远程配置 </p></figcaption></figure>

| 原始URL | 到URL |
| ------------------------------ | ------------------------------------ |
| ws \:// 本地主机: 4000 | wss \:// ws.postman-echo.com |
| ws \:// localhost:4000/websocket | wss \:// ws.postman-echo.com/websocket |

### 7.5将Websocket从生产映射到本地主机

<figure><img src = "images/Screenshot_2023-02-15_at_09.38.19_8919a042.png" alt = ""><figcaption><p> 地图远程配置 </p></figcaption></figure>

| 原始URL | 到URL |
| ------------------------------------ | ------------------------------ |
| wss \:// ws.postman-echo.com | ws \:// 本地主机: 3000 |
| wss \:// ws.postman-echo.com/websocket | ws \:// 本地主机: 3000/websocket |
