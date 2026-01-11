# Map Local (目录)

# #1.什么事？

这是一个方便的工具，可以将匹配的请求映射到选定目录上的本地文件。如果本地文件不存在，它将从真实服务器提供服务。

如果要映射本地文件，请查看 “映射本地 (文件)” 页面

{% content-ref url = "map-local" %}
[地图-本地](https://docs.proxyman.com /高级功能/地图-本地)
{% endcontent-ref %}

# #2.如何使用

### 2.1映射路径及其子目录

'api.proxyman.io/build/v1/* '=>'/v1/'之后的所有子路径都将映射到选定的目录。

例如，我们选择 “~/desktop/my_folder” 作为本地目录

| 真实URL | 解析的本地路径 |
| -------------------------------------------- | -------------------------------- |
| <http:// api.proxyman.io/build/v1/index.html> | \ ~/desktop/my \_folder/index.html |
| <http:// api.proxyman.io/build/v1/js/main.js> | \ ~/desktop/my \_folder/js/main.js |

#### 如何配置

| 规则 | 如何使用 | 示例 |
| -------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| 通配符 | <ul><li> 选中 “包含子路径” 复选框 </li><li> 或在URL</li></ul> 的末尾使用/\ * | <ul><li>api.proxyman.io/build/v1/ (检查)</li><li>api.proxyman.io/build/v1/\ *</li></ul> |
| Regex | <ul><li> 在末尾使用 (.\ *)</li></ul> | <ul><li><https:// api.proxyman.io/build/v1/(>.*)</li><li><https:// api.proxyman.io/build/v1/(>.*.css)</li></ul> |

{% 提示样式 = "info" %}
确保你使用 '()' 组正则表达式运算符告诉Proxyman在哪里映射
{% endhint %}

### 2.2映射整个主机

'api.proxyman.io/* '=> 所有子路径都将映射到选定的目录。

例如，我们选择 “~/desktop/my_folder” 作为本地目录

| 真实URL | 解析的本地路径 |
| -------------------------------------------- | ----------------------------------------- |
| <http:// api.proxyman.io/build/v1/index.html> | \ ~/desktop/my \_folder/build/v1/index.html |
| <http:// api.proxyman.io/build/v1/js/main.js> | \ ~/desktop/my \_folder/build/v1/js/main.js |

#### 如何配置

| 规则 | 如何使用 | 示例 |
| -------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| 通配符 | <ul><li> 将路径留空 </li></ul> | <ul><li>api.proxyman.io</li></ul> |
| Regex | <ul><li> 使用末尾包含 (.\ *) 的单个路径 </li></ul> | <ul><li><https:// api.proxyman.io/(>.*)</li><li><https:// api.proxyman.io/(>*.html)</li></ul> |

# #3.使用脚本工具映射本地Directoy

如果您想使用 ** 复杂的规则映射本地目录，** 您可以查看 [脚本](https://docs.proxyman.com/scripting/script# 1-whats-it)，因为它更容易实现相同的结果。

请查看我们的 [代码片段](https://docs.proxyman.com/scripting/ 代码片段-代码 #2-common-on-request-and-response)，了解如何使用Javascript代码映射本地文件。
