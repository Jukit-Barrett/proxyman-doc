# Map Local for iOS教程

# # M ** 使用Proxyman地图本地工具在iPhone上启用HTTP(s) 响应 **

自2.0.0版以来，Proxyman引入了Map Local工具，该工具使开发人员可以使用本地文件的内容作为对您请求的响应，因为它们与您的规则匹配。

<figure><img src = "images/image_05725211.png" alt = ""><figcaption></figcaption></figure>

Map Local工具可以显着提高您的开发速度，并提供在多个边缘环境下快速测试的功能，而无需明确更新服务器中的数据。如果您想通过各种响应测试应用程序的行为，它也是QAs或开发人员的必备工具。一些测试场景:

* 定义响应并将其用作匹配请求的响应
* 在响应中快速尝试新参数。
* 使用响应中的不同参数测试应用的行为。
* 使用异常内容测试UI布局。
* 在响应中使用特定参数快速重现错误。
* 使用本地文件模拟假API: 对于开发人员来说，这很有用，他们会尝试不在生产环境中的测试API。

# # 先决条件

* 已经在AppStore上下载了最新版本的Proxyman: <https://apps.apple.com/us/app/proxyman/ id1551292695>
* 已经在iOS设备上安装并信任Proxyman证书 (如果您是Proxyman的新手，请按照 [本教程](https:// proxyman.io/posts/2021-10-17-Getting-Started-With-Proxyman-For-iOS) 如何开始拦截iPhone上的HTTP流量)。

# # 创建地图本地规则

有两种方法可以定义断点规则:

1.从设置屏幕

* 转到设置 → 地图本地 → 点击按钮。
* 从这里开始，我们将需要手动填写规则的所有必填字段，包括标题，方法，匹配URL，以及是否包含子路径。

<figure><img src = "images/image_63d4ba56.png" alt = ""><figcaption></figcaption></figure>

2.从菜单上下文

* 长按请求 → 添加到地图本地列表。
* 它会自动填写所有字段，以根据所选请求定义规则。

<figure><img src = "images/image_396ab72c.png" alt = ""><figcaption></figcaption></figure>

#### 修改表头、状态码和正文

从地图本地编辑器屏幕，我们可以自由地操作标题，状态代码和正文数据。如果我们用新的数据类型替换正文，Proxyman将自动检测内容类型并为我们更新标题。

<figure><img src = "images/image_18847dd9.png" alt = ""><figcaption></figcaption></figure>

# # 使用地图本地工具操纵响应

<figure><img src = "images/image_c7ffcb64.png" alt = ""><figcaption></figcaption></figure>

你们都准备好了，是时候再提出一个要求，看看它是如何工作的。

如果传入请求的URL与 ** 预定义的匹配规则 ** 匹配，并且本地文件有效 => 这些匹配请求的正文响应将自动替换为本地文件的内容。

如果请求不匹配任何规则，则整个响应的内容将保留在服务器上。

<figure><img src = "images/image_07927739.png" alt = ""><figcaption></figcaption></figure>

干得好!如果您查看流列表，您会发现一个蓝色的小图标，表示此流已被修改。如您所见，两个响应内容都已使用本地文件进行了更新。

# # 下一步是什么

Map Local工具允许您尝试各种类型的响应来测试设备的布局或内容，从而提高调试效率，但仅限于修改响应内容的功能。如果您想修改请求内容，您可能需要查看我们的 [断点教程](https:// docs.proxyman.io/proxyman-ios/tutorial-for-ios/breakpoint-for-ios-tutorial)，使我们能够在不改变客户端任何逻辑的情况下即时操作请求和响应。
