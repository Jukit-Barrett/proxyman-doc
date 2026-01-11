# 自定义证书

### 1.什么事？

Proxyman支持自定义 ** 根证书 ** 、 ** 服务器证书和 ** ** 客户端证书 **，允许您添加Proxyman用于在客户端、服务器和Proxyman应用程序之间建立SSL连接的证书。

| 自定义证书类型 | 用途 | Proxyman如何使用 |
| ----------------------- | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| ** 服务器证书 ** | 用于拦截来自使用ssl-pinning的客户端的HTTPS流量 | 使用此证书与您的客户端进行ssl-handshake |
| ** 客户端证书 ** | 用于拦截来自使用相互身份验证的客户端的HTTPS流量 | 使用此证书与特定服务器进行SSL握手 |
| ** 根证书 ** | 用于在不使用本地代理证书的情况下拦截来自客户端和服务器的HTTPS流量 | 客户端和服务器的SSL握手 |

![](图片/Screen_Shot_2020-09-09_at_15.52.42_d6d117ba.png)

{% 提示样式 = "info" %}
即使Proxyman根证书是在您的计算机中本地生成的，您也可以手动生成并添加到Proxyman。[阅读更多](#6-如何生成-自签名-证书-那-满足-苹果-要求)
{% endhint %}

### 2.证书格式

Proxyman接受以下格式:

| 自定义证书 | PEM或DER | PKCS #12 (p12) |
| ------------------ | ------------- | -------------- |
| 根证书 | 不支持 |
| 客户端证书 | 支持 |
| 服务器证书 | 支持 |

* PKCS #12 (p12)。
* PEM或DER私钥和证书文件。

{% 提示样式 = "info" %}

* Proxyman自动确定私钥和证书文件的格式 (支持PEM或DER)。
* 如果导入加密的私钥或PKCS #12文件，Proxyman将提示输入密码。
* 所有密码安全地存储在Proxyman钥匙串中。
{% endhint %}

{% 提示样式 = "info" %}
如果您的证书采用Proxyman支持的不同格式，请在导入之前将其转换为p12或PEM/DER格式。
{% endhint %}

### 3.macOS 10.15 + 和iOS 13 + 上的证书要求

如果您在macOS 10.15或iOS 13上使用自定根证书或服务器证书，如果不满足以下要求，您可能会在Safari或iOS设备上遇到握手失败的问题:

* RSA密钥的密钥大小必须大于2048位
* 哈希算法是SHA-2族
* 服务器的DNS名称必须存在于主题备用名称中。公用名不再受信任
* 有效证书 (当天不在之前和之后)
* TLS服务器证书必须包含ExtendedKeyUsage (EKU) 扩展，其中包含 ** id-kp-serverauth ** OID。

阅读更多 < https://support.apple.com/en-us/HT210176>

{% 提示样式 = "info" %}
如果它对你来说太复杂了，我们建议让Proxyman自动执行它。请访问证书菜单-> 在此Mac上安装证书-> 选择 ** 自动 ** 选项卡。
{% endhint %}

### 4.常见问题

| 问题 | 解决方案 |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 私钥和证书不匹配 | 尝试不同的证书和私钥并确保它们匹配 |
| 获取自定义证书的SSL握手错误 | <ul><li> 尝试将自定义证书添加到系统钥匙串并信任它 </li><li> 证书与macOS的要求不匹配 => 阅读 <a href = "#3-certificate-requirement-on-macos-10-15-and-ios-13"> 第3节 </a></li><li> 检查证书到期日 </li></ul> |
| 由于密码短语无效，无法导入证书 | 要求您的主管提供正确的密码短语以打开加密的私钥或P12文件 |

### 5.如何使用

* 从 ** 证书菜单访问 ** -> ** 添加自定义证书 **

![](图片/Screen_Shot_2021-07-31_at_20.21.35_3e6d79cd.png)

### ** 6.如何为符合新Apple安全要求的自定义根证书生成自签名证书 **

由于 [来自iOS 13和Catalina (10.15) 的Apple要求](#3-certificate-requirement-on-macos-10-15-and-ios-13)，它需要额外的配置才能正确生成自签名证书。

以下步骤将指导您如何正确执行此操作:

1.在 ** 桌面文件夹 ** 上准备一个 “cert.Config” 文件

'''
[ca]
default_ca = CA_default
[CA_default]
default_md = sha256
[v3_ca]
subjectKeyIdentifier = 哈希
authorityKeyIdentifier = keyid: 始终，颁发者
basicConstraints = critical,CA:true
keyUsage = 关键，keyCertSign
extendedKeyUsage = serverAuth,clientAuth
[要求]
提示 = 否
distinguished_name = req_distinguished_name
[req_distinguished_name]
C = 美国
L = US
O = Proxyman LLC
CN = proxyman.de v
OU = 代理人
'''

* 请更新C、L、O、CN和OU参数的值。

2 \。在终端应用程序中生成RSA密钥。(将 ** 您的 \_密码 ** 替换为任何密码，例如123456)

'''bash
cd ~/桌面
openssl genrsa -aes256 -passout pass:your_password -out key.pem 2048
'''

3 \。生成自签名证书和私钥。(将 ** 您的 \ _password ** 替换为步骤2中的密码)

'''
openssl req -x509 -new-nodes-passin pass:your_password -config cert.Config-key key.pem -sha256 -extensions v3_ca -days 825 -out root-ca.pem
'''

4 \。转换为p12格式。(将 ** 您的 \ _password ** 替换为步骤2中的密码)

'''
openssl pkcs12-export-legacy-out root-ca.p12 root-ca.pem密钥。pem-passin pass:your_password -passout pass:your_password
'''

5 \。最后，您将有 ** root-ca.p12 ** 文件并移动到下一步

{% 提示样式 = "info" %}
如果您无法在macOS 14 (OpenSSL v3) 或更高版本上导入自定义证书，则应在步骤4中使用 \ '-legacy \' 标志。

参考: <https://stackoverflow.com/questions/ 70431528/mac-verification-failed-during-pkcs12-import-wrong-password-azure-devops>
{% endhint %}

### 7.导入为自定义根证书

1.转到证书菜单-> 自定义证书-> 选择根证书选项卡
2.点击 ** 导入 ** 按钮-> P12
3.选择 ** root-ca.p12 ** 文件并输入密码。
4.在Keychain Access应用程序中信任您的自定义证书:

* 打开钥匙串访问应用程序
* 搜索您添加的证书。名称可能是证书的公用名 (CN)
* 双击打开并选择始终信任
* 单击 “X” 并保存更改

![](图片/Screen_Shot_2020-09-09_at_06.30.51_3d017eb7.png)

5 \。请验证您是否可以看到显示证书已正确安装和信任的绿色勾号。

![已正确安装并信任自定义根证书。准备就绪!](图像/Screen_Shot_2020-09-09_at_20.52.39_8d6996e4.png)

### 8.作为服务器/客户端证书导入

对于自定义服务器/客户端证书，不应生成自签名证书。请向您的同事或团队负责人询问公司正在使用的证书。它可以是DER/PEM或P12格式。

然后在 “自定义证书” 窗口中将证书作为服务器/客户端证书导入。

![将PEM/DER密钥和私钥导入自定义客户端/服务器证书] (图片/Screen_Shot_2020-06-26_at_10.54.35_52af878c.png)

{% 提示样式 = "info" %}
您不需要信任系统钥匙串上的证书，因为它不是根证书。
{% endhint %}
