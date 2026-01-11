# 更新Proxyman应用程序后丢失数据？

### 问题

将应用更新到最新版本后，您可能会遇到:

* 您当前的数据，包括所有调试工具规则 (地图本地，脚本，断点，SSL代理列表，...) 和用户设置等被抹去。

{% 提示样式 = "info" %}
Proxyman将 ** 保证 ** 您当前的数据 ** 永远不会丢失 **。然而，它仍然更好，如果我们有你的宝贵数据的备份⚡️。
{% endhint %}

### 如何恢复

1.打开位于 “〜/Library/Application Support/com.proxyman.NSProxy/user-data-backups” 的备份文件夹
2.解压缩最新的备份文件 (您可以在Finder应用程序中按 “添加日期” 排序。它将显示最新的备份)。
3.将备份文件夹的每个文件夹复制到位于 '〜/Library/Application Support/com.proxyman.NSProxy' 的应用文件夹中

例如:

<table><thead><tr><th width = "186.4852062786498"> 从 </th><th> 复制到 </th></tr></thead><tbody><tr><td>~/Library/Application Support/com.proxyman。NSProxy/user-data-backups/userdata_proxyman_3.6.0_05-24-2022-11-55-20/user-data</td><td>~/Library/Application Support/com.proxyman.NSProxy/user-data</td></tr><td>~/Library/Application Support/com.proxyman.NSProxy/user-data-backups/userdata_proxyman_3.6.0_05-24-2022-11-55-20/map-local</td><td>~/Library/Application Support/com.proxyman.NSProxy/map-local</td></tr><td>></td></tr></tbody></table>

### Proxyman什么时候备份我的数据？

将Proxyman更新到较新版本后，Proxyman可能会备份当前数据并保存在 “~/Library/Application Support/com.proxyman.NSProxy/user-data-backups”
