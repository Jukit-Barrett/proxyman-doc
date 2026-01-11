# 安装证书

# # 在Windows上安装证书

为了拦截加密的HTTPS消息 (请求或响应)，您必须在当前的Windows计算机上安装 ** Proxyman CA证书 **。

您可以通过导航到安装Proxyman CA证书

* ** 证书 ** 菜单-> ** 在此Windows上安装证书 **...

{% 提示样式 = "info" %}
Proxyman证书是在您的计算机上生成的自签名证书。Proxyman从不将任何个人数据存储或传输到Proxyman的服务器或第三方。

请查看 [隐私声明](https:// proxyman.io/Privacy) 以了解Proxyman是否获得。

如果您想在您的计算机上手动生成证书，然后添加到Proxyman。请查看 [自定义证书文档](https://docs.proxyman.com /高级功能/自定义证书 #6-如何生成-自签名证书-自定义-根证书-符合-新-苹果-安全-要求)
{% endhint %}

# #1.自动模式

<figure><img src = "images/Screenshot_2023-01-23_at_09.38.09_9b5970f1.png" alt = ""><figcaption><p> 在Windows机器上自动安装证书 </p></figcaption></figure>

Proxyman提供了一个自动脚本来安装和信任Proxyman CA证书到系统。

* 证书菜单-> 安装此Windows的证书-> 单击 “安装和信任” 按钮
* 在系统提示中单击 “是”

<figure><img src = "images/Screenshot_2023-01-23_at_09_41_41_1842ac7d.jpg" alt = ""><figcaption><p> 授予运行自动脚本的权限 </p></figcaption></figure>

### 为什么我需要授予权限？

在幕后，Proxyman将在管理模式下执行以下命令:

'''bash
$ certutil -addstore "Root" <Certificate_Path>
'''

{% 提示样式 = "info" %}
[certutil](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil) 是用于管理证书的内置Windows命令行。
{% endhint %}

# #2.手动模式

如果您没有执行脚本的权限，请执行以下步骤:

1.关闭Proxyman
2.查找Proxyman CA证书在 “C:\ Users \\\< your \ _username>\ AppData \ Roaming \ Proxyman \ Certificate \ certs \ ca.cer”
3.双击打开
4.安装证书-> 选择 “当前用户”-> 选择 “将所有证书放在以下存储中”-> “浏览...”

<figure><img src = "images/212792551-e3875685-294b-46b4-b563-b3c7051fb29a_7bd0294b.jpg" alt = ""><figcaption><p> 证书安装步骤 </p></figcaption></figure>

5 \。选择下一步-> 完成

6 \。在系统提示中选择 “是”。
