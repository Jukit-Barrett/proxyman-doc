# 内置JS库

### 1.什么事？

Proxyman提供了一些有用的捆绑的JS库，帮助您轻松地实现一些任务

{% 提示样式 = "info" %}
库位置: ** \ ~/Library/Application \ Support/com.proxyman.NSProxy/addons/libs **
{% endhint %}

### 2.内置库

| 名称 | 描述 | 源 |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| base64.js | 包含基本的Base64编码/解码 | - |
| atob.js | window \.atob() | <https://github.com/jsdom/abab> |
| btoa.js | window \.btoa() | <https://github.com/jsdom/abab> |
| hashes.js | 包含各种哈希函数: MD5，RIPEMP-160，SHA1，SHA256，SHA512，HMAC | <https://github.com/h2non/jshashes> |
| lodash.js | 包含各种文本转换函数 | <https://lodash.com> |
| vkBeautify.js | 以XML、JSON、CSS和SQL格式打印或缩小文本。| <https://github.com/kayhadrin/vkBeautify/> |
| crypto-js.min.js | 标准和安全加密算法的JavaScript实现，例如DES，AES，Rabbit，...(版本3.3.0) | <https:// cryptojs.gitbook.io/docs/> |

### 3.如何导入自己的JS库？

1.您可以提供自己的JS库，但请确保使用 [Browserify](http://browserify.org) 或 [WebPack](https://webpack.js.org) 将所有依赖项捆绑到单个JS文件中。
2.确保正确导出func。
3.将文件放在 ** \ ~/Library/Application \ Support/com.proxyman.NSProxy/addons/libs/your-lib.js **
4.使用导入文件

'''javascript
require('@ libs/your-lib.js')；
'''

例如，

'''javascript
const哈希 = require('@ libs/Hashes.js')；
const { cssmin } = require('@ libs/vkBeautify.js');
const Lodash = require('@ libs/lodash.js');
const { atob } = require('@ lib@atob.js')
'''

{% 提示样式 = "info" %}
您可以在 ** \ ~/Library/Application \ Support/com.proxyman.NSProxy/addons/libs/** 处检查内置库以供参考
{% endhint %}

### 4.备注

{% 提示样式 = "info" %}
感谢 [Ivan Mathy](https://github.com/IvanMathy) 创建Boop应用程序，促进Proxyman的内置附加组件。
{% endhint %}
