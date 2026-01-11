# 自定义预览器选项卡

# #1.什么事？

您可以自定义 “自定义预览器” 选项卡，这些选项卡始终一次呈现一种格式。

这个方便的工具可能会帮助您解决以下问题:

* 将正文格式化为 ** JSON **，但内容类型不是 'application/json'
* 将正文格式化为 ** Protobuf **，但内容类型不是 “application/x-protobuf”
* 在Web视图上呈现HTML页面
* ** 美化 ** 缩小的文件 (HTML，CSS，JS)
* 多部分/表单数据
* 尝试将正文格式化为所选类型，而不考虑 “Content-type”
* 将MessagePack (msgpack) 转换为JSON
* [代码生成器](https://docs.proxyman.com /高级功能/代码生成器) 到Swift，Node，Javascript，cURL，...
* GraphQL查询更漂亮

<div data-full-width = "false"><figure><img src = "images/Screenshot_2024-06-27_at_15.01.33_20195768.png" alt = "" width = "563"><figcaption><p> 为请求/响应面板选择自定义选项卡 </p></figcaption></figure></div>

{% 提示样式 = "info" %}
选定的自定义选项卡将附加到请求或响应视图的右侧
{% endhint %}

<figure><img src = "images/CleanShot_2024-06-27_at_15.04.11_2x_9cda9736.jpg" alt = ""><figcaption><p> 显示自定义标签页 </p></figcaption></figure>

# #2.如何使用它？

您可以访问自定义预览器窗口:

1.单击请求/响应栏上的 “+” 按钮或 (从 “工具” 菜单-> “自定义预览器” 选项卡...)
2.单击复选框以显示/隐藏自定义选项卡
3.新选项卡将出现在请求或响应面板上✅

### 2.1服务器发送的事件和OpenAI选项卡

从Proxyman 5.22.0或更高版本，Proxyman支持

* 来自OpenAI端点的服务器发送的事件: 自动美化数据事件的内联JSON
* OpenAI Tab: 自动累积内容并显示最终结果，类似于聊天视图的输出。

<figure><img src = "images/1_5a33d494.jpg" alt = ""><figcaption><p> 捕获OpenAI端点 </p></figcaption></figure>

##3.⚡️ Advance: 使用脚本工具创建自定义选项卡

*✅在选项卡上显示您自己的数据
* 如果你想解码你的身体或显示部分身体你的自定义选项卡是有用的

### 如何使用:

1.单击请求/响应栏上的 “+” 按钮或 (从 “工具” 菜单-> “自定义预览器” 选项卡...)
2.选择 “添加自定义选项卡” 按钮
3.选择请求/响应面板并为选项卡设置名称

<figure><img src = "images/Screenshot_2024-06-27_at_15.01.51_6b57e773.png" alt = ""><figcaption></figure>

4.单击 “...” 按钮以显示Javascript代码

<figure><img src = "images/343035426-24d2901d-10e3-4fa0-a472-579df7385358_e4bb0869.jpg" alt = ""><figcaption><p> 显示Javascript代码 </p></figcaption></figure>

5.工具-> 脚本-> 添加新规则-> 使用此代码显示您自己的数据

<figure><img src = "images/343035431-1a336092-5c50-4e23-afbb-9a41f9679bb9_4ede2b9c.jpg" alt = ""><figcaption><p> 编写显示数据的代码 </p></figcaption></figure>

6.完成

<figure><img src = "images/343035436-dc7e6346-9ac6-4601-b07a-8294de2c4a02_90903fb4.jpg" alt = ""><figcaption><p> 在新选项卡上显示数据 </p></figcaption></figure>

# #4.示例

#### 强制渲染JSON TreeView

Proxyman支持JSON树视图以实现更好的可视化

![](图像/JSON_66862117.png)

我们可以通过右键单击列标题来显示/隐藏某个列

![](images/JSON_Col_3765cf10.png)

#### 强制渲染HTML页面

![](图片/Screen_Shot_2020-07-14_at_10_19_51_e03c4566.png)

#### 美化Javascript文件

![美化JS Body](图片/Screen_Shot_2020-07-12_at_08_40_52_1c6e8d60.png)
