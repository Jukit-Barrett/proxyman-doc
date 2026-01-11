# 手动设置

# #1.问题

Proxyman ** 无法从以下设置捕获 ** HTTP/HTTPS流量:

* ** NodeJS **: Axios、tot、superagent、fetch和node-fetch
* Python: http，https，aiohttp，请求
* 红宝石: http，net/http，net/htps，法拉第，httpparty和fastlane
* 卷曲

这是一个已知的问题，因为从终端应用程序执行的NodeJS，Python，Ruby和cURL，不尊重系统HTTP代理。因此，Proxyman上没有流量。

您必须阅读每个库的技术文档并手动配置:

* HTTP代理
* 信任自签名证书

\=> 耗时且容易出错❌

# #2.解决方案: 手动设置

### 好处:

*✅在您最喜欢的终端应用程序上运行: iTerm2与Bash，Zsh和鱼壳
* 从NodeJS，Python，Ruby，终端或Web浏览器等捕获HTTP(s) 流量
* 安全。在当前会话上工作，不会影响您的操作系统

### 如何使用:

1.打开Proxyman -> 设置菜单-> 手动设置
2.打开自己喜欢的终端app，比如iTerm2
3.复制和粘贴脚本到您的终端-> 运行它
4.完成✅
5.您可以启动后端服务器或运行脚本 => Proxyman自动捕获开箱即用的所有HTTP/HTTPS流量

<figure><img src = "images/CleanShot_2023-04-22_at_15.23.20_2x_d2edfbbd.jpg" alt = ""><figcaption><p> 手动设置 </p></figcaption></figure>

### 支持库:

Proxyman (手动设置) 可以使用以下网络库开箱即用。

* NodeJS: [axios](https://www.npmjs.com/package/axios )，[fetch](https://nodejs.org/dist/ latest-v18.x/docs/api/globals.html # fetch) (v18)，[node-fetch](https://www.npmjs.com/package/ node-fetch)，[got](https://www.npmjs.com/package/got )，[https](https://nodejs.org/api/https.html )，和 [超级代理](https://www.npmjs.com/package/superagent)
* 红宝石: [http](https:// ruby-doc.org/stdlib-3.0.2/libdoc/net/http/rdoc/Net/HTTP.html)，[net/http](https:// ruby-doc.org/stdlib-2.7.0/libdoc/net/http/rdoc/Net/HTTP.html)，[net/https](https:// ruby-doc.org/stdlib-2.7.0/libdoc/net/http/rdoc/Net/HTTP.html) 、 [httpparty](https://github.com/jnunemaker/httparty) 、 [faraday](https://github.com/lostisland/faraday) 和fastlane
* Python: [请求](https://pypi.org/project/requests/ )，[aiohttp](https://docs.aiohttp.org/en/stable/ )，http.client，urllib3和httpx
* 没有 -- proxy标志的cURL

# #3.高级: 它是如何工作的？

请参阅 [自动设置: 它是如何工作的？](https://docs.proxyman.com /自动设置 #3.-高级-它是如何工作的)

# #4.故障排除

请参见 [故障排除](https://docs.proxyman.com /自动-设置/故障排除) 页面
