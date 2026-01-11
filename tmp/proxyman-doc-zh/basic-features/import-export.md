# 导入/导出

### 1.导入

Proxyman支持来自Proxyman和Charles Proxy的多个流量日志文件。

* ** Proxyman Log **: 内置Proxyman日志，包含所有请求和响应信息。
* Proxyman会话: 从Proxyman应用程序导出的整个工作会话文件。
* ** HAR 1.2 ** ([HTTP Archive](https://en.wikipedia.org/wiki/HAR_\(file_format \ ))): 适用于将HTTP请求和响应传输到其他应用程序，以供以后的检查器使用。完全支持Charles、Google Chrome、Safari、Firefox和其他网络分析器应用。
* ** 查尔斯代理日志 **: 从查尔斯代理应用程序导出的查尔斯日志。文件扩展名为 ** chls **。
* ** CSV文件 **: 将选定的请求导出为CSV文件 (Proxyman 2.29.0 +)
* ** 适用于iOS的Charles代理日志 ** (Proxyman 2.30.0 +): 文件扩展名为 ** chlsj **。
* 出口为邮递员集合2。

如果您想保存整个工作会话，请阅读保存会话页面。

{% content-ref url = "../advanced-features/save-session" %}
[保存-会话](https://docs.proxyman.com /高级-功能/保存-会话)
{% endcontent-ref %}

{% content-ref url = "../advanced-features/charles-proxy-converter" %}
[查尔斯代理转换器](https://docs.proxyman.com /高级功能/查尔斯代理转换器)
{% endcontent-ref %}

### 2.出口

您可以导出:

* 选定的请求或响应的列表。
* 来自特定客户端或域节点或远程设备的所有流量。
* 整个工作会议。
* 导出为Proxyman日志或ProxymanSession，身体或原始选项卡。

导出bug请求非常有用，您可以稍后进行调查或将其发送给QA团队。

### 3.通过命令行导入和导出

Proxyman提供了一个有用的命令行，可帮助您通过bash脚本执行导入/导出操作。

{% content-ref url = "../command-line" %}
[命令行](https://docs.proxyman.com /命令行)
{% endcontent-ref %}

### 4.如何使用

#### 4.1将文件导入到Proxyman

* ** 拖放 ** 文件到Proxyman窗口
* 文件-> 打开-> 选择一个文件

导入的文件将添加到Pin部分，您可以在其中检查所有流量。

#### 4.2导出到文件

有多种方法可以将选定的请求导出到文件:

* 在主表视图上选择请求和响应-> 右键单击-> 导出
* 右键单击应用程序或域-> 导出

![](图片/Screen_Shot_2021-08-27_at_13_56_53_2b3f6030.png)
