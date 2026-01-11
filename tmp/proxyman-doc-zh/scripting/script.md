# 脚本

### 1.什么事？

Proxyman提供了一个脚本功能，开发人员可以编写JS代码以灵活的方式操作请求/响应。

### 2.好处

* 通过JS代码实现地图本地/地图远程/断点。** 快100倍 **
* 更改 ** 请求内容 **，包括域、Host、Scheme、Port、Path、HTTP方法、HTTP Headers、Query、Body (Encoded-Form、JSON、plain-text)
* 更改 ** 响应内容 **，包括HTTP状态代码，HTTP标头和正文 (JSON，编码形式，纯文本，二进制...)
* 为常见任务提供大量内置插件和库，例如哈希，编码/解码，JSON文本转换器，美化，...
* 能够 ** 编写自己的JS插件或库 **
* 旨在取代重写GUI工具从查尔斯代理
* 使用 [ShareState或环境变量](https://docs.proxyman.com/scripting/ 环境变量) 在每个脚本或当前会话之间分配和接收共享状态

<figure><img src = "images/Screenshot_2024-01-07_at_14.52.47_b7443033.jpg" alt = ""><figcaption><p> 脚本工具 </p></figcaption></figure>

{% content-ref url = "snippet-code" %}
[代码段-代码](https://docs.proxyman.com/scripting/ 代码段-代码)
{% endcontent-ref %}

### 3.如何使用它？

您可以通过以下方式访问脚本工具:

* 脚本菜单-> 脚本列表 (⌘ ⌘ i)
* 打开菜单上下文从右键点击流-> 工具-> 脚本

请查看 [代码片段](https://docs.proxyman.com/scripting/ 代码片段-代码) 以查看脚本工具的代码片段JS代码的集合。

### 4.使用GraphQL请求编写脚本

从Proxyman 2.27.0 + 开始，脚本工具可以处理特定QueryName的GraphQL请求。请查看以下GraphQL文档。

{% content-ref url = "../advanced-features/graphql" %}
[graphql](https://docs.proxyman.com /高级功能/graphql)
{% endcontent-ref %}

### 使用Websocket 4.1脚本

从Proxyman v6.2.0或更高版本，可以使用脚本

* 修改Websocket请求URL和标头
* 修改Websocket响应头
*❌无法修改websocket消息。仅支持URL和标头。
* 请参阅此代码片段。

### 5.示例

以下指南将向您展示如何编写JS代码以将请求域从生产更改为本地主机并更改响应正文

1.确保在创建脚本之前为此域启用了SSL。
2.打开脚本工具并创建一个新的脚本条目 (⌘ n)。您可以右键单击请求-> 工具-> 脚本 => Proxyman也将创建一个脚本
3.给出名称并定义匹配规则。
4.例如: ** Name ** = 在Localhost端点上测试，** URL ** =<https:// proxyman.io>
5.在 ** 请求 ** 和 ** 响应 ** 复选框 ** 上启用运行脚本 **
6.开始为 'onRequest' 函数编写JS代码

** onRequest(context, url, request) {}**

'''javascript
// 导入UUID插件
const { uuidv4 } = require("@ addons/UUID.js");

函数onRequest(context，url，request) {
// 打印日志
console.log (请求)；

// 更改生产域-> 本地主机
request.method = "GET";
request.scheme = "http";
request.host = "localhost";
request.port = 8000；

// 添加新标题
request.headers["X-New-Header"] = "Hello From Scripting feature";
request.headers["UUID"] = uuidv4(); // 生成随机UUIDv4
delete request.headers["Key-Need-Delete"];

// 更新或添加新查询
request.queries["name"] = "Proxyman";

// 更新正文
var body = request.body;
body["name"] = "Proxyman";
request.body = body;

// 或使用本地文件映射正文 (Proxyman 2.25.0 +)
// request.bodyFilePath = "~/Desktop/mockdata.json";

// 完成
退货请求；
}
'''

### onRequest() 对象格式

“上下文” 、 “url” 和 “请求” 对象的定义如下:

'''javascript
// context (readonly)
{
"scriptName": "<String> 您的脚本名称"，
"matchingRule": "<String> 您的匹配规则"，
"matchingMethod": "<String> 方法"，
"isEnableOnRequest": "Bool",
"isEnableOnResponse": "Bool",
"filePath": "<String> 脚本路径"，
“流量”: {// 从2.16.0 + 可用
"serverPort": "443"，
"serverIpAddress": "104.18.230.83",
"clientIpAddress": "192.168.0.102",
"remoteDeviceName": "iPhone XR",
"remoteDeviceIP": "192.168.0.102",
"id": "51",
"clientPath": null,
"clientPort": "51494"，
"clientName": null,
"mapRemoteOriginalURL": "<String> 地图远程修改前的原始URL (可空)"
},
}

// url (只读)
url: String // => 显示完整的URL

// 请求
{
"method": "<String> HTTP Method. Accept string method. Ex: GET, POST, ...",
"scheme": "<String> 接受http或https"，
"host": "<String> 请求的主机。例如: api.proxyman.io，localhost，..."，
"path": "<String>: URL的路径。Ex: /v1/data"，
"port": "<Int> 接受int端口号。例如: 443，8080，.."，
"queries": "<[String: Any]> 一个JS对象 (字典) 包含查询的键值"，
"headers": "<[String: Any]> JS对象 (字典) 包含标头的键值"，
“body”: “取决于Content-Type头。它可能是JSON和form的字典，纯文本或Uint8Array”，
"bodyFilePath": "<String><Optional> 使用本地文件设置正文。请参阅代码段代码页中的示例"
"rawBody": "<Readonly>: 原始正文字符串或Uint8Array"，
"preserveHostHeader": "<Bool> 保留主机"，
"isURLEncoding": "<Bool> 确定Proxyman在构造最终URL时是否将执行URLEncoding。默认值为True"
}

'''

{% 提示样式 = "info" %}
您可以更改请求obj的任何值，“rawbody” 除外
{% endhint %}

{% 提示样式 = "info" %}
如果由于标头中的Content-Type错误而导致 ** body ** 变量的格式无效。请考虑使用 ** rawBody ** 并手动解析字符串。
{% endhint %}

Content-type标头上的 “request.Body” 答复的类型。

| Content-Type标头 | request.body |
| ----------------------------------------------------------------------------------- | ----------------- |
| 应用程序/json或JSON系列 | Javascript对象 |
| application/x-www-form-urlencoded | Javascript对象 |
| 纯文本或基于文本的内容类型，例如: application/js，text/css，text/html，... | String |
| 其余: 二进制数据 (application/zip，application/octet-stream) | Uint8Array |

从剪下的代码页中查看常见的JS代码

{% content-ref url = "snippet-code" %}
[代码段-代码](https://docs.proxyman.com/scripting/ 代码段-代码)
{% endcontent-ref %}

7 \。开始在 'onResponse' 函数上编写代码

'''javascript
函数onResponse (上下文，url，请求，响应) {
console.log (响应)；

// 更新或添加新标题
response.headers["Content-Type"] = "application/json";

// 更新状态代码
response.statusCode = 500；

// 更新正文
var body = response.body;
body["new-key"] = "Proxyman";
response.body = body;

// 或使用本地文件映射正文 (Proxyman 2.25.0 +)
// response.bodyFilePath = "~/Desktop/mockdata.json";

// 完成
返回响应；
}
'''

### onResponse() 对象格式

“Context” 、 “url” 、 “request” 和 “response” 对象的定义如下:

'''javascript
// context (readonly): 与onRequest相同

// url (readonly): 与onRequest相同

// request (readonly): 与onRequest相同

// 响应
{
"statusCode": "<Int> 状态码。例如: 200，400，404，..."，
"httpVersion": "<String><Readonly> HTTP版本"，
"statusPhrase": "<String><Readonly> HTTP状态短语.Ex未找到，好，..."，
"headers": "<[String: Any]> JS对象 (字典) 包含标头的键值"，
“body”: “取决于Content-Type头。它可能是JSON和form的字典，明文或Uint8Array”，
"rawBody": "<Readonly>: 原始正文字符串或Uint8Array"，
"bodyFilePath": "<String><Optional> 使用本地文件设置正文。请参阅代码段代码页中的示例"
}
'''

{% 提示样式 = "info" %}
您可以从响应Obj更改 “statuscode”，“headers” 和 “body”
{% endhint %}

{% 提示样式 = "info" %}
如果由于标头中的Content-Type错误而导致 ** body ** 变量的格式无效。请考虑使用 ** rawBody ** 并手动解析字符串。
{% endhint %}

Content-type标头上的 “response.Body” 答复的类型

| Content-Type标头 | request.body |
| ----------------------------------------------------------------------------------- | ----------------- |
| 应用程序/json或JSON系列 | Javascript对象 |
| application/x-www-form-urlencoded | Javascript对象 |
| 纯文本或基于文本的内容类型，例如: application/js，text/css，text/html，... | String |
| 其余 (application/zip，application/octet-stream) | Uint8Array |

{% 提示样式 = "info" %}
您必须在 'onRequest' 和 'onResponse' 函数中返回 'request' 和 'response' 对象
{% endhint %}

### 6.内置插件和库

Proxyman提供了大量的插件和库，帮助您实现常见的任务: 散列，编码/解码，...

{% content-ref url = "addons" %}
[插件](https://docs.proxyman.com/scripting/addons)
{% endcontent-ref %}

{% content-ref url = "内置js库" %}
[内置js库](https://docs.proxyman.com/scripting/ 内置js库)
{% endcontent-ref %}

{% content-ref url = "snippet-code" %}
[代码段-代码](https://docs.proxyman.com/scripting/ 代码段-代码)
{% endcontent-ref %}

### 7.调试JS错误

在某些情况下，由于语法错误，无效代码，...，您可能会遇到Javascript错误。您可以通过查看控制台上的错误消息或使用 “console.log()” 进行调试。

### 8.使用脚本作为模拟API

从Proxyman 2.32.0，我们可以使用脚本工具作为模拟API。这意味着你的请求永远不会击中服务器，你必须定义一个响应体。此行为与Map Local相同。

当实际的Restful API尚不可用时，此功能非常有用。您可以在本地定义和测试它。

要启用模拟API，请执行以下操作:

1.打开脚本工具-> 选择脚本
2.启用运行为模拟API复选框。

![启用模拟API](图像/Screen_Shot_2021-09-17_at_14_59_30_36378ed8.png)

然后你可以像往常一样定义一个响应:

'''javascript
函数onResponse (上下文，url，请求，响应) {

// 初始化新主体
var body = {};
body["new-key"] = "Proxyman";
response.body = body;

// 或从文件映射
// response.bodyFilePath = "~/Desktop/myfile.json"

// 完成
返回响应；
}
'''

### 9.备注

* 您必须在 'onRequest' 和 'onResponse' 函数中返回 'request' 和 'response' 对象。
* ** Proxyman 4.16.0或更高版本 **: Proxyman现在将二进制数据转换为 ** Uint8Array **
* Proxyman 4.15.0或更早版本: 由于Javascript没有数据对象类型，因此数据主体将转换为Javascript中的 ** Base64编码字符串 **。要将Uint8Array、blob或ArrayBuffer传递到正文，请确保转换为 ** Base64编码的字符串。**
