# Golang

## 1. New Automatic Solution (macOS v5.17.0 or later) ✅

Proxyman macOS v5.17.0 or later can capture HTTP/HTTPS traffic from Golang with 1-click.

* 1-click solution: No need to manually set HTTP Proxy config or trust the self-signed certificate.
* ✅ Support many Go Network Libraries: net/http, fasthttp, resty, gorequest, req, grequests

### How to use:

1. Open Proxyman -> Setup Menu -> Automatic Setup
2. Select your favorite Terminal ->  Click on the "Open New Terminal" button
3. Accept the Apple Script permission prompt if needed

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2F4CIEVKhzglYi5T3YHVLT%2FScreenshot%202025-03-18%20at%2010.54.37.jpg?alt=media&#x26;token=295c1e9f-10ce-4766-ab65-e08d24f79858" alt=""><figcaption><p>Open Pre-configured Terminal to intercept GO network https</p></figcaption></figure>

4. The New Terminal app is launched -> You can start your Golang Backend Server, or Run scripts => Proxyman automatically captures all traffic.
5. For example:&#x20;

```
$ go run main.go
```

6. Proxyman captures all internal HTTP/HTTPS from go, including net/http

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FtsBq8JdHXuQU1vL31PYZ%2FCleanShot%202025-03-18%20at%2009.56.44%402x.jpg?alt=media&#x26;token=df25804a-c39b-4c87-9422-b52ab338b7a3" alt=""><figcaption><p>capture and intercept HTTPS traffic from net/http go</p></figcaption></figure>

* Go Example Code: <https://github.com/ProxymanApp/golang-example>

## 2. Old Solution (Not recommended ❌)

* Proxyman can't capture any HTTP/HTTPS traffic from the Golang Server.
* The reason is that some network libraries (such as net/http) won't respect the System HTTP Proxy, so no traffic goes through the Proxyman app.

### 2.1 Solution

#### net/http

1. Config Proxy to Proxyman, by default, it's at IP = localhost, port 9090
2. Tell the Transport to trust Proxyman self-signed certificate. Otherwise, you will get an SSL Error because net/http rejects.

```go
package main

import (
	"crypto/tls"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"net/url"
)

func main() {
	// Create a new HTTP client
	client := &http.Client{}

	// Configure the proxy
	proxyURL, err := url.Parse("http://localhost:9090")
	if err != nil {
		log.Fatal("Error parsing proxy URL:", err)
	}

	// Configure transport with proxy and TLS settings
	transport := &http.Transport{
		Proxy: http.ProxyURL(proxyURL),
		TLSClientConfig: &tls.Config{
			InsecureSkipVerify: true, // This allows self-signed certificates
		},
	}

	// Set the transport for the client
	client.Transport = transport

	// Make a request
	resp, err := client.Get("https://example.com")
	if err != nil {
		log.Fatal("Error making request:", err)
	}
	defer resp.Body.Close()

	// Read the response body
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal("Error reading response:", err)
	}

	// Print the response
	fmt.Printf("Status: %s\n", resp.Status)
	fmt.Printf("Body: %s\n", string(body))
}

```
