# 自动设置

# #1.问题

Proxyman ** 无法从以下设置捕获 ** HTTP/HTTPS流量:

* ** NodeJS **: Axios、tot、superagent、fetch和node-fetch
* ** Python **: http, https, aiohttp, requests
* ** Ruby **: http、net/htps、faraday和httpparty、fastlane
* Golang: net/http, fasthttp, resty, gorequest, req, grequests
* ElectronJS
* 卷曲

这是一个已知的问题，因为从终端应用程序执行的NodeJS，Python，Ruby和cURL，不尊重系统HTTP代理。因此，Proxyman上没有流量。

您必须阅读每个库的技术文档并手动配置:

* HTTP代理
* 信任自签名证书

\=> 耗时且容易出错❌

# #2.解决方案: 自动设置

### 好处:

*✅** 1-单击以自动设置HTTP代理和证书 ** 在各种开发环境中
* 从NodeJS，Python，Ruby，终端或Web浏览器等捕获HTTP(s) 流量
* 安全。在当前会话上工作，不会影响您的操作系统

### 如何使用:

1.打开Proxyman -> 设置菜单-> 自动设置
2.点击 “打开新终端”
3.如果需要，接受Apple脚本权限提示
4.新的终端应用程序启动-> 您可以启动后端服务器，或运行脚本 => Proxyman自动捕获所有流量。
5.完成✅

<figure><img src = "images/CleanShot_2023-04-22_at_15.18.19_2x_16d393ad.jpg" alt = ""><figcaption><p> 启动预配置的终端app</p></figcaption></figure>

<figure><img src = "images/CleanShot_2023-04-26_at_15.53.00_2x_c0848638.jpg" alt = ""><figcaption><p> 新终端应用启动 </p></figcaption></figure>

### 注意事项:

* 只有预先配置的终端应用程序能够捕获HTTP流量开箱即用。如果您想使用自己的终端应用程序 (例如iTerm2，Hyper等)，请使用手动设置。
* 这是完全安全的，因为它运行在您当前的会话。它不会改变你的系统配置。

#### ElectronJS

1.打开自动终端
2.使用此命令行:

'''
打开 ~/Applications/your_electron_app.app
'''

### 支持库:

Proxyman (具有自动设置) 可以使用以下网络库开箱即用。

* NodeJS: [axios](https://www.npmjs.com/package/axios )，[fetch](https://nodejs.org/dist/ latest-v18.x/docs/api/globals.html # fetch) (v18 +)，[node-fetch](https://www.npmjs.com/package/ node-fetch)，[got](https://www.npmjs.com/package/got )，[https](https://nodejs.org/api/https.html )，和 [超级代理](https://www.npmjs.com/package/superagent)
* 红宝石: [http](https:// ruby-doc.org/stdlib-3.0.2/libdoc/net/http/rdoc/Net/HTTP.html)，[net/http](https:// ruby-doc.org/stdlib-2.7.0/libdoc/net/http/rdoc/Net/HTTP.html)，[net/https](https:// ruby-doc.org/stdlib-2.7.0/libdoc/net/http/rdoc/Net/HTTP.html)，[httpparty](https://github.com/jnunemaker/httparty) 和 [faraday](https://github.com/lostisland/faraday )，fastlane
* Python: [请求](https://pypi.org/project/requests/ )，[aiohttp](https://docs.aiohttp.org/en/stable/ )，http.client，urllib3和httpx
* Golang: net/http, fasthttp, resty, gorequest, req, grequests
* ElectronJS应用程序
* 没有 -- proxy标志的cURL

{% 提示样式 = "成功" %}
这是完全 ** 安全 **，因为更改只影响您当前的终端会话。它不会改变你的 ** bash \_profile ** 或 ** zshrc ** 文件。
{% endhint %}

# #3.高级: 它是如何工作的？

单击 “打开新终端” 按钮后，Proxyman将执行一系列自动操作:

1.使用AppleScript启动终端应用程序
2.使用新的终端应用程序，它开始运行此命令行:

'''bash
set -a & & source "$ HOME/.proxyman/proxyman_env_automatic_setup.sh" & & set + a
'''

3. proxyman \ _env \ _automatic \ _setup.sh是一个bash脚本，它定义了新的变量环境，帮助Proxyman.

例如:

* HTTP \_代理和HTTPS \_代理环境
* 路径
* RUBYLIB
* PYTHONPATH
* 节点 \_选项
* 全局 \_代理 \_HTTP \_代理

** NodeJS **:

1. Proxyman将一个新的节点目录前置到 $ PATH env中
2. Monkey-使用 [global-agent ](https://www.npmjs.com/package/ global-agent) 包修补节点，该包支持axios的HTTP代理，并开箱即用

** Ruby **:

1.覆盖 $ RUBYLIB到Proxyman应用程序
2.修补所有常见的库，例如http，net/http和net/https等-> 设置HTTP代理和信任代理自签名证书。

** Python **:

1.将 $ PYTHONPATH覆盖到Proxyman应用程序
2.修补所有常见的库，如aiohttp，httplib，http.client -> 设置HTTP代理和信任代理自签名证书。

** Go **:

1.覆盖HTTP \ _proxy & HTTPS \ _proxy env
2.覆盖一些Go env信任自签名证书

# #4.故障排除

请参见 [故障排除](https://docs.proxyman.com /自动-设置/故障排除) 页面
