# SOCKS Proxy

## 1. What's it?

From Proxyman 4.9.0, Proxyman supports SOCKS Proxy beside the normal HTTP/HTTPS Proxy.

* Support HTTPS over SOCKS Proxy: All debugging tools (e.g. Map Local, Breakpoint, ...) still work fine.
* Compatible with SOCKS 5

{% hint style="info" %}
Proxyman app doesn't automatically override the System SOCKS Proxy Setting at launch time. You have to manually enable it if needed.
{% endhint %}

{% hint style="warning" %}
Proxyman only supports \`connect `` and `udp` command. The`bind` ``command is not supported yet.
{% endhint %}

## 2. How to use it?

1. Open the SOCKS Proxy Setting in Tools Menu -> Proxy Setting -> SOCKS Proxy Setting
2. By default, Proxyman listens on port 8889&#x20;
3. On your client: Set the SOCKS proxy to 127.0.0.1 at port 8889

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FrEFmycrGx972YBsFJUfT%2F252151302-d68e2a24-1310-4764-b8b5-ecc37ef42fab.png?alt=media&#x26;token=6cb2aa47-d0dd-438e-b10b-1d8179760d87" alt=""><figcaption><p>SOCKS Proxy</p></figcaption></figure>
