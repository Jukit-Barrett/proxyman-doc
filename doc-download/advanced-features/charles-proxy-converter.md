# Charles Proxy Converter

## 1. What's it?

Proxyman is capable of converting and reading the `chls` files from Charles Proxy app to `har` format that Proxyman can understand.

{% hint style="success" %}
It requires that Charles Proxy beis already installed in order to convert `chls` files&#x20;
{% endhint %}

You can manually convert the files from the File menu -> Convert -> `chls` to `har`

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-M6PIQiDj7p2umCK6D5Y%2F-M6PIce9rkDFwLNTFfBY%2FScreen%20Shot%202020-05-03%20at%2018.31.39.png?alt=media\&token=bdb9ae4f-9a63-4eb0-a199-cd50b532cced)

## 2. How does it work?

In general, Proxyman uses [Convert CLI from Charles Proxy](https://www.charlesproxy.com/documentation/tools/command-line-tools/) to convert .chls to .har, which Proxyman can understand.

1. As soon as you open `chls` file, Proxyman tries to find the Charles Proxy app, which has a bundle ID is&#x20;

   `com.xk72.Charles`
2. Convert by using the convert command

```
$ ./Applications/Charles.app/Contents/MacOS/Charles convert ~/Desktop/input.chls ~/Desktop/output.har

```

3\. The output is `har` formatted in your Desktop directory

## 3. How to use?

There are several ways to open `chls` files:

* Open the `chls` file directly (Double-Click on the file, or Open With from Finder app)
* Drag and drop the file to the Proxyman app
* File -> Open and select `chls` files
