# Golang

# #1.新的自动解决方案 (macOS v5.17.0或更高版本)✅

Proxyman macOS v5.17.0或更高版本可以通过单击从Golang捕获HTTP/HTTPS流量。

* 1-click解决方案: 无需手动设置HTTP代理配置或信任自签名证书。
*✅支持许多Go网络库: net/http，fasthttp，resty，gorequest，req，grequests

### 如何使用:

1.打开Proxyman -> 设置菜单-> 自动设置
2.选择您喜欢的终端-> 点击 “打开新终端” 按钮
3.如果需要，接受Apple脚本权限提示

<figure><img src = "images/Screenshot_2025-03-18_at_10.54.37_1172ad44.jpg" alt = ""><figcaption><p> 打开预配置终端拦截GO网络https</p></figcaption></figure>

4.新的终端应用程序启动-> 您可以启动您的Golang后端服务器，或运行脚本 => Proxyman自动捕获所有流量。
5.例如:

'''
$ go run main.go
'''

6. Proxyman从go捕获所有内部HTTP/HTTPS，包括net/http

<figure><img src = "images/CleanShot_2025-03-18_at_09.56.44_2x_86960445.jpg" alt = ""><figcaption><p> 捕获和拦截来自net/http go的HTTPS流量 </p></figcaption></figure>

* Go示例代码: <https://github.com/ProxymanApp/ golang-example>

# #2.旧解决方案 (不推荐❌)

* Proxyman无法捕获来自Golang服务器的任何HTTP/HTTPS流量。
* 原因是某些网络库 (例如net/http) 不会尊重系统HTTP代理，因此没有流量通过Proxyman应用程序。

### 2.1解决方案

#### net/http

1.配置代理到Proxyman，默认情况下，它位于IP = localhost，端口9090
2.告诉运输信任Proxyman自签名证书。否则，您将收到SSL错误，因为net/http拒绝。

''' 去
主要包装

导入 (
"加密/tls"
"fmt"
"io/ioutil"
"日志"
"net/http"
"网络/url"
)

func main() {
// 创建一个新的HTTP客户端
客户端: = & http.client {}

// 配置代理
proxyURL，err := url.Parse("http:// localhost:9090")
如果错了!= nil {
log.Fatal("解析代理URL时出错:"，err)
}

// 使用代理和TLS设置配置传输
传输: = & http.transport {
代理: http.ProxyURL(proxyURL)，
TLSClientConfig: & tls.Config {
InsecureSkipVerify: true，// 这允许自签名证书
},
}

// 设置客户端的传输
client.Transport = transport

// 提出请求
resp，err := client.Get(" https://example.com ")
如果错了!= nil {
log.Fatal("请求错误:"，err)
}
延迟resp.Body.Close()

// 读取响应正文
正文，err := ioutil.ReadAll (对应正文)
如果错了!= nil {
log.Fatal("错误读取响应:"，err)
}

// 打印响应
fmt.Printf("状态: % s \ n"，resp.Status)
fmt.Printf("Body: % s \ n", string(body))
}

'''
