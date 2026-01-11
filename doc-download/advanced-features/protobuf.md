# Protobuf

### 1. Protocol Buffer

From [Protobuf's Google](https://developers.google.com/protocol-buffers/), Protocol buffers are Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data – think XML, but smaller, faster, and simpler.

You define how you want your data to be structured once, then you can use special generated source code to easily write and read your structured data to and from a variety of data streams and using a variety of languages.

Proxyman is capable of **reading** a Protobuf Binary and parsing to **JSON Format** with given Protobuf File Descriptors.

![Parse protobuf request with File Descriptor](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-M5lixcwWeMPWwvY2whW%2F-M5lkc_hSq_6DhDF6Az5%2FScreen_Shot_2020-04-25_at_21_32_54.png?alt=media\&token=70cdd7c2-5c07-49e7-99fc-84fb0d94bfa8)

### 2. Protobuf File Descriptor (\*.desc)

Proxyman requires File Descriptor (\*.desc) to properly parse the Protobuf Data.

There are various ways to get the File Descriptor:

#### 1. Ask your colleagues.

If your company is using Protobuf, it's a high chance that your colleagues have already had this file, especially the Backend and Frontend teams.

It might be one or multiple descriptor files.

#### 2. Generate from \*.proto file

If you have a bunch of \*.proto files, you can simply generate 1 single \*.desc file by using the following command line.

```bash
# Install protobuf cli if need
brew install protobuf

# Create `input` folder on the Desktop
# Copy all proto files to the `input` folder

# Generate 1 descriptor file with multiple proto files
protoc --descriptor_set_out=output.desc --include_imports -I=/Users/<your_name>/Desktop/input /Users/<your_name>/Desktop/input/*.proto

# Done
# output.desc
```

Once you have the Descriptor File, you can import them to Proxyman:

* Proxyman -> Tools Menu -> Protobuf Schema
* Click on the + button and select the **output.desc** file

{% hint style="info" %}
Proxyman 3.6.0+ only accepts **File Descriptor (\*.desc)** for better Protobuf parsing.

If you have **\*.proto** files, you can convert them to **\*.desc**. Please check out the next section.
{% endhint %}

{% hint style="info" %}
Proxyman automatically imports all common types from **Google Protobuf**, such as Timestamp, Struct, Value, Enum, Method, etc.

Proxyman supports both **proto2** and **proto3** syntax. [Read more](https://developers.google.com/protocol-buffers/docs/proto3)
{% endhint %}

### 3. Protobuf Config

Before using Protobuf, you have to config which Message Type should be used to parse the Protobuf data.

The following table describes which config are:

| Name                                | Description                                                                                                                                                         |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Schema                              | Add `.desc` file if need                                                                                                                                            |
| Message Type                        | The Class name of the root object in Protobuf binary. **Must include Package name**                                                                                 |
| Payload Type: **Auto**              | Auto detect if the Protobuf Binary is encoding as a Single Message or [Delimited Message](https://developers.google.com/protocol-buffers/docs/techniques#streaming) |
| Payload Type: **Single Message**    | Single Mesage in a Protobuf Binary                                                                                                                                  |
| Payload Type: **Delimited Message** | Multiple Messages in a Protobuf Binary (Length-Prefix)                                                                                                              |

![Add Message Type to particular requests](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-M5lixcwWeMPWwvY2whW%2F-M5lmAlPcvbTehjdCiFz%2FScreen%20Shot%202020-04-25%20at%2021.40.16.png?alt=media\&token=8ee4e3fe-b1e9-40c4-8a16-f9b036c7b2ba)

### 4. How to use?

There are **two** ways to parse Protobuf properly with qualified name fields:

* Define Protobuf Rules
* Read from Content-Type Header

#### 4.1 Define Protobuf Rule

1. Make a request, which has `Content-Type: application/x-protobuf` or `Content-Type: application/protobuf`
2. You can see the Warning that Proxyman couldn't parse properly due to the absence of Message Type. Click Add to open Protobuf Settings

![Missing Message Type](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-M5lnvriZFMegQHaQMbz%2F-M5lq38TdKPlCYQk1JvO%2FScreen_Shot_2020-04-25_at_21_56_19.png?alt=media\&token=fe738ee8-808e-4032-ac8c-23fec9123fe2)

3\. Add Schema and fill Message type and Payload Type:

* Right Click on the Protobuf Request -> Tools -> Protobuf
* Select which Message Type for this request (Add Desc file if need)

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-M5lixcwWeMPWwvY2whW%2F-M5lmAlPcvbTehjdCiFz%2FScreen%20Shot%202020-04-25%20at%2021.40.16.png?alt=media\&token=8ee4e3fe-b1e9-40c4-8a16-f9b036c7b2ba)

4\. Click Add and see qualified JSON Format

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-M5lnvriZFMegQHaQMbz%2F-M5lsSsNQf3WDg0JIvmX%2FScreen%20Shot%202020-04-25%20at%2022.08.07.png?alt=media\&token=e7b4f811-5fb5-4e03-beda-5ddd696abab2)

#### 4.2 Read from Content-Type Header

You can **dynamically** provide the Protobuf Config from `Content-Type`

For example: Your `Content-Type` in the Request or Response might look like:

`Content-Type: application/x-protobuf; messageType="tutorial.Address"; delimited=true`

`Content-Type: application/x-protobuf; messageType="com.proxyman.User"; delimited=false`

To specify that the Protobuf Body this MessageType and the payload encoding.

### 5. Troubleshooting

#### 5.1 Some name fields are missing

There is a situation where some field names are absent because the field name definition is not included in your Protobuf File Descriptor. It might be your descriptor is out of date.

**Solution**:

* Remove old Protobuf Schema and Add the latest descriptor file from your server.
* If you're using Proxyman 3.5.2 and older, please update to Proxyman 3.6.0 or later. Then, use File Descriptor (\*.desc) for better results.
