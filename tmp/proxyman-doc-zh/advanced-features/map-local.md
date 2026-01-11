# Map Local (File)

# #1.什么事？

使用Map Local工具，您可以将本地文件的内容用作对请求的HTTP响应。

{% 提示样式 = "info" %}
您可以使用脚本工具 ([Snippet Code](https://docs.proxyman.com/scripting/ snippet-code # Map-Local-与-GraphQL)) 为 ** graphql ** 执行map local

您可以将 ** 本地地图与断点 ** 结合使用，以动态修改内容 (2.16.0 +)
{% endhint %}

# #2.好处

* 使用状态代码，标头和正文定义响应-> 模拟给定的请求-> 轻松测试某些边缘情况，而无需等待服务器的更新。
* ** 使用本地文件模拟假API **: 对于开发人员来说，试用不在生产环境中的测试API非常有用。

![定义状态代码、标题和正文] (图像/Screen_Shot_2021-08-09_at_11_28_40_0c519f0e.png)

### 带有HTTP消息

1.在主表上右键单击您的请求-> 工具-> 地图本地-> Proxyman将自动创建具有当前响应的新规则
2.随意更改状态代码，标头和JSON正文
3.完成
4.重新发送您的请求-> 新的响应被映射。

### 与本地文件

* 单击 “选择本地文件” 按钮并选择任何文件。支持: 文本，JSON，二进制，图像

### 带 \<FILE \ _url> 标志

* 映射到给定文件并能够提供状态代码和响应标头很有用。
* 使用JSON，文本，二进制，图像等
* 确保提供 'Content-type' 标头，以便您的客户端可以正常工作

'''json
HTTP/1.1 200好
Content-Type: application/json

<FILE_URL = "~/Desktop/myjson.json">
'''

# #2.如何使用

1.右键单击请求 (已经有响应) -> 工具-> 映射本地。Proxyman将使用当前响应正文创建一个规则 (该文件存储在您的桌面文件夹中)
2.我们可以直接改变响应体。
3.提出请求并观察新的响应主体。

<figure><img src = "images/Screen_Shot_2022-09-23_at_13_23_11_b2a97441.jpg" alt = ""><figcaption><p> 创建具有curernt响应的本地地图 </p></figcaption></figure>

# #3.使用GraphQL请求映射本地

从Proxyman 2.27.0 +，Map Local可以通过特定的QueryName处理GraphQL请求。请查看以下GraphQL文档。

{% content-ref url = "graphql" %}
[graphql](https://docs.proxyman.com /高级功能/graphql)
{% endcontent-ref %}

# #4.使用脚本工具映射本地地图 â œ…

如果你想做地图本地与 ** 复杂的规则，** 你可以看看 [脚本](https://docs.proxyman.com/scripting/script# 1-whats-it)，因为它更容易实现相同的结果。

请查看这些 [代码片段](https://docs.proxyman.com/scripting/ 代码片段-代码 #2-common-on-request-and-response) 以了解如何使用Javascript代码映射本地文件。
