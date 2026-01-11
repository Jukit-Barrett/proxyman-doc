# NodeJS

# #1.新的自动解决方案 (v4.7.0或更高版本)✅

Proxyman v4.7.0或更高版本可以通过1-click从NodeJS捕获HTTP/HTTPS流量。

* 1-click解决方案: 无需手动设置HTTP代理配置或信任自签名证书。
* 支持许多NodeJS库: axios，got，superagent，fetch和node-fetch

### 如何使用:

1.打开Proxyman -> 设置菜单-> 自动设置
2.点击 “打开新终端”
3.如果需要，接受Apple脚本权限提示
4.新的终端应用程序启动-> 您可以启动您的NodeJS后端服务器，或运行脚本 => Proxyman自动捕获所有流量。
5.例如:

'''
$ npm开始
'''

完成✅

<figure><img src = "images/CleanShot_2023-04-22_at_15.18.19_2x_5039dd93.jpg" alt = ""><figcaption><p> 捕获NodeJS流量 </p></figcaption></figure>

请查看自动设置页面:

{% content-ref url = "../automatic-setup/automatic-setup" %}
[自动设置](https://docs.proxyman.com /自动设置)
{% endcontent-ref %}

# #2.旧解决方案 (不推荐)❌

使用NodeJS + Proxyman时存在常见问题:

### 1.Proxyman无法将 <http:// localhost:3000> 请求捕获到我的NodeJS服务器

如果您使用NodeJS来服务本地主机网站 (例如 <http:// localhost:3000>)，Proxyman可能不起作用。例如: 使用ExpressJS为位于 <http:// localhost:3000> 的API服务器提供服务

### 解决方案:

请查看此解决方案。

### 2.Proxyman无法捕获HTTP请求，这是从我的NodeJS本地服务器调用。

* 我使用 [fetch](https://www.npmjs.com/package/ node-fetch) 或 [axios](https://github.com/axios/axios) 不显示在Proxyman应用程序
* 从HTTPS请求获取SSL错误

### 解决方案

默认情况下，从NodeJS库调用的所有HTTP/HTTPS请求都不会通过HTTP代理服务器。因此，Proxyman无法捕获流量。

### 1. node-fetch

1.安装 [global-agent](https://github.com/gajus/ global-agent) 软件包

'''bash
npm安装全局代理
'''

2 \。在NodeJS代码的顶部，添加以下代码:

'''javascript
从 'global-agent' 导入 {bootstrap}；
bootstrap();
process.env['NODE_TLS_REJECT_UNAUTHORIZED'] = '0';
'''

3 \。将此env添加到您当前的bash。确保Proxyman在9090端口监听

'''
导出GLOBAL_AGENT_HTTP_PROXY = http:// 127.0.0.1:9090
'''

4 \。完成✅

再次运行您的NodeJS脚本，HTTP/HTTPS请求将出现在Proxyman应用程序上。

#### 示例代码

'''javascript
从 'node-fetch' 导入fetch；

// Setup global-agent
从 'global-agent' 导入 {bootstrap}；
bootstrap();
process.env['NODE_TLS_REJECT_UNAUTHORIZED'] = '0';

// 获取数据
const响应 = await fetch('https:// httpbin.org/get？id= 123')；
const data = 等待response.json()；

// 完成
console.log (数据)；
'''

### 2.Axios

根据Axios文档，我们可以简单地提供HTTP \ _proxy和HTTPS \ _proxy环境。

1.单击Proxyman状态菜单
2. Copy Shell命令

<figure><img src = "images/Screenshot_2023-04-15_at_10.39.02_c5b14989.jpg" alt = ""><figcaption></figure>

3.打开终端并运行粘贴内容: 例如导出https \ _proxy =<http:// 192.168.1.103:9090> http \ _proxy =<http:// 192.168.1.103:9090>
4.在同一个终端上-> 使用axios启动您的NodeJS服务器
5. Axios将把流量代理给Proxyman。
6.完成✅

### 3.我使用不同的NodeJS库

如果您未使用fetch或axios，则配置可能会有所不同。请查看您的lib文档，了解如何设置代理并信任Proxyman证书。

* 讨论在 < https://github.com/ProxymanApp/Proxyman/issues/ 236>
