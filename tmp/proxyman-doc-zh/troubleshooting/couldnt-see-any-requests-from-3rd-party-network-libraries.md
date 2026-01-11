# 我看不到来自第三方网络库的任何请求

###

# #1.问题

* 我可以看到Proxyman上的其他请求，但不是从我的网站，NodeJS，iOS或Android，....其中使用第三方网络库，如 [fetch](https://github.com/github/fetch )，[axios](https://github.com/axios/axios )，[Alamofire](https://github.com/Alamofire/Alamofire )，[Ktor Apache HttpClient](https:// ktor.io)，curl...

# #2.新的自动解决方案 (v4.7.0或更高版本)✅

Proxyman v4.7.0或更高版本可以通过1-click从Python捕获HTTP/HTTPS流量。

* 1-click解决方案: 无需手动设置HTTP代理配置或信任自签名证书。
* 支持NodeJS，Ruby和Python。

### 如何使用:

1.打开Proxyman -> 设置菜单-> 自动设置
2.点击 “打开新终端”
3.如果需要，接受Apple脚本权限提示
4.新的终端应用程序启动-> 您可以启动您的Python后端服务器，或运行脚本 => Proxyman自动捕获所有流量。
5.完成✅

<figure><img src = "images/CleanShot_2023-04-22_at_15.18.19_2x_5039dd93.jpg" alt = ""><figcaption></figure>

# #3.旧解决方案 (不推荐❌)

通常，我们必须手动配置网络库以使用HTTP代理并指向Proxyman端口 (默认为9090)

可能的解决方案列表:

* Fetch: <https://stackoverflow.com/questions/ 44524236/using-proxy-like-fiddler-与fetch-api>
* cURL: 使用 * -- 代理 * 标志。例如:

'''
$ curl -v " https://httpbin.org/get？id= 123" -- 代理localhost:9090
'''

阅读更多: <https://stackoverflow.com/a/ 9445516/3127477>

* Ktor: <https:// ktor.io/clients/http-client/features/proxy.html>
* 阿拉莫火: <https://stackoverflow.com/a/ 42754358/3127477>

#### Axios

您可以在Axios上明确设置HTTP代理。所有流量都将显示在Proxyman上。

'''javascript
axios.get({
url: '/v1/user/data',

// 'proxy' 定义代理服务器的主机名和端口
// 使用 'false' 禁用代理，忽略环境变量。
// 'auth' 表示应使用HTTP基本身份验证连接到代理，并且
// 提供凭据。
// 这将设置一个 '代理授权' 头，覆盖任何现有的
// 使用 “headers” 设置的 “Proxy-authorization” 自定义标头。
代理服务器: {
主持人: “127.0.0.1”，
端口: 9090
}
});
'''

对于主机和端口值，您可以在 [iOS设备Windows] 中找到它 ( https://docs.proxyman.com /调试-设备/ios-设备 # ios-设置-指南)
