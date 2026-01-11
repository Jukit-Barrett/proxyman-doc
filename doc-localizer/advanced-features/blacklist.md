# Block List

## 1. What's it?

The Block List Tool is useful when you would like to **block or hide** certain domains during a debugging session.

For instance, you can use Block List in the following situations:

* Block all ads requests from particular domains
* Block all analytic requests that flood the working space
* Block all annoying ping requests from your app to reduce the number of requests that appear on Proxyman
* Hide analytic traffic from your website without blocking it.

All blocked domains in the Block List will **drop the connection.**

<figure><img src="images/Screenshot_2025-09-05_at_21.11.17_79189c03.png" alt=""><figcaption><p>Block certain Requests by Domains or Client</p></figcaption></figure>

## 2. Block Actions

Block List supports some block actions that can suit your needs:

<table><thead><tr><th width="238.87890625">Block Action</th><th>Description</th></tr></thead><tbody><tr><td>Block &#x26; Hide Request</td><td>Matched requests are blocked and don't display on the app.</td></tr><tr><td>Block &#x26; Display</td><td>Matched requests are blocked, but display the blocked requests on the app.</td></tr><tr><td>Hide, but not Block</td><td>Just hiding the matched requests without blocking them. It's useful if you'd hide your annoying requests but don't block them.</td></tr></tbody></table>

![Create a Block / Hide Rule](images/Screen_Shot_2022-01-10_at_14.43.38_c892a445.png)

## 3. How to use it?

* **Tools** Menu -> **Block List**
* Right-click on the requests or domains -> **Tools** -> **Block List...**

{% hint style="success" %}
**⌥⌘\[** to quick open Block List Window
{% endhint %}

## 4. Block all traffic from a given App

* On Proxyman macOS 5.24.0 or later, you can select an app and block all traffic

<figure><img src="images/Screenshot_2025-09-02_at_10.08.23_4c6d177b.jpg" alt=""><figcaption></figcaption></figure>
