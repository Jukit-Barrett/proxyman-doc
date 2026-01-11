# 环境变量

# #1.共享状态

{% 提示样式 = "info" %}
此功能仅在 ** macOS 10.15 + ** 上可用。在macOS 10.15之前，它可能会崩溃。
{% endhint %}

当使用全局对象执行脚本时，可以从 ** onRequest()** 和 ** onResponse()** 从 ** 不同的脚本 ** 共享状态: ** sharedState **

* ** sharedState ** 是一个JS对象 (字典)，因此您可以从 ** onRequest()** 分配任意键和值，然后在 ** onResponse()** 或 ** 不同的脚本 ** 上接收数据。

下面的代码演示:

* 获取全局计数器，并在脚本执行后立即增加
* 在请求和响应之间共享数据

'''javascript
函数onRequest(context，url，request) {

// 将一些状态保存到sharedState
sharedState.url = url;
sharedState.data = "自定义"；
sharedState.info = {"用户名": "Proxyman"}；

// 增加全局计数器
var count = sharedState.count ??0;
count + = 1;
sharedState.count = count;

// 日志
console.log(sharedState);
退货请求；
}

函数onResponse (上下文，url，请求，响应) {

// 收到它
console.log("自定义数据 =" + sharedState.dataa)；
console.log("sharedState.count =" + sharedState.count);

// 完成
返回响应；
}
'''

{% 提示样式 = "info" %}
从Proxyman 2.25.0 + 开始，** sharedState ** 可用于不同的脚本。它仅在退出Proxyman应用程序或使用 \ 'clearSharedState()\' 功能时发布。
{% endhint %}

{% 提示样式 = "info" %}
在Proxyman 2.24.0 ** 之前，** ** sharedState ** 仅在执行脚本的当前流中处于活动状态，并在脚本运行时释放。
{% endhint %}

要清除所有数据，请考虑使用 \ 'clearSharedState \ '函数。

'''javascript
// 清除sharedState对象中的所有数据
clearSharedState();
'''

# #2.环境变量

环境变量功能是从 ** Proxyman 3.8.0 ** 及更高版本引入的。

* 脚本可以访问系统环境。
* 支持bash或zsh。

#### 如何使用

1.在 '~/.zshrc' 或' ~/.bashrc' 中定义一个env

'''bash
导出ACCESS_TOKEN = AAABBBCCC
导出PROXYMAN_PATH =/Users/my_user/Desktop/file-mapper
'''

2 \。打开任何脚本-> 更多按钮-> 环境变量-> 允许所有脚本访问env。

3 \。重新加载ENV以获取env更新。

![在脚本上启用env] (图像/Screen_Shot_2022-07-31_at_10_48_26_ee70002b.jpg)

4 \。使用前缀 “$” 从脚本访问env

'''javascript
异步函数onResponse (上下文，url，请求，响应) {
console.log($ PATH);
console.log($ ACCESS_TOKEN);
console.log($ PROXYMAN_PATH);

// 完成
返回响应；
}
'''

# #3.增加

* 手动重新加载系统环境 (在Proxyman macOS 4.15.0或更高版本上可用)。确保我们首先启用权限，在更多按钮-> 环境变量-> 允许所有脚本读取env。

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
