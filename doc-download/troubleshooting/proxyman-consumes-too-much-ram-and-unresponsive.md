# Proxyman consumes too much RAM & unresponsive

## Problems

If Proxyman is:

* Unresponsive after using it for a while.
* Consume too much Memory.

You might encounter the above problems if you enable SSL Proxying with the following rules:

* Use the all \`\*\` wildcard to intercept all traffic from your Mac Machine.
* Enable the entire web browser (Google Chrome, Safari, Firefox, etc.).

## **Reason**

Proxyman will intercept and decrypt all traffic which leads to high memory usage. In the worst scenario, the app can become unresponsive.

![SSL Proxying List with web browser or \* wildcard can slow your Mac.](https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2FQG6Gb8p4TKIBY3Q30b3l%2FScreen_Shot_2022-08-10_at_14_01_16.png?alt=media\&token=e0903e7a-5bfe-419d-a9cf-cc58b893670c)

## Solution

1. ✅ Update to the latest Proxyman version (Memory Leaks has been fixed in the latest builds)
2. Open Tools -> SSL Proxying List&#x20;
3. Remove all Web Browser or \`\*\` wildcards if they exist.
4. Enable SSL Proxying on particular domains.
