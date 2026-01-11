# GraphQL

## 1. Use Debugging Tools with GraphQL Requests&#x20;

From Proxyman 2.27.0, we can use debugging tools with GraphQL Requests by specifying the GraphQL Query Name.

Matching by GraphQL QueryName works with Breakpoint, Map Local, Map Remote, Block List, Allow List, and the Scripting Tool.

#### How to use

1. Open the debugging tool (e.g. Breakpoint)
2. Create new Rule
3. Click on Use "Wildcard Dropdown" -> Advanced -> Check GraphQL QueryName.
4. Enter the GraphQL QueryName

By doing this way, the debugging tool will match the original matching rule firstly, then match the GraphQL QueryName.

![Enable GraphQL QueryName](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MacgPHEbYY2MrgWPuxX%2F-MacgUeszvheTmIlUrlG%2FScreen_Shot_2021-05-26_at_15_46_13.png?alt=media\&token=0315198b-0784-4fb5-a749-3116495ed320)

![Specify the GraphQL QueryName](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MacgPHEbYY2MrgWPuxX%2F-MachGDOOk0ERFBap4p-%2FScreen_Shot_2021-05-26_at_15_48_17.png?alt=media\&token=513ed723-3395-40e0-b4b7-5c7109852545)

{% hint style="info" %}
From build 3.0.0, Proxyman automatically fills the GraphQL Query Name when we create a debugging tool rule.
{% endhint %}

## 2. GraphQL Prettier

From Proxyman 2.33.0, Proxyman can prettify/beautify GraphQL's Query Value. To do it, please open Tools Menu -> Custom Previewer Tab -> Check GraphQL checkbox.

![Beautify GraphQL Query](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MjJ69ff1vDV4wU6dKAD%2F-MjJ6Jbk2YKgmnqmYc6u%2FScreen_Shot_2021-09-11_at_15_58_08.png?alt=media\&token=71007b3f-4f6c-44e8-a3b8-1e51393163bf)

## 3. Show GraphQL Query Name on the main table view

It's possible to extract and display the Query Name. Please Right-click on the Column Header and enable it.

![Query Name from GrapQL Request](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LlPt_6BePnJ3oK3saP1%2F-MVepXPi2YNzkeoVqOWB%2F-MVetX1HGlYXY9NQS7A3%2FScreen_Shot_2021-03-13_at_16_20_42.png?alt=media\&token=f7f16b9c-d200-4742-b158-db9f23cdd42b)

{% content-ref url="../basic-features/custom-header-column" %}
[custom-header-column](https://docs.proxyman.com/basic-features/custom-header-column)
{% endcontent-ref %}

## 4. Debug GraphQL Requests (Legacy - Proxyman 2.26.0 and below)

GraphQL uses the same URL to query different responses from the server, current debugging tools (e.g. Map Local, Breakpoint, Map Remote) doesn't work well.

However, by using the Scripting Tool, we can easily achieve:

* Map Local for the response depends on QueryName
* Manipulate the query, body, header for GraphQL Requests and Response

### Map Local with the Scripting Tool

We can use the Scripting tool to map&#x20;

1. Open Proxyman
2. Enable SSL Proxying on the GraphQL domain
3. Verify that you can see HTTPS requests from your domain
4. Right-Click on the flow -> Tool -> Scripting to create a script with the given URL
5. To import a local file: Click the More button -> Import JSON or Other files -> Then selecting your file
6. Use the following script shows you how to set a Local File to a GraphQL request with QueryName="user"

```javascript
// Import file from More Button -> Import JSON or Other files 
const file = require("@users/B02D96D5.default_message_32E64A5B.json");

function onRequest(context, url, request) {

  // 1. Extract the queryName from the request
  var queryName = request.body.query.match(/\S+/gi)[1].split('(').shift();
  
  // Or extract the operationName
  var operationName = request.body.operationName
  
  // 2. Save to sharedState
  sharedState.queryName = queryName
  sharedState.operationName = operationName
  
  // Done
  return request;
}

function onResponse(context, url, request, response) {

  // 3. Check if it's the request we need to map
  if (sharedState.queryName == "user") {
    
    // 4. Import the local file by Action Button -> Import
    // Get the local JSON file and set it as a body (like Map Local)
    response.headers["Content-Type"] = "application/json";
    response.body = file;
  }

  // Done
  return response;
}
```

### Manipulate Headers, Query, Body

1. Use the same code and change the queryName&#x20;
2. Please use [the snipped code](https://docs.proxyman.com/scripting/snippet-code#2-common-on-request-and-response) to change the values
