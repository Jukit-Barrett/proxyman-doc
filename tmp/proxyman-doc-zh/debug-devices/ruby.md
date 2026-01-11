# Ruby

# #1.新的自动解决方案 (v4.7.0或更高版本)✅

Proxyman v4.7.0或更高版本可以通过单击从Ruby捕获HTTP/HTTPS流量。

* 1-click解决方案: 无需手动设置HTTP代理配置或信任自签名证书。
* 支持许多Ruby库: http，net/http，net/https，httpparty和faraday。

### 如何使用:

1.打开Proxyman -> 设置菜单-> 自动设置
2.点击 “打开新终端”
3.如果需要，接受Apple脚本权限提示
4.新的终端应用程序启动-> 您可以启动您的Ruby后端服务器，或运行脚本 => Proxyman自动捕获所有流量。
5.完成✅

<figure><img src = "images/CleanShot_2023-04-22_at_15.18.19_2x_5039dd93.jpg" alt = ""><figcaption><p> 从Ruby捕获流量 </p></figcaption></figure>

# #2.旧解决方案 (不推荐)

### 1.将HTTP代理设置为Ruby

Net::HTTP将自动从 'http_proxy' 环境变量创建一个代理，如果它是present。

所以你可以使用:

'''bash
ENV['http_proxy'] = 'http:// 127.0.0.1:9090' # 您的http:// 地址: 此处的端口
'''

Net::HTTP将默认使用它的所有请求。

参考: <https://stackoverflow.com/questions/ 15792999/how-to-set-a-proxy-in-rubys-net-http>

### 2.在Ruby上安装Proxyman证书

默认情况下，macOS上的 ** Ruby ** 可能不信任Proxyman的自签名证书。因此，如果您尝试拦截HTTPS流量，则可能会遇到SSL错误。

您可以通过使用 'SSL_CERT_FILE' env显式告诉Ruby使用Proxyman证书。

'''bash
$ env SSL_CERT_FILE = ~/.proxyman/proxyman-ca.pem ruby my_script.rb
'''
