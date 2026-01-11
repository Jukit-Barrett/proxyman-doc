# Firefox

## ✅ New Solution (Proxyman v5.19.0 or later - recommended)

With Proxyman v5.19.0+, Proxyman can capture HTTPS Requests/Responses from Firefox with 1-click setup.

1. Go to Setup Menu -> Automatic Setup
2. On the Web Browser Section -> Click the ⬇️ Arrow Button -> Select Firefox

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2Fs9CEz0ITuJFFEjMWYjLG%2FScreenshot%202025-04-28%20at%2009.53.27.jpg?alt=media&#x26;token=87bc7291-2ecf-418f-9bc5-f58bcbf0c02f" alt=""><figcaption><p>How to capture HTTPS Reqyests/Responses from Firefox Browser with Proxyman</p></figcaption></figure>

3. New Firefox instance will open
4. ✅ Done. All traffic from Firefox will be captured by Proxyman

This setup will make Firefox or Google Chrome:

* Auto set Proxyman to Proxyman
* Auto install & trust Proxyman Certificate

{% hint style="success" %}
Works with Google Chrome and Firefox
{% endhint %}

## ❌ Old Solution (Proxyman v5.18.0 or ealier)

In order to intercept HTTPS traffic from Firefox, it requires extra steps to install Proxyman CA into Firefox's Trust Store.

### 1. Install Proxyman CA on macOS machine

Before installing Proxyman CA on Java VMs, we have to install it properly on your current machine.

Check out macOS Guidelines:

{% content-ref url="macos" %}
[macos](https://docs.proxyman.com/debug-devices/macos)
{% endcontent-ref %}

If you've done this step, you can skip to the next step.

### 2. Set Proxy on Firefox

* Open Firefox's Preferences panel (CMD+,)
* Search Proxy and open the Proxy Settings
* Select Auto Use System Proxy or manually hardcode the Proxy IP and Port

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MH_Go0N5xZXL5IXWXr0%2F-MH_Hi8ciXNj2TC6323L%2FScreen_Shot_2020-09-19_at_14_33_17.png?alt=media\&token=893e85c2-2e4a-451b-b4b0-eccfa1446280)

### 3. Install Proxyman CA to Firefox

1. Open `http://proxy.man/ssl` on Firefox and download the certificate to your Download folder

{% hint style="info" %}
<http://proxy.man/ssl> is a local HTTP Server for strengthening the security. Please make sure the Proxyman app is open when accessing this domain.
{% endhint %}

2\. Open Firefox's Preferences (CMD+,) and openthe  View Certificate window

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MAUFPily_DmIzAplEmx%2F-MAUH9ID3Ks0R5MuU0L6%2FScreen_Shot_2020-06-23_at_10_27_27.png?alt=media\&token=c82c8345-0dae-4fed-bcac-2b9da5ec2f50)

3\. Open the Authorities Tab and select the Import button

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MAUFPily_DmIzAplEmx%2F-MAUHITJp-gj9-hSheNW%2FScreen_Shot_2020-06-23_at_10_27_35.png?alt=media\&token=efc6c514-3041-4499-a3a5-8a071b1fc261)

4\. Select Proxyman CA, which you've downloaded and Trust all.

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MAUFPily_DmIzAplEmx%2F-MAUHTWo97fQnsijXTbu%2FScreen_Shot_2020-06-23_at_10_37_52.png?alt=media\&token=a88b32e7-e8bf-40b9-a571-7aee82663b28)

5\. Reload the page that you need to intercept. Enjoy!
