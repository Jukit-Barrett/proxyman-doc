# 故障排除

### 1.自动设置不会从我的新网络库捕获任何HTTP流量

Proxyman支持以下库:

* ** NodeJS **: Axios、tot、superagent、fetch和node-fetch
* ** Python **: http, https, aiohttp, requests
* ** Ruby **: http、net/htps、faraday和httpparty

-> 如果您使用的是一个新的图书馆和Proxyman自动设置不捕获您的HTTP/HTTPS流量，请 [创建一个新的票证](https://github.com/ProxymanApp/Proxyman/issues) 请求您的图书馆。

### 2.我从我的NodeJS，Ruby，Python脚本中获取SSL错误

-> 确保您已在macOS上安装并信任证书。您可以通过打开证书菜单-> 安装Mac证书轻松地做到这一点。

-> 如果该错误仍然发生，则似乎自动设置功能中存在错误，请 [创建新票证](https://github.com/ProxymanApp/Proxyman/issues) 并告知我们。

### 3.Proxyman无法记录来自本地服务器的任何流量，例如 <http:// localhost:3000>

默认情况下，来自 <http:// localhost:3000> 的通信不通过系统代理。因此，Proxyman无法捕获您的流量。

请按照此 [解决方案](https:// docs.proxyman.io/故障排除/couldnt-see-any-request-from-localhost-server) 来修复它。
