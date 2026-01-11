# Filter JSON Response

You can quickly filter the JSON Response with the following approach:

### 1. Filter on JSON Previewer

* **⌘F** to trigger the Filter
* Support Regex
* Support Jump Next

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MIxxav7aI2mJ6cNqZrq%2F-MIxxuqk-fVjjHSX9dcr%2FScreen_Shot_2020-10-06_at_19_47_47.png?alt=media\&token=ad576252-9751-43cd-87a9-d3ae06fb71f2)

### 2. JSONPath

Proxyman supports [JSONPath](https://github.com/json-path/JsonPath#path-examples) for quickly querying the data in JSON Document.

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MfzvKgHrrVOB_SexW44%2F-MfzvapgK9JWsYTJn6dt%2FScreen_Shot_2021-08-01_at_10_29_23.png?alt=media\&token=8aedc2a1-3dad-478d-8c5e-442e2caf0a2c)

Please check out JSONPath documentation.

{% content-ref url="jsonpaths" %}
[jsonpaths](https://docs.proxyman.com/basic-features/jsonpaths)
{% endcontent-ref %}

### &#x20;3. KeyPaths

* Support Key Paths filter on JSON Tree View mode
* Search specifically the children keys&#x20;

Syntax example:

* **posts\[1].maker\[2]**: Go from Root -> Get item at index 1 of the Posts array -> Get the index 3 items of Makers array and filter out
* **users.name**: Get the name value of the "users" dictionary&#x20;

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MIxxav7aI2mJ6cNqZrq%2F-MIxy5sNhUXUbfvyiijX%2FScreen_Shot_2020-10-06_at_19_30_35.png?alt=media\&token=e80edbe7-da3d-497b-acfa-130944b57daf)

### 4. All Keys or All Values

* Show all nodes that the key or value contains the search text

![](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MIxyS6P3poAOWR9J7RQ%2F-MIxzB4KkDq13VJqL13z%2FScreen%20Shot%202020-10-06%20at%2014.21.26.png?alt=media\&token=7a3bef8a-0f16-4d52-ba84-8bc1632edbe0)
