# 代码片段

# #1.什么事？

脚本工具的Javascript代码段集合。

{% 提示样式 = "info" %}
找不到您要查找的代码段？

请在 < https://github.com/ProxymanApp/Proxyman > 开票，我们会回来帮助你⭐️
{% endhint %}

# #2.常见的请求和响应

* [更新请求或响应的标头](# http-header)
* [更新请求查询](# Request-Query)
* [更新URLEncoded表单请求正文](# urlencoded-Form-Body)
* [更新JSON请求或响应正文](# json-body)
* [将本地文件映射到响应的身体，如地图本地工具](# map-a-local-file-to-responses-body-like-map-local-tool-proxyman-2.25.0 +)
* [更改请求方案，主机，端口，路径](# Change-Request-destination-Scheme-Host-Port-Path)
* [HTTP到HTTPS](# http到https)
* [HTTPS到HTTP](# http-to-https-1)
* [更改请求方法](# Change-response-http-status-code)
* [更改响应状态代码](# Change-Response-http-Status-Code)
* [日志记录](# Logging)
* [使用JSON文件作为请求或响应的主体](# use-json-fie-as-body-of-Request-or-Response)
* [使用多个JSON文件](# Use-multiple-json-files)
* [用于GraphQL的本地地图](# Map-Local-与graphql一起)
* [在请求/响应正文中使用ArrayBuffer](# Use-arraybuffer-in-Request-Response-Body)
* [保留主机](# Preserve-the-Host)
* [用颜色注释和突出显示](# 用颜色注释和突出显示)
* [中止 (关闭) 请求/响应连接 (如块列表工具)](# Abort-the-request-response-Like-Block-List-Tool)

# #3.插件

* [Base64编码/解码或atob/btoa](# use-base64-addon)
* [散列插件 (MD5，SHA1，SHA256，SHA512)](# use-hashing-addon-md-5-sha-1-sha-256-sha-512)
* [UUIDv4发生器](# use-uuid-v4-addon)
* [放气/充气或GZip/解压缩](# 放气-充气-和-gzip-解压缩)
* [JWT解码](# jwt解码)

# #4.正则表达式

* [检查给定的字符串是否只包含数字](# regex)
* [正则表达式获取URL的方案，主机，端口，路径和查询](# Regex-to-get-the-scheme-host-Port-Path-and-Query-of-the-url)

# #5.导入/导出文件

* [导入JSON文件](# json)
* [导入二进制数据 (图像)](# 二进制文件)
* [导入基于文本的文件 (css，html，js...)](# 基于文本的文件)
* [不使用 “导入工具” 导入文件](# 导入文件-不使用导入工具)
* [写入/导出到本地文件](# Write-Export-to-a-local-file)
* [检查文件是否存在](# Check-if-the-first-exist)
* [读取本地文件](# Read-a-File)
* [使用响应作为模拟API](# use-as-mock-api)

# #6.杂项

* [旁通CORS](# 旁通cors)
* [向请求或响应注入标头](# Inject-Header-to-Request-Response)
* [带有sleep() 功能的响应延迟](# Response-delay-与-sleep-function)

# #7.加密/解密

* [AES](# aes-加密-解密)
* [DES](# des-加密-解密)

# #8.使用脚本映射远程

* [映射v1到v2端点](# map-v1-to-v2-endpoints)
* [映射本地主机到生产](# 映射本地主机到生产)
* [映射生产到本地主机](# 映射生产到本地主机)

# #9.使异步/等待HTTP请求 (macOS)

* [带查询的GET请求](# get-Request-与查询)
* [带JSON正文的POST请求](# post-Request-与json-body)
* [使用application/x-www-form-urlencoded的POST请求](# post-Request-与application-x-www-form-urlencoded-正文)
* [PUT / PATCH / DELETE Request](# put-patch-delete-request)

# #9.1。使异步/等待HTTP请求 (Windows/Linux)

* [使用Axios库发出请求](# 制作-异步-等待-http-请求-windows-linux)

# #10.URL和URLSearchParams

* [URL和URLSearchParams](# url-and-urlsearchparams)

# #11.访问环境变量

* [手动读取系统环境变量](# reload-system-environment-variables)

# # Websocket

* [更改Websocket URL，Headers](# Change-websocket-url-requests-response-header)

# # HTTP头

#### 添加/更新: 请求或响应头

'''javascript
函数onRequest(context，url，request) {
// 添加或更新请求头
request.headers["X-Proxyman-Key"] = "My-Value";
request.headers.name = "Proxyman"；
退货请求；
}

函数onResponse (上下文，url，请求，响应) {
// 添加或更新响应头
response.headers["X-Proxyman-Key"] = "My-Value";
response.headers.id = 100；
返回响应；
}
'''

#### Delete: 请求或响应头

'''javascript
函数onRequest(context，url，request) {
删除request.headers["x-proxyman-key"]；
退货请求；
}

函数onResponse (上下文，url，请求，响应) {
删除response.headers["x-proxyman-key"]；
返回响应；
}

'''

# # 请求查询

#### 添加/更新

'''javascript
函数onRequest(context，url，request) {
request.queries["name"] = "Proxyman";
request.queries["platform"] = "macOS";
// => http:// proxyman.io?name = Proxyman & platform = macOS
退货请求；
}
'''

#### 删除

'''javascript
函数onRequest(context，url，request) {
删除请求。查询 ["name"]；
delete request.queries["platform"];
退货请求；
}

'''

# # URLEncoded表单正文

#### 添加/更新

'''javascript
函数onRequest(context，url，request) {
// 确保响应头是application/x-www-form-urlencoded
// Content-Type: application/x-www-form-urlencoded
var formBody = request.body;

formBody["name"] = "Proxyman";
formBody["flatform"] = "macOS";

request.body = formBody; // => name = Proxyman & platform = macOS
退货请求；
}

'''

#### 删除

'''javascript
函数onRequest(context，url，request) {
// Content-Type: application/x-www-form-urlencoded
var formBody = request.body;

删除formBody["name"]；
删除formBody["flatform"]；

request.body = formBody;
退货请求；
}

'''

# # 更改请求目标 (方案，主机，端口，路径)

'''javascript
函数onRequest(context，url，request) {
request.scheme = "http";
request.host = "proxyman.de v";
request.port = 9090；
request.path = "v1/data/user";
退货请求；
}
'''

# # HTTP到HTTPS

'''javascript
函数onRequest(context，url，request) {
request.scheme = "http";
request.port = 80; // 不要忘记覆盖端口
退货请求；
}
'''

# # HTTPS到HTTP

'''javascript
函数onRequest(context，url，request) {
request.scheme = "https";
request.port = 443; // 不要忘记覆盖端口
退货请求；
}
'''

# # 更改HTTP请求方法

'''javascript
函数onRequest(context，url，request) {
request.method = "POST";
退货请求；
}
'''

# # 更改响应HTTP状态码

'''javascript
函数onResponse (上下文，url，请求，响应) {
response.statusCode = 404；
返回响应；
}
'''

# # JSON正文

#### 根据请求

'''javascript
函数onRequest(context，url，request) {
// 设置JSON内容
request.headers["Content-Type"] = "application/json";

// Get请求正文
var jsonBody = request.body;

// 修改数据
jsonBody["name"] = "Proxyman";
jsonBody["flatform"] = "macOS";
jsonBody["info"] = {
"网站": "proxyman.io"，
"地区": "地球"
};
// 重新设置
request.body = jsonBody;
退货请求；
}
'''

#### 响应

'''javascript
函数onResponse (上下文，url，请求，响应) {
// 设置JSON内容
response.headers["Content-Type"] = "application/json";

// Get请求正文
var jsonBody = response.body;

// 修改数据
jsonBody["name"] = "Proxyman";
jsonBody["flatform"] = "macOS";
jsonBody["info"] = {
"网站": "proxyman.io"，
"地区": "地球"
};
// 重新设置
response.body = jsonBody;
返回响应；
}

'''

#### 将本地文件映射到响应的主体，如映射本地工具 (Proxyman 2.25.0 +)

这是一种通过使用 “bodyfilepath” 属性直接将本地文件设置为正文的便捷方法

'''javascript
// 对于请求
request.bodyFilePath = "~/Desktop/image.png";

// 用于响应
response.bodyFilePath = "~/Desktop/image.png";
'''

'''javascript
函数onResponse (上下文，url，请求，响应) {

response.headers["Content-Type"] = "image/png";
response.bodyFilePath = "~/Desktop/image.png";

// 完成
返回响应；
}
'''

'''javascript
函数onResponse (上下文，url，请求，响应) {

response.headers["Content-Type"] = "application/json";
response.bodyFilePath = "~/Desktop/my_response.json";

// 完成
返回响应；
}
'''

#### 使用JSON文件作为请求或响应的主体

可以使用您的JSON文件并将其设置为请求/响应的主体

请按照这个 [教程](# json)。

#### 使用多个JSON文件

您可以使用IF语句为每个匹配的端点设置不同的主体。

1.按照此 [教程](# json) 了解如何将JSON文件导入脚本
2.使用可以匹配许多端点的通配符或正则表达式模式设置脚本规则。例如 <https:// my-domain.com/v \\>\ *
3.使用 \ 'include ()\' 检查端点是否匹配

'''javascript
const file_1 = require("@ users/myfile_1.json");
const file_2 = require("@ users/myfile_2.json");
const file_3 = require("@ users/myfile_3.json");

函数onResponse (上下文，url，请求，响应) {

// 设置JSON内容
response.headers["Content-Type"] = "application/json";

// 检查
if (url.includes("v1/data")) {
response.body = file_1
} else if (url.includes("v2/login")) {
response.body = 文件 _2
} else if (url.includes("v3/user")) {
response.body = file_3
}

// 完成
返回响应；
}
'''

#### 使用GraphQL映射本地

阅读更多 < https://github.com/ProxymanApp/Proxyman/issues/ 412 # issuecomment-697101594>

'''javascript
// 在此处导入JSON文件
const file = require("@ users/B02D96D5.default_message_32E64A5B.json");

函数onRequest(context，url，request) {

// 1.从请求中提取queryName
var queryName = request.body.query.match(/\ S +/gi)[1].split('(').shift();

// 2.保存到sharedState
sharedState.queryName = queryName

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

#### 在请求/响应正文中使用ArrayBuffer

由于Javascript没有数据对象类型，因此数据主体将转换为Javascript中的 ** Base64编码字符串 **。要将 ** Uint8Array ** 、 ** blob ** 或 ** ArrayBuffer ** 传递到body，请确保转换为 ** Base64编码的字符串 **，并将ContentType设置为 'application/octet-stream'

Proxyman将Base64编码转换为ArrayBuffer，因此客户端将正确接收数据。

'''javascript
// 导入
const { btoa } = require('@ addons/Base64.js');

函数onResponse (上下文，url，请求，响应) {
// 构造ArrayBuffer
const buffer = new ArrayBuffer(256)
const视图 = 新Uint8Array (缓冲区)
for (设i = 0; i < view.length; i ++) {
视图 [i] = i
}

// 将ArrayBuffer转换为Base64String
var newBody = btoa(String.fromCharCode.apply(null, new Uint8Array(buffer)));

// 设置新的身体
response.body = newBody;
response.statusCode = 200
response.headers['Content-Type'] = 'application/octet-stream'

// 完成
返回响应；
}
'''

#### 保留主机

'''javascript
函数onRequest(context，url，request) {
request.preserveHostHeader = true
退货请求
}
'''

#### 注释和用颜色突出显示

使用 “注释” 或 “颜色” 突出显示主表格视图。

'''javascript
函数onRequest(context，url，request) {
request.com = “这是一个请求”
request.color = “红色” // 红色，蓝色，黄色，紫色，灰色，绿色
退货请求
}

函数onResponse (上下文，url，请求，响应) {
response.com = “这是一个回应”
response.color = “黄色” // 红色，蓝色，黄色，紫色，灰色，绿色
返回响应
}
'''

![对颜色和注释使用脚本] (图像/Screen_Shot_2021-08-13_at_09_27_36_98ab01fb.png)

# # 使用require() 导入文件

#### JSON

1.准备一个JSON文件并将其保存到桌面

'''javascript
// myfile.json
{
"name": "Proxyman",
"平台": "macOS"，
"信息": {
"网站": "proxyman.io"，
"地区": "地球"
}
}
'''

2 \。更多-> 导入JSON或其他文件。然后选择您的文件

![](图片/Screen_Shot_2021-04-22_at_10.59.46_187f03dd.png)

3 \。Proxyman会将导入代码添加到脚本的顶部

'''javascript
// ~/Library/Application Support/com.proxyman.NSProxy/users/myfile.json
const file = require("@ users/myfile.json");

函数onResponse (上下文，url，请求，响应) {
// 1.如果需要，将标头设置为JSON
response.headers["Content-Type"] = "application/json";

// 2.将Body设置为导入的文件
response.body = 文件；

返回响应；
}
'''

{% 提示样式 = "info" %}
所选文件将复制到 ** \ ~/Library/Application \ Support/com.proxyman.NSProxy/users ** 文件夹。
{% endhint %}

{% 提示样式 = "info" %}
支持其他格式的文件，如图像，文本，pdf。确保您有正确的 ** 标题内容类型 **
{% endhint %}

#### 二进制文件

1.按照上面的说明 (选择你的二进制文件)
2.将其设置为身体

'''javascript
// ~/Library/Application Support/com.proxyman.NSProxy/users/myscreenshot.png
const文件 = require (“@ users/myscreenshot.png”)；

函数onResponse (上下文，url，请求，响应) {
// 设置标头
response.headers["Content-Type"] = "image/png";

// 设置主体
response.body = 文件；

返回响应；
}
'''

#### 基于文本的文件

1.按照上面的说明 (选择你的二进制文件)
2.将其设置为身体

'''javascript
// ~/Library/Application Support/com.proxyman.NSProxy/users/main.css
const文件 = require("@ users/main.css")；

函数onResponse (上下文，url，请求，响应) {
// 设置标头
response.headers["Content-Type"] = "text/css";

// 设置主体
response.body = 文件；

返回响应；
}
'''

#### 不使用 “导入工具” 导入文件

从Proxyman 2.24.0 +，您可以导入任何文件，而无需使用 “导入文件”。

'''javascript
// 从桌面文件夹导入文件
const file = require("~/Desktop/myfile.json");

函数onResponse (上下文，url，请求，响应) {

// 1.如果需要，将标头设置为JSON
response.headers["Content-Type"] = "application/json";

// 2.将Body设置为导入的文件
response.body = 文件；

返回响应；
}
'''

* 如果文件有 “.js” 作为扩展名 => Proxyman将执行它作为一个JS脚本
* 否则，Proxyman将正常导入

{% 提示样式 = "info" %}
在将脚本导出给同事时，仅包括使用 “导入工具” 导入的文件。
{% endhint %}

#### 用作模拟API

您可以使用脚本作为一个模拟的API通过以下 [指南](https:// docs.proxyman.io/脚本 # 8-use-scripting-as-a-mock-api)。

# # 使用插件

[内置插件的完整列表](https://docs.proxyman.com/scripting/addons)

#### 使用Base64插件

'''javascript
// Base64编码
const { btoa } = require("@ addons/Base64.js")

// 用法:
var text = "HelloWorld";
var encodedText = btoa(text);
'''

'''javascript
// 解码Base64
const { atob } = require("@ addons/Base64.js")

// 用法:
var text = atob("aGVsbG8 =");
'''

#### 使用哈希插件 (MD5，SHA1，SHA256，SHA512)

'''javascript
// 哈希MD5
const { md5 } = require("@ addons/MD5.js")

// 用法:
var hashedText = md5("你好，世界")；
'''

'''javascript
// 哈希SHA1
const { sha1 } = require("@ addons/SHA1.js")

// 用法:
var hashedText = sha1("你好，世界")；
'''

#### 使用UUID-v4插件

'''javascript
// 哈希MD5
const { uuidv4 } = require("@ addons/UUID.js")

// 用法:
var uuid = uuidv4();
'''

# # 放气/充气和GZip/UnGZip

#### 放气/充气

'''javascript
const { inflate, deflate } = require("@ addons/Pako.js")

// 压缩
var input = "从Pako你好，世界!"
var结果 = deflate (输入)；
console.log (结果); // eJzzSM3JyVcIzy/KSVFIK8rPVQhIzM5XVFQEAGsMB/8 =

// 解压
var text = 'eJzzSM3JyVcIzy/KSVFIK8rPVQhIzM5XVFQEAGsMB/8 =';
var rawText = inflate(text);
console.log(rawText); // 从Pako你好，世界!
'''

#### GZip/UnGZip

'''javascript
const { ungzip, gzip } = require("@ addons/Pako.js")

// 压缩
var text = 'HelloWorld';
var结果 = gzip(text)；
console.log (结果); // H4sIAAAAAAAAA/NIzcnJD88vykkBAHkMd3cKAAAA

// 解压
var text = 'H4sIAAAAAAAAA/NIzcnJD88vykkBAHkMd3cKAAAA';
var rawText = ungzip(text);
console.log(rawText); // HelloWorld
'''

#### JWT解码

'''javascript
const { jwtDecode } = require('@ addons/JWTDecode.js');

var text = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c';
var jSONObject = jwtDecode (文本)
'''

# # 日志记录

'''javascript
// 打印obj
const myObj = {};
console.log(myObj);

// obj的打印类型
console.log(typeof(myObj));
'''

# # 正则表达式

#### 仅编号

'''javascript
// 初始化正则表达式
var reg = /^-?\ d * \.?\ d * $/;

if (reg.test (“123123123”)) {
console.log (“匹配”)；
}
'''

#### Regex获取URL的Scheme，Host，Port，Path，Query

'''javascript
函数onRequest(context，url，request) {
console.log(url);

// 获取每个部分
const regex = /^(https?):\/\/([^:\/\ n]+ )(?::( \ d + ))?([^#\ n?]+ )(?:\?([^#\ n]+ ))?/;
const [, scheme, host, port, path, query] = url.match(regex);

// 再次赋值
request.scheme = 方案；
request.host = 主机；
if (port != = 未定义) {
request.port = parseInt(port);
}
request.path = 路径；

// 日志
控制台日志 ("----------")；
console.log (方案)；
console.log (主机)；
console.log (端口)；
console.log (路径)；

// 完成
退货请求；
}
'''

# # 杂项

#### 旁路CORS

'''javascript
函数onResponse (上下文，url，请求，响应) {

// 允许所有
response.headers["Access-Control-Allow-Origin"] = "*";
response.headers["Access-Control-Allow-Headers"] = "*";
response.headers["访问控制允许方法"] = "*"；

// 完成
返回响应；
}
'''

#### 向请求/响应注入标头

'''javascript
函数onRequest(context，url，request) {
// 添加标头
request.headers["My-Injected-Header"] = "Proxyman";
退货请求
}

函数onResponse (上下文，url，请求，响应) {
// 添加标头
response.headers["My-Injected-Header"] = "Proxyman";
返回响应；
}

'''

#### 具有sleep() 功能的响应延迟

它对于模拟特定请求或响应上的 “慢速网络” 非常有用。您可以查看GUI的 [网络条件工具](https://docs.proxyman.com /高级功能/网络节流 #1.-whats-it)。

* macOS

'''javascript
函数onResponse (上下文，url，请求，响应) {
console.log (“开始睡眠”)；

// 睡眠5秒
睡眠 (5000)；

// 完成
返回响应；
}
'''

* Windows/Linux

'''javascript
异步函数onResponse (上下文，url，请求，响应) {
console.log (“开始睡眠”)；

// 睡眠5秒
// 在Windows/Linux上必须使用 'await' 关键字
等待睡眠 (5000)；

// 完成
返回响应；
}
'''

#### AES加密/解密

'''javascript
const { encryptAES, decryptAES } = require("@ addons/CryptoJS.js")

函数onRequest(context，url，request) {

// 加密
var message = 'my message from Proxyman';
var password = '密钥123'；
var密文 = encryptAES (消息，密码)；

// 解密
var originalText = decryptAES (密文，密码)；

// 完成
退货请求；
}
'''

#### DES加密/解密

'''javascript
const { encryptDES, decryptDES } = require("@ addons/CryptoJS.js")

函数onRequest(context，url，request) {

// 加密
var message = 'my message from Proxyman';
var password = '密钥123'；
var密文 = encryptDES (消息，密码)；

// 解密
var originalText = decryptDES (密文，密码)；

// 完成
退货请求；
}
'''

#### 写入/导出到本地文件

* 覆盖模式

'''javascript
函数onResponse (上下文，url，请求，响应) {

// 写入单个文件
writeToFile(response.body, "~/Desktop/body.json");

// 将正文写入具有流ID的文件
writeToFile(response.body, "~/Desktop/sample-" + context.flow.id);

// 完成
返回响应；
}
'''

* 附加模式 (仅适用于Proxyman 3.6.2 +)

'''javascript
异步函数onResponse (上下文，url，请求，响应) {

// 追加到已存在的文件
// 或创建一个新的文件，如果它不存在
var opt = {appendFile: true}
writeToFile(response.body, "~/Desktop/body.json", opt);

// 完成
返回响应；
}
'''

#### 检查第一个是否存在

* 可用: Proxyman macOS 5.4.0 +

'''javascript
异步函数onRequest (上下文，url，请求) {

const filePath = "~/Desktop/myfile.json"

// 检查文件是否存在
if (isFileExists(filePath)) {
console.log("文件存在")；
} else {
console.log("文件不存在")；
}

// 完成
退货请求；
}
'''

#### 读取文件

* 如果它是基于文本的-> 返回一个 ** 字符串 **
* 否则-> 返回 ** Uint8Array **
* 可用: Proxyman macOS 5.4.0 +

'''javascript
异步函数onRequest(context，url，request) {// console.log(request)；

const textFilePath = "~/Desktop/myfile.json";

// 检查是否存在
if (isFileExists(filePath)) {

// 从文件中读取
const text = readFromFile(textFilePath);

// 将字符串解析为JSON对象
const obj = JSON.parse(text);
}

// 读取二进制文件
const binaryFilePath = "~/Desktop/screenshot.png";
const binaryFile = readFromFile(binaryFilePath); // Uint8Array

// 完成
退货请求；
}
'''

# # 地图遥控器

#### 将v1映射到v2端点

'''javascript
函数onRequest(context，url，request) {

// 将URL路径中的v1替换为v2
var newPath = request.path.replace("v1", "v2");
request.path = newPath

// 完成
退货请求；
}
'''

#### 将本地主机映射到生产

'''javascript
函数onRequest(context，url，request) {

// 使用生产URL
request.scheme = "https";
request.host = "proxyman.io";
request.port = 443；

// 完成
退货请求；
}
'''

#### 将生产映射到本地主机

'''javascript
函数onRequest(context，url，request) {

// 使用生产URL
request.scheme = "http";
request.host = "localhost";
request.port = 3000；

// 完成
退货请求；
}
'''

# # 使异步/等待HTTP请求 (macOS)

{% 提示样式 = "info" %}
此功能 \ '$ http \' 在macOS版本上可用。要在Windows上使用，请检查下一部分。
{% endhint %}

#### 带查询的GET请求

'''javascript
异步函数onResponse (上下文，url，请求，响应) {
// 带查询的GET请求
var url = "https:// httpbin.proxyman.app/get？id = proxyman & country = 美国 % 20个州"；
var输出 = 等待 $ http.get(url)；

// 获取状态代码
console.log(output.statusCode);

// 获取身体
console.log(output.body)

// 获取标头
console.log(output.headers)

// 完成
返回响应；
}
'''

#### 带JSON正文的POST请求

'''javascript
异步函数onResponse (上下文，url，请求，响应) {
// 定义JSON Body和Header
// 确保 “Content-Type” 是 “application/json”
var参数 = {
正文: {
"用户": {
"名称": "Proxyman"
}
},
标题: {
"Content-Type": "application/json"
}
}

// 带有等待的POST请求
var输出 = await $ http.post("https:// httpbin.proxyman.app/post"，param)；

// 获取状态代码
console.log(output.statusCode);

// 获取身体
console.log(output.body)

// 获取标头
console.log(output.headers)

// 完成
返回响应；
}
'''

#### 带有application/x-www-form-urlencoded正文的POST请求

'''javascript
异步函数onResponse (上下文，url，请求，响应) {
// 定义表单体和表头
// 确保 “Content-Type” 是 “application/x-www-form-urlencoded”
var参数 = {
正文: {
"key1": "value1",
"key2": "value2"
},
标题: {
"Content-Type": "application/x-www-form-urlencoded"
}
}

// 带有等待的POST请求
var输出 = await $ http.post("https:// httpbin.proxyman.app/post"，param)；

// 获取状态代码
console.log(output.statusCode);

// 获取身体
console.log(output.body)

// 获取标头
console.log(output.headers)

// 完成
返回响应；
}
'''

#### PUT / PATCH/DELETE请求

'''javascript
异步函数onRequest (上下文，url，请求) {

var参数 = {
正文: {
"用户": {
"名称": "Proxyman"
}
},
标题: {
"Content-Type": "application/json"
}


var输出 = await $ http.post("https:// httpbin.proxyman.app/post"，param)；
var output = await $ http.put("https:// httpbin.proxyman.app/put", param);
var output = await $ http.de lete("https:// httpbin.proxyman.app/delete", param);

// 完成
退货请求；
}
'''

# # 使异步/等待HTTP请求 (Windows/Linux)

Windows/Linux附带一个内置的 [Axios](https://github.com/axios/axios) 库。您可以使用 \ 'Axios \ \ '语法轻松地发出HTTP(s) 请求。

'''javascript
异步函数getUser() {
尝试 {
const响应 = 等待axios.get('https:// httpbin.proxyman.app/user？ID = 12345 ')；
console.log (响应)；
} catch (error) {
console.error (错误)；
}
}
'''

### 像阻止列表工具一样中止请求/响应

* 仅适用于Proxyman 3.11.0及更高版本

#### 中止请求

'''javascript
函数onRequest(context，url，request) {
// 删除连接
中止 ()；
}
'''

'''javascript
函数onRequest(context，url，request) {

// 在某些条件下使用if中止
if (true) {
中止 ()；
return; // 必须返回一个void来停止func
}

// 完成
退货请求；
}
'''

#### 中止响应

'''javascript
函数onResponse (上下文，url，请求，响应) {
// 删除连接
中止 ()；
}
'''

### URL和URLSearchParams

从Proxyman 4.13.0或更高版本开始，本机支持 [URL](https://developer.mozilla.org/en-US/docs/Web/API/URL) 和 [URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams)。

'''javascript
函数onRequest(context，url，request) {

// URL
const urlObj = 新URL("https:// proxyman.io/api/v1/user？id = 123")；
console.log(urlObj.hostname);
console.log(urlObj.search);
console.log(urlObj.searchParams);

// URLSearchParmas
const params1 = 新URLSearchParams("foo = 1 & bar = 2")；

// 完成
退货请求；
}
'''

### 重新加载系统环境变量

Proxyman macOS 4.15.0或更高版本。

确保我们首先启用权限，在更多按钮-> 环境变量-> 允许所有脚本读取env。

'''javascript
异步函数onRequest (上下文，url，请求) {
// 手动重新加载以获取最新更改
_reloadEnv();

// 获取环境
console.log($ PROXYMAN_ID)

// 完成
退货请求；
}
'''

### 更改Websocket URL，请求/响应标头

* 支持从macOS 6.2.0或更高版本
*❌无法修改Websocket消息。仅支持URL和标头。

** 从本地主机映射到生产 **

* 规则ws \:// proxyman.Debug: 3000

'''js
异步函数onRequest (上下文，url，请求) {
// console.log (请求)；
console.log(url);

request.scheme = "wss";
request.host = "wss.httpbin-proxyman.xyz"
request.port = 443

// 完成
退货请求；
}

'''

** 生产到本地主机 **

* 规则wss \:// echo.websocket.org

'''js
异步函数onRequest (上下文，url，请求) {
// console.log (请求)；
console.log(url);

request.scheme = "ws";
request.host = "proxyman.de bug"
request.port = 3000

// 完成
退货请求；
}

'''
