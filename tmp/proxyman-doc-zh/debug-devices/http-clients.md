# HTTP客户端

### 1.问题

Proxyman可能无法从HTTP/HTTPS请求中捕获或获取SSL错误，这些请求来自某些HTTP客户端，例如 [Postman](https://www.postman.com/)，[失眠休息](https:// Insomnia.Rest/) 和 [Paw](https:// paw.cloud/) 应用程序。

本文档将提供一个解决方案，使Proxyman的作品。

### 2.邮差

1.打开邮递员首选项
2.在常规选项卡-> 取消选中 “SSL证书验证” 复选框
3.在代理选项卡-> 检查 “使用系统代理” 和 “尊重 'HTTP_PROXY' * 和 'HTTPS_PROXY' * 变量”。

![配置以使Postman与Proxyman一起工作](images/Postman_And_Proxyman_8725f2c2.jpg)

### 3.失眠休息

1.打开失眠偏好-> 常规选项卡
2.取消选中 “验证证书” 复选框
3.检查 “启用代理”，然后在HTTP代理和HTTPS代理文本框中输入 'localhost:9090 '。

![配置使失眠休息与Proxyman合作](images/Insomnia_And_Proxyman_e11b9d08.jpg)

### 4.爪子

默认情况下，Paw app使用系统代理配置。因此，Proxyman可以开箱即用。

如果您没有看到来自Proxyman的任何Paw流量，请仔细检查:

1.打开爪子偏好。
2.确保在代理设置中使用系统代理配置。

![Paw和Proxyman](images/Paw_Proxyman_67a833f4.jpg)
