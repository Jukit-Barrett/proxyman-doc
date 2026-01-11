# 撰写新请求

# #1.什么事？

“撰写新请求” 工具是一个方便的工具，以帮助开发人员:

* 编写HTTP/HTTPS请求并将其发送到您的服务。它类似于爪子，失眠和邮递员。
* 快速测试您的api，而不依赖于您的应用程序客户端。
* 支持头，查询，URL，表单，JSON正文
* 支持原始消息
* 支持多部分身体
* 预设模板: 空请求，GET请求，带有JSON或表单的Post请求。

{% 提示样式 = "info" %}
您可以将请求数据重复用于新请求。请查看 [编辑和重复](https://docs.proxyman.com /高级-功能/编辑和重复) 页面。
{% endhint %}

<figure><img src = "images/Screenshot_2025-09-05_at_21.01.54_fb448b1e.png" alt = ""><figcaption><p> 使用Proxyman进行HTTPS请求 </p></figcaption></figure>

# #2.如何使用

您可以通过以下方式打开该工具:

* 单击主导航栏上的撰写按钮
* 工具-> 撰写

![打开合成工具] (图像/Screen_Shot_2022-06-23_at_15_03_44_a3bc8558.jpg)

1.输入URL
2.选择HTTP方法
3.修改Header，Param，Body，Raw消息
4.单击 “发送” 按钮。

![撰写JSON正文] (图像/Screen_Shot_2022-06-23_at_15_07_35_c5105d9d.jpg) ![使用原始消息] (图像/Screen_Shot_2022-06-23_at_15_08_10_880d81e3.jpg)

# #3.模板

Proxyman还支持一些请求模板。

* GET与查询
* 使用JSON发布
* 用表格张贴
* 与多个Post
* 从cURL导入

![使用预设模板] (图片/Screenshot_2025-02-01_at_10.45.59_PM_1e2b9062.jpg)

# #4.从cURL导入

您可以导入cURL，您可以从Google Chrome中的网络选项卡复制该cURL，并使用撰写工具发出请求。

<figure><img src = "images/Screenshot_2025-02-01_at_10.42.21_PM_2a2ab38d.jpg" alt = ""><figcaption><p> 导入cURL</p></figcaption></figure>

{% 提示样式 = "成功" %}
您可以简单地将cURL粘贴到URL文本视图，Proxyman将尝试解析您的cURL
{% endhint %}

# #5.历史记录请求

在Proxyman macOS 5.24.0中，Proxyman会将您的请求/响应存储在历史记录列表中。

* Â œ… 有用预览您以前的请求/响应

<figure><img src = "images/Screenshot_2025-08-25_at_14.02.04_7e97076d.jpg" alt = ""><figcaption><p> Compose视图中的请求历史记录 </p></figcaption></figure>

# #6.设置

* ** SettingsRequest超时 **: 在设置-> 工具选项卡-> 请求超时中: 定义请求将超时的第二秒。使用0禁用它。在Proxyman 4.13.0或更高版本上可用
