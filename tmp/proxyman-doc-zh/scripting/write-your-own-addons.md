# 编写自己的插件

# #1.什么事？

您可以编写自己的插件来实现Proxyman尚未提供的功能。你可以做:

* 编写自己的Javascript插件。
* 使用 [内置库](https://docs.proxyman.com/scripting/ 内置js库)。
* 写你的图书馆，并与你的同事分享。

# #2.如何写一个插件？

1.打开位于 '~/Library/Application \ Support/com.proxyman.NSProxy/users的用户插件文件夹，或者您可以通过打开更多按钮-> 文档-> 打开自定义插件文件夹来打开...

![](图片/Screen_Shot_2021-08-13_at_20.37.39_0026c252.png)

2 \。复制 “helloworld.js” 文件并将其重命名为 ** MyAwesomeAddon.js **

3 \。打开文件，您可以看到模板。

4 \。更改元数据并编写JS代码

'''javascript
/**
{
“名称”: “我的真棒插件”，
"description":"第一个用户插件"，
“作者”: “Proxyman”，
"标签":"helloworld"
}
**/

const { md5 } = require("@ addons/MD5.js");

const sayHello = () => {
var content = “你好，世界。我的第一个自定义插件。”；
var hash = md5 (内容)；
返回内容 + ". MD5 =" + hash；
};

// 确保在方法的末尾导出函数
exports.sayHello = sayHello;

'''

* 您可以使用 ** require(@ "addons/\<name.js>")** 导入内置插件

'''javascript
const { md5 } = require("@ addons/MD5.js");
'''

{% 提示样式 = "info" %}
查看Proxyman提供的 [内置插件](https://docs.proxyman.com/addons# 2内置插件)
{% endhint %}

* 您可以使用 ** require(@ "lib/\<name.js>")** 导入内置库

{% 提示样式 = "info" %}
查看Proxyman提供的 [内置库](https://docs.proxyman.com/scripting/ 内置js库)
{% endhint %}

5 \。保存文件

6 \。在Proxyman应用程序中打开脚本并导入脚本

'''javascript
// 导入您的插件
// 确保导入您在插件中导出的函数
const { sayHello } = require("@ users/MyAwesomeAddon.js");

// 用法
sayHello();
'''

{% 提示样式 = "info" %}
** require (“@ users/MyAwesomeAddon.js”) ** 是您的插件目录

@ users是自定义插件文件夹。
{% endhint %}

# #3.备注

{% 提示样式 = "info" %}
您自己的脚本存储在 ** \ ~/Library/Application \ Support/com.proxyman.NSProxy/users **

此文件夹是安全的。它永远不会被Proxyman覆盖或删除。
{% endhint %}
