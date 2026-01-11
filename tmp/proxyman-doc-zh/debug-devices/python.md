# Python

# #1.新的自动解决方案 (v4.7.0或更高版本)✅

Proxyman v4.7.0或更高版本可以通过1-click从Python捕获HTTP/HTTPS流量。

* 1-click解决方案: 无需手动设置HTTP代理配置或信任自签名证书。
* 支持许多Python库: 请求，http.client，urllib3，httpx和aiohttp

### 如何使用:

1.打开Proxyman -> 设置菜单-> 自动设置
2.点击 “打开新终端”
3.如果需要，接受Apple脚本权限提示
4.新的终端应用程序启动-> 您可以启动您的Python后端服务器，或运行脚本 => Proxyman自动捕获所有流量。
5.完成✅

<figure><img src = "images/CleanShot_2023-04-22_at_15.18.19_2x_5039dd93.jpg" alt = ""><figcaption><p> 使用Proxyman捕获NodeJS流量 </p></figcaption></figure>

请查看自动设置页面:

{% content-ref url = "../automatic-setup/automatic-setup" %}
[自动设置](https://docs.proxyman.com /自动设置)
{% endcontent-ref %}

# #

# #2.旧解决方案 (不推荐)❌

### 1.脚本方法

1.使用 [以下脚本](https://github.com/ProxymanApp/Proxyman/issues/ 1220 # issuecomment-1249090359) 自动安装/删除证书到Python。
2.将脚本保存到 \ ~/desktop文件，名称为 'script.py'

* 添加证书:

'''bash
$ python3脚本.py添加
'''

* 删除证书

'''
$ python3 script.py删除
'''

{% 提示样式 = "info" %}
对于macOS 12.2或更高版本，请确保使用 “python3”

[@ novitae](https://github.com/novitae)
{% endhint %}

### 2.手动进近

###-在Python环境中安装Proxyman

默认情况下，macOS上的Python不信任Proxyman自签名证书。因此，如果您尝试拦截HTTPS流量，则可能会遇到SSL错误。

如果你想从你的Python脚本拦截HTTPS流量，你必须明确地 ** 告诉Python使用Proxyman根证书 ** 在 '~/.proxyman/proxyman-ca.pem'

请遵循以下准则:

1.在Mac上安装Proxyman证书 (如果您已经完成，请跳过它。如果没有，请查看 [MacOS指南](https://docs.proxyman.com/macos# Install-certificates-on-macos))。
2.在终端应用上运行以下CLI

'''bash
$ export SSL_CERT_FILE = ~/.proxyman/proxyman-ca.pem
$ export REQUESTS_CA_BUNDLE = ~/.proxyman/proxyman-ca.pem
$ echo "export REQUESTS_CA_BUNDLE = ~/.proxyman/proxyman-ca.pem" >> ~/.bash_profile; 源 ~/.bash_profile
'''

3 \。完成。

###-还原更改

如果您不使用Proxyman，请通过注释恢复更改:

'''bash
# export REQUESTS_CA_BUNDLE = ~/.proxyman/proxyman-ca.pem
'''

在 \ ~/.bash \_配置文件中

# #3.故障排除

#### 3.1 Proxyman无法从我的Python代码捕获HTTP流量。

** 解决方案 **: 请使用 [自动设置](https://docs.proxyman.com /自动设置)。

### 参考

* <https://github.com/ProxymanApp/Proxyman/issues/ 948 # issuecomment-890520435>
* <https://github.com/ProxymanApp/Proxyman/issues/ 1220>
