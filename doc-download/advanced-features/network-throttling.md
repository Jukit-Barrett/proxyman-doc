# Network Conditions

### 1. What's it?

Network Conditions (Network Throttling) v1 allows developers to simulate adverse networking environments. Proxyman provides various preset profiles:

| Profile              | Description                              |
| -------------------- | ---------------------------------------- |
| 100% Lost connection | 100 % lost all connection                |
| Very Bad Network     | Download/Upload: < 1mbps                 |
| Slow Network         | Download/Upload: 5-10 mbps               |
| Medium Network       | Download/Upload: 10-20 mbps              |
| 2G (EDGE)            | Download: <240kbps, Upload <200kbps      |
| 3G                   | Download: <780kbps, Upload <300kbps      |
| 4G (LTE)             | Download: 30-50mbps, Upload 5-10mbps     |
| Wi-Fi                | Download: 25-40mbps, Upload 15-30mbps    |
| Wi-Fi 802.11ac       | Download: 150-250mbps, Upload 70-100mbps |

### 2. Benefit?

* Various preset profiles: 3G, 4G, Wifi, Bad/Medium Network, etc.
* Help developers to simulate various network conditions (Download/Upload Bandwidth, Packets Dropped rate, delay).
* Easier to test your app under a particular network condition.
* Apply for **system-Wide** or **certain domains**.

{% hint style="info" %}
Network Conditions v1 does not allow you to customize a profile. We will implement it in v2.
{% endhint %}

{% hint style="info" %}
To better simulate the real-life, the download/upload bandwidth is not fixed, it might randomize in a given range.&#x20;
{% endhint %}

### 3. How to use it?

You can access the feature by navigating to Tool -> Network Condition (CMD+SHIFT+J) or access from the right-menu context.

![Set Network Condition for particular domain](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MVit2xH7yEC5FgKyj2f%2F-MVit7lBYfPWRzmass9F%2FScreen%20Shot%202021-03-14%20at%2009.59.23.png?alt=media\&token=389ae2fd-021d-4250-9a9b-49ac30e57392)

### 4. Alternative

* Network Link Conditions for macOS: <https://nshipster.com/network-link-conditioner/>
