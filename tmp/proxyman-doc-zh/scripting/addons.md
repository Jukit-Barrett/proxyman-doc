# 插件

# #1.什么事？

Proxyman提供了一个方便的内置附加组件列表，可帮助您执行许多常见任务，例如MD5，SHA1哈希，Base64编码/解码，美化XML，JSON ....

### 2.内置插件

您可以在 [addons代码段代码](https://docs.proxyman.com/scripting/ 代码段代码) 中找到所有插件的示例代码

| 名称 | 描述 |
| ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| [Base64.js](https://docs.proxyman.com /代码段-代码 # use-base64-addon) | Base64编码/解码。支持本机atob/btoa函数 |
| CamelCase.js | 将文本转换为骆驼大小写 |
| CryptoJS.js | DES，AES，Rabbit加解密算法.CryptoJS的一个小包装 |
| DateToTimestamp.js | 将字符串日期转换为时间戳 |
| DateToUTC.js | 将字符串日期转换为UTC字符串 |
| DecodeURI.js | 解码百分比编码的字符串 |
| EncodeURI.js | 编码为百分比编码的字符串 |
| FormatCSS.js | 美化CSS字符串 |
| FormatJSON.js | 美化JSON字符串 |
| BeautifyJSON.js | 将JSON Obj转换为beauty JSON字符串 |
| UglifyJSON.js | 将JSON Obj转换为丑陋的JSON字符串 |
| FormatXML.js | 美化XML字符串 |
| HelloWorld.js | 你好，世界 |
| Hex2rgb.js | 将 #000000字符串转换为RGB字符串 |
| JsonToQuery.js | 将JSON Objc转换为查询字符串 |
| JSONValidator.js | 验证JSON字符串 |
| [JWTDecode.js](https://docs.proxyman.com /代码段-代码 # jwt-decode) | 解码jwt令牌 |
| KebabCase.js | 转换为Kebab字符串 |
| [MD5.js](https://docs.proxyman.com /代码段-代码 # use-hashing-addon-md-5-sha-1-sha-256-sha-512) | 哈希MD5 |
| MinifyCSS.js | 缩小CSS字符串 |
| MinifyJSON.js | Minify JSON String |
| MinifyXML.js | 缩小XML字符串 |
| QueryToJson.js | 将查询字符串转换为JSON对象 |
| [Pako.js](https://docs.proxyman.com /代码片段-代码 # deflate-inflate-and-gzip-ungzip) | Deflate/Inflate和gzip/ungzip |
| [SHA1.js](https://docs.proxyman.com /代码段-代码 # use-hashing-addon-md-5-sha-1-sha-256-sha-512) | 哈希SHA1 |
| [SHA256.js](https://docs.proxyman.com /代码段-代码 # use-hashing-addon-md-5-sha-1-sha-256-sha-512) | 哈希SHA256 |
| [SHA512.js](https://docs.proxyman.com /代码段-代码 # use-hashing-addon-md-5-sha-1-sha-256-sha-512) | 哈希SHA512 |
| SnakeCase.js | 转换为蛇形大小写 |
| StartCase.js | 转换为开始大小写 |
| [UUID.js](https://docs.proxyman.com /代码段-代码 # use-uuid-v4-addon) | 生成唯一UUID-v4字符串 |

# #3.如何使用插件？

每个插件将导出您可以使用 “require” 函数导入的函数

为了说明，Base64.js插件看起来像:

'''javascript
// Base64.js
const Base64 = require('@ libs/base64.js');
const { atob } = require("@ libs/atob.js");
const { btoa } = require("@ libs/btoa.js");

// atob / btoa
// 它们与window.atob和window.btoa等价

exports.atob = atob;
exports.btoa = btoa;

// 基本Base64
导出.base64Decode = (输入) => {
返回Base64.decode (输入)
};

导出.base64Encode = (输入) => {
返回Base64.encode (输入)；
};
'''

然后，您可以在脚本中使用它:

'''javascript
const { atob, btoa } = require("@ addons/Base64.js")

函数onRequest(context，url，request) {

// 使用export函数对base64进行编码
var text = btoa("你好，世界")；

console.log (文本)
// => SGVsbG8gV29ybGQ =
}
'''

{% 提示样式 = "info" %}
您可以在 ** \ 〜/Library/Application \ Support/com.proxyman.NSProxy/addons ** 中找到所有插件代码
{% endhint %}

# #4.备注

{% 提示样式 = "info" %}
“Require” 函数不是 [JavascriptCore框架](https://developer.apple.com/documentation/javascriptcore) 的内置函数，它是Proxyman提供的自定义函数，允许用户轻松导入插件/库。

感谢 [Ivan Mathy](https://github.com/IvanMathy) 创建Boop应用程序，促进Proxyman的内置附加组件。
{% endhint %}

{% 提示样式 = "info" %}
每个新的Proxyman更新都将覆盖Addons文件夹。确保你不编辑插件。如需修改，请复制到 ** users ** 文件夹
{% endhint %}
