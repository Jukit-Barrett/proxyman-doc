# 请求/响应预览器

在域或客户端上安装 [证书](https://docs.proxyman.com /调试设备/macos) 并启用 [HTTP响应](https://docs.proxyman.com /基本功能/ssl代理) 后，您的网络流量将立即显示在Proxyman窗口内，分为三个主要区域:

* 左侧面板上的源列表
* 中间面板上的流程列表
* 右侧面板上的流内容

![](图像/01_f952e95e.png)

### 正文内容预览器

取决于请求或响应的内容: Proxyman将自动显示在单独的选项卡中:

* ** Header **: 所有Header (键值表)
* ** Cookie **: ** Cookie ** 标头中的键
* ** Set-Cookie ** 用于响应中的Set-Cookie标头
* ** Auth **: ** Authentication ** header中的key
* ** Body **: 消息的正文: Proxyman会根据 ** content-Type ** 自动格式化和美化正文内容，例如JSON，PNG，GIF，Raw Data，...
* ** 查询 **: 如果请求有查询，则显示所有查询。
* ** Raw **: 原始HTTP消息。
* Protobuf消息
* MessagePack
* 多部分/表单数据

### 自定义预览器选项卡

可以自定义您希望看到的预览器选项卡

* 自定义选项卡将持久的请求/响应面板
* 尝试解码和美化内容

{% content-ref url = "custom-previewer-tab" %}
[自定义预览选项卡](https://docs.proxyman.com /基本功能/自定义预览选项卡)
{% endcontent-ref %}

![自定义预览器选项卡] (图像/Screen_Shot_2021-06-25_at_09.39.55_80b3ed3e.png)

### 布局模式

有两种排序请求/响应面板的方法: 垂直或水平布局

![请求/响应面板](images/http_response_vertical_fac8606f.png)

![水平布局中的预览器] (图像/Screen_Shot_2020-04-25_at_16.21.34_04721f79.png)

![垂直布局中的预览器] (图像/Screen_Shot_2020-04-25_at_16.21.55_71a2efc4.png)

### 自定义工作区

您可以使用应用程序右上角的自定义布局按钮将内容显示为您的首选项

1.折叠/展开源列表面板
2.在新窗口中打开请求/响应面板
3.在水平布局中显示请求/响应面板
4.在垂直布局中显示请求/响应面板

![](images/02_56e68ced.png)

### 快捷方式

所有部分都支持 ** 复制 ** 和多个选择

![](图片/Screen_Shot_2019-08-17_at_10.04.36_09568bf2.png)

阅读更多在我们的 [Proxyman键盘快捷键](https:// proxyman.io/博客/2019/08/Proxyman-keyboard-shortcuts.html) 博客

### ** 正文预览器 **

Body previewer自动美化内容，并提供方便的次要功能:

* ** 树视图 **: 以树视图模式表示JSON
* ** 十六进制 **: 以十六进制格式显示正文
* ** 仅导出正文 **: 能够将正文内容导出到文件。适用于原始数据或二进制数据
* ** 使用 ** 打开: 您可以使用自己喜欢的编辑器打开正文内容。** Sublime Text ** 是mime ü ò ç

![](图片/body_previewer_8fe8223b.png)

### JSON树视图模式

Proxyman支持本机JSON树视图模式，该模式显示JSON正文。它允许开发人员:

* 通过 [JSON路径] 搜索JSON ( https://docs.proxyman.com /基本功能/jsonpaths)
* 复制JSON节点像谷歌开发者工具。

![](图片/Screen_Shot_2021-10-15_at_16.14.44_04bb9b21.png)
