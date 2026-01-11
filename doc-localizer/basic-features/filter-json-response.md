# Filter JSON Response

You can quickly filter the JSON Response with the following approach:

### 1. Filter on JSON Previewer

* **⌘F** to trigger the Filter
* Support Regex
* Support Jump Next

![](images/Screen_Shot_2020-10-06_at_19_47_47_cc364e30.png)

### 2. JSONPath

Proxyman supports [JSONPath](https://github.com/json-path/JsonPath#path-examples) for quickly querying the data in JSON Document.

![](images/Screen_Shot_2021-08-01_at_10_29_23_fcc64f7d.png)

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

![](images/Screen_Shot_2020-10-06_at_19_30_35_d8d347ad.png)

### 4. All Keys or All Values

* Show all nodes that the key or value contains the search text

![](images/Screen_Shot_2020-10-06_at_14.21.26_7c9adab7.png)
