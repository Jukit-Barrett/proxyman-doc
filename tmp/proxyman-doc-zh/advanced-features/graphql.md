# GraphQL

# #1.使用调试工具处理GraphQL请求

在Proxyman 2.27.0中，我们可以通过指定GraphQL查询名称来对GraphQL请求使用调试工具。

GraphQL QueryName的匹配适用于断点，映射本地，映射远程，阻止列表，允许列表和脚本工具。

#### 如何使用

1.打开调试工具 (如断点)
2.创建新规则
3.点击使用 “通配符下拉”-> 高级-> 检查GraphQL QueryName。
4.输入GraphQL QueryName

通过这种方式，调试工具将首先匹配原始匹配规则，然后匹配GraphQL QueryName。

![启用GraphQL QueryName](图像/Screen_Shot_2021-05-26_at_15_46_13_04a0690f.png)

![指定GraphQL QueryName](图像/Screen_Shot_2021-05-26_at_15_48_17_3e091744.png)

{% 提示样式 = "info" %}
从构建3.0.0开始，当我们创建调试工具规则时，Proxyman会自动填充GraphQL查询名称。
{% endhint %}

# #2.GraphQL更漂亮

从Proxyman 2.33.0，Proxyman可以美化/美化GraphQL的查询值。为此，请打开工具菜单-> 自定义预览器选项卡-> 检查GraphQL复选框。

![美化GraphQL查询] (图片/Screen_Shot_2021-09-11_at_15_58_08_e0517e22.png)

# #3.在主表视图上显示GraphQL查询名称

可以提取并显示查询名称。请右键单击列标题并启用它。

![来自GrapQL请求的查询名称] (图像/Screen_Shot_2021-03-13_at_16_20_42_779ba000.png)

{% content-ref url = "../basic-features/custom-header-column" %}
[自定义标题列](https://docs.proxyman.com /基本功能/自定义标题列)
{% endcontent-ref %}

# #4.调试GraphQL请求 (legacy-proxyman 2.26.0及以下版本)

GraphQL使用相同的URL来查询来自服务器的不同响应，当前的调试工具 (例如Map Local，Breakpoint，Map Remote) 不能很好地工作。

但是，通过使用脚本工具，我们可以轻松实现:

* 响应的映射本地依赖于QueryName
* 操作GraphQL请求和响应的查询，正文，标头

### 使用脚本工具映射本地

我们可以使用脚本工具来映射

1.打开Proxyman
2.在GraphQL域上启用SSL代理
3.确认您可以看到来自您网域的HTTPS请求
4.右键单击流-> 工具-> 脚本以使用给定的URL创建脚本
5.导入本地文件: 点击更多按钮-> 导入JSON或其他文件-> 然后选择您的文件
6.使用以下脚本向您展示了如何使用QueryName = "user" 将本地文件设置为GraphQL请求

'''javascript
// 从更多按钮导入文件-> 导入JSON或其他文件
const file = require("@ users/B02D96D5.default_message_32E64A5B.json");

函数onRequest(context，url，request) {

// 1.从请求中提取queryName
var queryName = request.body.query.match(/\ S +/gi)[1].split('(').shift();

// 或提取operationName
var operationName = request.body.operationName

// 2.保存到sharedState
sharedState.queryName = queryName
sharedState.operationName = operationName

// 完成
退货请求；
}

函数onResponse (上下文，url，请求，响应) {

// 3.检查它是否是我们需要映射的请求
if (sharedState.queryName = = "user") {

// 4.通过操作按钮-> 导入导入本地文件
// 获取本地JSON文件并将其设置为body (如Map local)
response.headers["Content-Type"] = "application/json";
response.body = 文件；
}

// 完成
返回响应；
}
'''

### 操作标题，查询，正文

1.使用相同的代码并更改queryName
2.请使用 [剪辑代码](https://docs.proxyman.com/scripting/ 代码片段-代码 #2-common-on-request-and-response) 更改值
