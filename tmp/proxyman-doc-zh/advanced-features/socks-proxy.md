# SOCKS代理

# #1.什么事？

从Proxyman 4.9.0开始，Proxyman在正常的HTTP/HTTPS代理旁边支持SOCKS代理。

* 支持HTTPS通过袜子代理: 所有调试工具 (例如地图本地，断点，...) 仍然工作正常。
* 与袜子5兼容

{% 提示样式 = "info" %}
Proxyman应用程序不会在启动时自动覆盖System SOCKS代理设置。如果需要，您必须手动启用它。
{% endhint %}

{% 提示样式 = "警告" %}
Proxyman仅支持 “连接” 和 “udp” 命令。尚不支持 'bind' ''命令。
{% endhint %}

# #2.如何使用它？

1.在工具菜单-> 代理设置-> SOCKS代理设置中打开SOCKS代理设置
2.默认情况下，Proxyman侦听端口8889
3.在您的客户端上: 在端口8889将SOCKS代理设置为127.0.0.1

<figure><img src = "images/252151302-d68e2a24-1310-4764-b8b5-ecc37ef42fab_5f3cd0da.png" alt = ""><figcaption><p>SOCKS代理 </p></figcaption></figure>
