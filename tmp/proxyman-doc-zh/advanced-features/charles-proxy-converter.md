# Charles Proxy转换器

# #1.什么事？

Proxyman能够将 “chls” 文件从Charles代理应用程序转换为Proxyman可以理解的 “har” 格式。

{% 提示样式 = "成功" %}
它需要查尔斯代理beis已经安装，以转换 “chls' 文件
{% endhint %}

您可以从文件菜单手动转换文件-> 转换-> 'chls' 到 'har'

![](图片/Screen_Shot_2020-05-03_at_18.31.39_b830382e.png)

# #2.它是如何工作的？

通常，Proxyman使用 [Convert CLI from Charles Proxy](https://www.charlesproxy.com/documentation/tools/ 命令行工具/) 进行转换。chls到。har，Proxyman可以理解。

1.只要你打开 'chls' 文件，Proxyman试图找到查尔斯代理应用程序，它有一个包ID是

'com.xk72.Charles'
2.使用Convert命令进行转换

'''
元。/Applications/Charles.app/Contents/MacOS/Charles convert ~/Desktop/input.chls ~/Desktop/output.har

'''

3 \。输出是 “har” 格式在您的桌面目录

# #3.如何使用？

有几种方法可以打开 “chls” 文件:

* 直接打开 “chl” 文件 (双击该文件，或从Finder应用程序打开)
* 拖放文件到Proxyman应用程序
* 文件-> 打开并选择 “chls' 文件
