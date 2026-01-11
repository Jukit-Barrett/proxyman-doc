# macOS

# # 在Mac上安装并信任Proxyman证书

为了拦截加密的HTTPS消息 (请求或响应)，您必须在当前计算机上安装 ** Proxyman CA证书 **。此步骤对于iOS、Android设备、iOS模拟器、Java vm和Firefox也是强制性的。

{% 提示样式 = "info" %}
Proxyman证书是在您的计算机上生成的自签名证书。Proxyman从不将任何个人数据存储或传输到Proxyman的服务器或第三方。

请查看 [隐私声明](https:// proxyman.io/Privacy) 以了解Proxyman是否获得。

如果您想在您的计算机上手动生成证书，请将其添加到Proxyman。请查看 [自定义证书文档](https://docs.proxyman.com /高级功能/自定义证书 #6-如何生成-自签名证书-自定义-根证书-符合-新-苹果-安全-要求)
{% endhint %}

{% 提示样式 = "info" %}
Proxyman的证书本地存储在 ** \ ~/Library/Application \ Support/com.proxyman.NSProxy/app-data/**
{% endhint %}

# #1.自动模式 (推荐)

Proxyman可以通过以下步骤 ** 自动 ** 安装并信任Keychain中的证书:

1.打开 ** 证书 ** 菜单
2.在这台Mac上安装证书...
3.在自动模式-> 输入您的Mac的密码 (Root权限)
4.验证状态:✅按钮中的 “已安装并受信任” (如果没有，请尝试使用 “手动” 选项卡，或与我们联系以获得进一步的支持)
5.完成: 白色 \_检查 \_标记:

![Install & trust Proxyman Certificacte](images/proxyman_install_ca_certificate_a54a52ac.jpg)

{% 提示样式 = "info" %}
** 自动化模式 ** 需要 ** Root权限 ** 来执行安装脚本。如果您不确定，请考虑使用手动模式。
{% endhint %}

### 它是如何工作的？

在自动模式下，Proxyman将自动执行两个步骤:

1.在 '~/Library/Application \ Support/com.Proxyman.NSProxy/app-data/proxyman-ca.pem' 处生成本地proxyman证书
2.安装并信任证书到系统钥匙串访问。它需要Root权限才能执行以下CLI:

{% code overflow = "wrap" %}

'''bash
sudo安全add-trusted-cert -d -r trustRoot -k /Library/keychain/System.keychain ~/Library/Application \ Support/com.proxyman.NSProxy/app-data/proxyman-ca.pem
'''

{% endcode %}

# #2.手动模式 (提前)

Proxyman还为需要代表其安装证书的超级用户提供了更多自由。

1.打开 ** 证书 ** 菜单
2.在此Mac上安装证书... -> 选择手动选项卡
3.单击 ** Generate & Add ** 按钮 (Proxyman会在本地生成证书并将其添加到Keychain，但不会自动信任它，不需要密码)
4.在某些情况下，系统钥匙串会要求选择应安装的钥匙串-> 选择 ** 系统钥匙串 **
5.在Mac上打开钥匙串访问应用程序-> 搜索 “Proxyman CA”-> 打开-> 选择 “始终信任”-> 退出钥匙串并保存

{% 提示样式 = "info" %}
如果你做得正确，Proxyman将显示“✅已安装和受信任 ”状态。
{% endhint %}

![手动安装Proxyman Certifiacte](图片/proxyman_install_manual_0ee61c07.jpeg)

{% 提示样式 = "info" %}
如果您想使用自己的自定义根证书，请查看 [自定义证书文档](https://docs.proxyman.com /高级功能/自定义证书 #6-如何生成-自签名证书-自定义-根证书-符合-新-苹果-安全-要求)
{% endhint %}

假设您不确定如何信任Keychain Access应用程序上的证书。您可以打开终端应用程序并执行命令:

{% code overflow = "wrap" %}

'''bash
sudo安全add-trusted-cert -d -r trustRoot -k /Library/keychain/System.keychain ~/Library/Application \ Support/com.proxyman.NSProxy/app-data/proxyman-ca.pem
'''

{% endcode %}

{% 提示样式 = "info" %}
如果您不再使用Proxyman，请确保 ** 删除钥匙串应用程序中的Proxyman证书 **。如果没有，任何拥有Proxyman证书的人都可以拦截来自您macOS计算机的HTTP/HTTPS请求。
{% endhint %}

# #3.卸载Proxyman证书

1.打开证书菜单
2.重置所有证书
3.输入您的Mac密码并完成
