# Docker

### 1.从Docker容器捕获流量

默认情况下，如果您从Mac设备访问Docker容器，Proxyman可以捕获您从该容器访问的所有流量。

为了详细说明，这里是示例Docker容器:

1.通过NodeJS Express设置一个简单的HTTP服务器然后dockering它。您可以在 < https://nodejs.org/en/docs/guides/ nodejs-docker-webapp/> 中找到它
2.确保我们通过端口8080暴露您的服务器。
3.您可以通过在Safari上打开 <http:// localhost:8080> 进行验证。

### 2.捕获Docker容器内的流量

阅读更多 < https://github.com/ProxymanApp/Proxyman/issues/ 419 # issuecomment-1059096490>

### 3.替代解决方案:

1.添加docker-compose.proxyman.yml。用您的服务替换 \<php8.1-fpm-xdebug>

'''yaml
版本: '2'
服务:
php8.1-fpm-xdebug:
环境:
HTTP_PROXY: host.docker.internal:9090
HTTPS_PROXY: host.docker.internal:9090
http_proxy: host.docker.internal:9090
https_proxy: host.docker.internal:9090
'''

2.启动Docker:

'docker-compose -f docker-compose.yml -f docker-compose.proxyman.yml up -d'

参考: <https://github.com/ProxymanApp/Proxyman/issues/ 1712 # issuecomment-1642279537>
