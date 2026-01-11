# WebSocket

# #1.什么事？

Proxyman可以捕获WebSocket (WS) 和安全WebSocket (WSS) 流量并轻松预览。

* 从iOS物理设备和iOS模拟器捕获WS/WSS (必需 [亚特兰蒂斯框架](https://github.com/ProxymanApp/atlantis))
* 从Web浏览器和Mac应用程序捕获WS/WSS。
* 从Android物理设备或Android模拟器捕获WS/WSS。
* 更漂亮的WebSocket消息。
* 过滤所有/发送/接收的消息。
* 请参阅JSON/树预览/十六进制格式的内容。
* 自定义列: 帧，长度，数据，时间，...
* 如果可能的话，自动解码二进制消息到JSON
* 通过外部编辑器打开WebSocket消息，如Sublime，VSCode

# #2.从iOS捕获WS/WSS

如果您的iOS应用程序正在使用 ** URLSessionWebSocketTask ** 或iOS WebSocket库，例如红蜘蛛，SocketRocket等。Proxyman可能无法捕获WS/WSS通信。

* ** 原因 **: 苹果的意图。** URLSessionWebSocketTask ** 不尊重系统HTTP代理。所有WS/WSS流量都直接进入Internet。因此，Proxyman或Charles代理无法捕获它。
* 示例Ap: <https://github.com/ProxymanApp/ websocket-example-ios-app>

###✅解决方案1 (建议用于iOS 17或更高版本)

1.按照您的 [iOS设备](https://docs.proxyman.com /调试设备/ios设备) 或 [iOS模拟器](https://docs.proxyman.com /调试设备/ios模拟器) 的设置指南 (确保我们在您的设备上安装并信任证书)
2. Proxyman设置: 工具> 代理设置> SOCKS代理设置-> 启用它 (注意端口)
3.在主Proxyman应用程序-> 记下Proxyman工具栏中的当前IP

<figure><img src = "images/proxyman_capture_websocket_4_91268e7e.jpeg" alt = ""><figcaption><p> 获取Proxyman当前IP</p></figcaption></figure>

4.在您的应用程序上: 在您的应用程序中配置袜子代理，确保这仅可用于通过实现开关或其他方式进行调试构建，您可能不希望使用此配置发布版本。

* 用于NWConnection

{% code overflow = "wrap" fullWidth = "false" %}

''' 斯威夫特
让参数 = webSocketURL.scheme = = "wss"？NWParameters.tls: NWParameters.tcp

let options = NWProtocolWebSocket.Options()
options.autoReplyPing = true

Parameters.Defaultprotocolstack.applicationProtocols.insert (选项，位于: 0)

如果 # 可用 (iOS 17.0，*) {
让socksv5Proxy = NWEndpoint.hostPort (主机: "x.x"，端口: 8889) // 请x.x与一个真正的Proxyman IP
让config = ProxyConfiguration.init(socksv5Proxy: socksv5Proxy)
let context = NWParameters.PrivacyContext (描述: "my socksv5Proxy")
context.proxyConfigurations = [config]

parameters.setPrivacyContext(context)
}

让连接 = NWConnection (到:。url(webSocketURL)，使用: 参数)
connection.start (队列:。主)
'''

{% endcode %}

* 对于URLSession和URLSessionWebSocketTask

{% code overflow = "wrap" fullWidth = "false" %}

''' 斯威夫特
私有惰性var urlSession: URLSession = {
让config = urlsessionconfiguration.default
如果 # 可用 (iOS 17.0，*) {
让socksv5Proxy = NWEndpoint.hostPort (主机: "x.x"，端口: 8889) // 请x.x与一个真正的Proxyman IP
让proxyConfig = ProxyConfiguration.init(socksv5Proxy: socksv5Proxy)
config.proxyConfigurations = [proxyConfig]
}

返回URLSession (配置: config，委托: nil，delegateQueue: nil)
}()
'''

{% endcode %}

5.完成✅

<figure><img src = "images/Screenshot_2024-11-29_at_1.17.23_PM_1e5670e9.jpg" alt = ""><figcaption><p> 使用Proxyman从iOS捕获Websocket </p></figcaption></figure>

* 贷记 [** 富兰克林桑博尼 **](https://github.com/FranklinSamboni) **->** <https://github.com/ProxymanApp/Proxyman/issues/ 586 # issuecomment-2125082129>
* 教程: <https:// proxyman.io/posts/2019-10-18-WebSocket-Debugging>

###✅解决方案2

使用 [Atlantis Framework](https://github.com/ProxymanApp/atlantis#features) (由Proxyman开发) 捕获来自iOS的WS/WSS ** URLSessionWebSocketTask ** 流量。

阅读更多 [ https://github.com/ProxymanApp/atlantis](https://github.com/ProxymanApp/atlantis# wswss-traffic)

# #3.从您的网络浏览器 (Chrome，Safari等) 捕获WebSockets

* Proxyman可以从开箱即用的Web浏览器捕获WS/WSS。不需要配置任何东西。
* 如何使用: 打开Google Chrome -> 访问建立WS/WSS连接的网站-> 打开Proxyman -> 找到您的websocket域-> 在响应面板上-> 单击在这些域上启用SSL代理。打开您的浏览器，并重新加载您的网站-> Proxyman将捕获和解密WS/WSS✅

# #4.从NodeJS，Golang，Python服务器捕获Websocket

* Proxyman可以从您的NodeJS，Golang，Python和Ruby服务器捕获WS/WSS。
* 使用方法: 阅读 [自动-设置](https://docs.proxyman.com /自动-设置 “提及”) 在此终端上启动您的服务器-> 进行WS/WSS连接-> Proxyman自动捕获并decyrpts它✅

# #5.从Localhost <-> 生产映射Websocket

可以映射来自localhost <-> 生产的WebSocket流量。请查看 [Map Remote Tool。](https://docs.proxyman.com/map-remote #7.4-map-websocket-从本地主机到生产)
