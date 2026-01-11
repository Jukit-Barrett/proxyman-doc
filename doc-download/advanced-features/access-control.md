# Access Control

## 1. What's it?

It's an advanced feature, which allows you to define how Remote Devices (iPhone, Android, other computers) can connect to the Proxyman app. It's designed for enterprise users for better security.

Access via **Tools Menu** -> Proxy Setting -> Access Control.

<table><thead><tr><th width="169">Mode</th><th>Description</th></tr></thead><tbody><tr><td>Allow All</td><td>All Remote Connections can connect to Proxyman (Default).</td></tr><tr><td>Disallow All</td><td>All Remote Connections are not allow to connect to Proxyman.</td></tr><tr><td>Specify Remote Device by IP</td><td>Define which device can connect to the Proxyman app.</td></tr></tbody></table>

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FzJwU5MqOdh4icM3PxOlZ%2FScreenshot%202023-01-23%20at%2009.25.40.png?alt=media&#x26;token=6718f108-5c53-4922-aec4-0446bfcc624a" alt=""><figcaption><p>Access Control UI</p></figcaption></figure>

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FTv31V8COAJB6hiKoBVZs%2FScreenshot%202023-01-19%20at%2014.31.47.png?alt=media&#x26;token=82cfae97-6b48-4e72-ba18-855dfccf58b5" alt=""><figcaption><p>Prompt to allow unauthorized connections</p></figcaption></figure>

## 2. Override the Access Control mode by Command Lines

From Proxyman 4.4.0, it's possible to override the Access Control by the following CLI.

It's useful if your company would enforce the mode without using GUI.

```
$ defaults write ~/Library/Preferences/com.proxyman.NSProxy.plist accessControlModeString "allowAll"
$ defaults write ~/Library/Preferences/com.proxyman.NSProxy.plist accessControlModeString "disallowAll"
$ defaults write ~/Library/Preferences/com.proxyman.NSProxy.plist accessControlModeString "specificIP"
```
