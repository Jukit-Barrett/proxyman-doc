# 访问控制

# #1.什么事？

这是一项高级功能，它允许您定义远程设备 (iPhone，Android，其他计算机) 如何连接到Proxyman应用程序。它专为企业用户设计，以获得更好的安全性。

通过 ** 工具菜单 ** -> 代理设置-> 访问控制进行访问。

<table><thead><tr><th width = "169"> 模式 </th></tr></thead><tbody><tr><td> 允许所有 </td><td> 所有远程连接都可以连接到Proxyman (默认)。</td></tr><td> 不允许全部 </td><td> 所有远程连接都不允许连接到Proxyman。</td></tr><td> 通过IP指定远程设备 </td><td> 定义哪个设备可以连接到Proxyman应用程序。</td></tr></tbody></table>

<figure><img src = "images/Screenshot_2023-01-23_at_09.25.40_1037b189.png" alt = ""><figcaption><p> 访问控制UI</p></figcaption></figure>

<figure><img src = "images/Screenshot_2023-01-19_at_14.31.47_3967ac76.png" alt = ""><figcaption><p> 允许未授权连接 </p></figcaption></figure>

# #2.通过命令行覆盖访问控制模式

从Proxyman 4.4.0，可以通过以下CLI覆盖访问控制。

如果您的公司在不使用GUI的情况下强制执行模式，这很有用。

'''
$ defaults写入 ~/Library/Preferences/com.proxyman.NSProxy.plist accessControlModeString "allowAll"
$ defaults写入 ~/Library/Preferences/com.proxyman.NSProxy.plist accessControlModeString "disallowAll"
$ defaults写入 ~/Library/Preferences/com.proxyman.NSProxy.plist accessControlModeString "specificIP"
'''
