# 铁锈

# #1.问题

Proxyman无法自动捕获从Rust中的 “reqwet” 调用的HTTP/HTTPS流量，因为:

* 'reqwest' 不尊重系统HTTP代理-> 没有流量通过Proxyman
* 'reqwest' 不信任任何自签名的Proxyman证书-> 获取SSL错误

# #2.解决方案

* 在 “http:// localhost:9090” 手动将代理设置为Proxyman
* 禁用SSL验证

''' 铁锈
使用anyhow::Result；
使用reqwest::Url；

#[tokio::main]
异步fn main() -> Result<()> {
让proxy_url = Url::parse("http:// localhost:9090" )？；
让client = reqwest::Client::builder()
。danger_accept_invalid_certs(true) // 信任自签名证书
.proxy(reqwest::Proxy::https(proxy_url)？) // 代理到Proxyman
.build()?;
让响应 = client.get (“ https://httpbin.org/get ”).send().await？；

如果response.status().is_success() {
让body = response.text()。等待？；
println!("响应文本: {}"，正文)；
} else {
println!("请求失败，状态: {}"，response.status ())；
}

好 (())
}
'''
