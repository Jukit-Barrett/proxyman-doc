# SSL Proxying

## 1. SSL Proxying List

A list of domains or applications that Proxyman should decrypt its SSL Connection. It enables the user to inspect the HTTPS Request/Response in plain text.

### Include List and Exclude List

You can define rules for:

* **Include List**: Intercept the traffic from apps/domains if it's in the include list
* **Exclude List**: Ignore all traffic from apps/domains in Exclude List

![SSL Proxying List](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MNNV0ioroSdDj1rtNl1%2F-MNNVBHLJJ_R4d-5rijF%2Fssl_proxying.png?alt=media\&token=a5232408-193a-44a1-9f76-0852b530c5f4)

{% hint style="info" %}
⌘⌥P to quickly open the SSL Proxying List.
{% endhint %}

### Apps / Domains / Wildcards

Proxyman supports several formats to define a rule:

* **By app**: Intercept all traffic that goes from this app
* **By Domain**: Intercept all traffic from this domain
* **Wildcard**: If it's matched the wildcard regex

For examplee:

| Wildcard                    | Description                                                |
| --------------------------- | ---------------------------------------------------------- |
| \*                          | Decrypt ALL HTTPS traffic                                  |
| \*.domain.com, \*.apple.com | e.g. v1.domain.com, data.domain.com, health.apple.com, ... |
| v?.domain.com               | e.g. v1.domain.com, v2.domain.com, ...                     |

{% hint style="info" %}
It's essential to set up the Proxyman Certificate before intercepting any HTTPS requests. You can follow the [macOS setup Guide](https://docs.proxyman.com/debug-devices/macos) to properly install and trust the certificate..
{% endhint %}

### How to enable SSL Proxying on a particular domain or app

* Right-Click on the app or domain on the Left Panel -> Enable SSL Proxying

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FbfeUhwBLzp7GI7vdSGCp%2Fdomain.jpeg?alt=media&#x26;token=5cff404f-1782-429a-9c37-2d24bb7af4c1" alt=""><figcaption><p>Add a domain to the SSL Proxying List</p></figcaption></figure>

* Right-Click on the Request on the main table -> Enable SSL Proxying
* Select the request and enable SSL Proxying on the Response Panel.

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FWOUdc3l4zWEphd5ANRD0%2F2.jpeg?alt=media&#x26;token=a8ab2e51-d1a2-468a-8222-fe764d43a5e6" alt=""><figcaption><p>Enable entire app or a single domain</p></figcaption></figure>
