# React Native

# #1.React Native - iOS

* 如果您在iOS应用中使用React Native，则只需遵循iOS指南即可。与iOS本机应用程序没有区别。
* 与Expo或Metro bundler一起工作

{% content-ref url = "ios-device" %}
[ios设备](https://docs.proxyman.com /调试设备/ios设备)
{% endcontent-ref %}

{% content-ref url = "ios模拟器" %}
[ios模拟器](https://docs.proxyman.com /调试设备/ios模拟器)
{% endcontent-ref %}

# #2.React Native - Android

基本上，要从React Native for Android应用程序捕获HTTP/HTTPS流量，它类似于本机Android应用程序。请按照Android设置指南:

* [Android物理设备](https://docs.proxyman.com /调试设备/android设备)
* [Android模拟器](# android模拟器)

{% 提示样式 = "警告" %}
确保您已遵循指南中的所有步骤，尤其是 ** 第5步 **，在其中添加 ** res/xml/network \_security \_config.xml ** 和 ** AndroidManifest.xml **

否则，Proxyman无法解密SSL连接。
{% endhint %}

# #3.故障排除-Android

### 3.1 Metro捆绑包错误

将Android的HTTP代理设置为Proxyman后，您可能会遇到以下错误，因为Metro Bundle无法连接到其本地服务器。

<figure><img src = "images/Screenshot_2023-04-06_at_07.58.01_02b45d28.png" alt = ""><figcaption><p>Metro bundle错误 </p></figcaption></figure>

要修复它:

#### Android模拟器

1.打开Proxyman -> 证书菜单-> 安装为Android -> 模拟器-> 点击 “恢复代理”
2.打开Android模拟器-> 设置应用程序-> 网络-> Wifi -> 找到更改代理的方法
3.使用 ** Proxyman IP & Port ** 手动更改HTTP代理。如果您不知道IP和端口是什么，请打开证书菜单-> 为Android安装-> 物理设备-> 在第二部分。查找服务器IP和端口。
4.在保存之前，在旁路代理列表中输入 'localhost'✅

![CleanShot 2023-04-05在22 28 12 2 @ 2x](图像/230129476-4bd5d1a0-c3c5-4c73-bb79-81f14a071e63_172a0fa3.jpg)

5.完成
6.“桥被关闭” 警告和地铁捆绑错误消失✅

#### Android物理设备

1.打开Android物理设备-> 设置应用程序-> 网络-> Wifi -> 找到更改代理的方法
2.使用Proxyman IP & 端口手动更改HTTP代理。如果您不知道IP和端口是什么，请打开证书菜单-> 为Android安装-> 物理设备-> 在第二部分。查找服务器IP和端口。
3.在保存之前，在旁路代理列表中输入 “您的ip”✅
4.完成

更多信息请访问: <https://github.com/ProxymanApp/Proxyman/issues/ 1407 # issuecomment-1497235102>
