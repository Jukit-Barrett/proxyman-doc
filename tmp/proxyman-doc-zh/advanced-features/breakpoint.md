# 断点

### 1.什么事？

断点是一个方便的工具，可帮助开发人员快速编辑请求和响应的内容。

可以在 ** 请求 ** 或 ** 响应 ** 上设置断点。

![](图片/Screen_Shot_2020-08-12_at_11.39.46_9d48138b.png)

{% 提示样式 = "info" %}
如果你使用 [亚特兰蒂斯框架](https://docs.proxyman.com/atlantis/ 亚特兰蒂斯-for-ios)，你不能使用断点。请考虑使用普通代理。
{% endhint %}

### 2.主要特点

断点工具允许开发人员停止正在进行的请求或传入的响应以修改其数据。

* 修改请求URL，包括方案，主机，路径，端口，HTTP方法 (在Proxyman 2.35.4 + 上可用)
* 修改请求/响应的HTTP头
* 从请求中修改查询或表单条目。
* 修改授权/Cookie/设置Cookie头。
* 修改请求/响应的HTTP主体
* 更改响应HTTP状态代码。

![响应上的断点] (图像/Screen_Shot_2021-08-25_at_11.12.06_aef8b5d5.png)

![请求URL上的断点 (方案、主机、端口、路径和查询)](图像/Screen_Shot_2021-12-20_at_15_06_05_a705e09b.png)

#### 断点操作

| 动作 | 含义 |
| ------- | ----------------------------------------------------- |
| 取消断点并继续请求/响应 |
| Abort | 中止连接并返回503状态代码 |
| 执行 | 使用新更改发出请求/响应 |

{% 提示样式 = "info" %}
查看断点教程: [在iOS应用程序上拦截和编辑请求/响应的断点](https:// proxyman.io/blog/2019/09/Use-Breakpoint-to-intercept-and-edit-request-response-on-iOS-app.html)
{% endhint %}

### 3.带有原始消息的断点

从版本3.1.0开始，我们可以使用原始消息修改请求/响应。

\[WIP]

### 4.断点由脚本工具 â œ…

如果你想以自动的方式做断点，你应该使用 [脚本](https://docs.proxyman.com/scripting/script# 1-whats-it) 工具，你可以实现与断点相同的结果，但是通过编写Javascript代码以灵活的方式。

请查看此 [代码片段](https://docs.proxyman.com/scripting/ 代码片段-代码 #2-common-on-request-and-response) 以了解如何使用脚本断点。

### 5.断点与GraphQL请求

从Proxyman 2.27.0 +，断点可以通过特定的QueryName处理GraphQL请求。请查看以下GraphQL文档。

{% content-ref url = "graphql" %}
[graphql](https://docs.proxyman.com /高级功能/graphql)
{% endcontent-ref %}

### 6.如何使用

您可以通过以下方式简单地创建一个断点规则:

1.右键单击请求-> 工具-> 断点
2. Proxyman将打开一个断点窗口并填充匹配规则
3.选择请求或响应或两者的断点。
4.单击 “添加” 创建规则。
5.尝试再次发送请求-> Proxyman将打开一个断点，您可以修改数据。
6.单击执行按钮发送请求/响应。
