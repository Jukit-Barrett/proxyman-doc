# async/await请求

# #1.什么事？

在Proxyman macOS v3.5.0和Windows/Linux v2.11.0或更高版本中，您可以使用 “async/await” 进行HTTP/HTTPS调用，以检索脚本中的外部资源。

{% 提示样式 = "info" %}

* 在macOS上: 使用 \ '$ http \'
* 在Windows/Linux上: 使用内置的 \ 'axios \'
{% endhint %}

#### 示例: 带有JSON正文的POST请求 (macOS)

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
var输出 = await $ http.post (“ https://httpbin.org/post ”，param)；

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

# #2.如何在macOS上使用？

#### 方法

'''javascript
var输出 = await $ http.get(" https://httpbin.org/anything ")；
var输出 = await $ http.post (“ https://httpbin.org/anything ”)；
var输出 = await $ http.put(" https://httpbin.org/anything ")；
var输出 = 等待 $ http.update (“ https://httpbin.org/anything ”)；
var输出 = await $ http.Delete (" https://httpbin.org/anything ")；
'''

#### 输出格式

'''javascript
var输出 = await $ http.get(" https://httpbin.org/anything ")；
console.log (输出)

// 打印
{
"statusCode": <Int>,
"headers": <Object>,
"body": <Object>
}
'''

#### 示例代码

* [带查询的GET请求](https://docs.proxyman.com /代码片段-代码 # get-Request-与查询)
* [带有JSON正文的POST请求](https://docs.proxyman.com /代码段代码 # post-Request-与json-body)
* [带有application/x-www-form-urlencoded正文的POST请求](https://docs.proxyman.com /代码段代码 # post-Request-与application-x-www-form-urlencoded-正文)
* [PUT / PATCH/DELETE请求](https://docs.proxyman.com/snippet-code # put-patch-delete-Request)

{% 提示样式 = "info" %}
有关更多示例代码，请签出 [HTTP代码段代码](https://docs.proxyman.com /代码段代码 # 制作-异步-等待-http-请求)。
{% endhint %}

# #3.如何在Windows/Linux上使用？

Proxyman Windows/Linux附带一个内置的 [axios](https://github.com/axios/axios) 库，这意味着我们可以使用axios语法来发出HTTP(s) 请求。

例如:

'''javascript
异步函数getUser() {
尝试 {
const响应 = 等待axios.get('/user？ID = 12345')；
console.log (响应)；
} catch (error) {
console.error (错误)；
}
}
'''

# #4.备注

* 确保您在 'onRequest()'和 'onResponse()' 上定义了 ** async ** 函数:

'''javascript
异步函数onRequest (上下文，url，请求) {
var输出 = await $ http.get(" https://httpbin.org/get ")；
退货请求；
}

异步函数onResponse (上下文，url，请求，响应) {
var输出 = await $ http.get(" https://httpbin.org/get ")；
返回响应；
}
'''

* 请求超时为10秒。
* 内联HTTP请求不通过Proxyman代理，因此不受其他调试工具的影响。
* 使用可以在 'onRequest()'和 'onResponse()' 上使用 'await $ http.get()'
* 确保正文类型与Content-type标头匹配。

** 带有应用程序/JSON的json正文 **

'''javascript
var参数 = {
正文: {
"name": "Proxyman",
},
标题: {
"Content-Type": "application/json"
}
}
'''

** 使用application/x-www-form-urlencoded编码的表单正文 **

'''javascript
var参数 = {
正文: {
"key1": "value1",
"key2": "value2"
},
标题: {
"Content-Type": "application/x-www-form-urlencoded"
}
}
'''
