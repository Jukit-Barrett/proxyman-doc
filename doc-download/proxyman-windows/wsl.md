# WSL

### 1. What's it?

In order to use Automatic Script for Android Emulator, the following command line must be installed on your Windows machine:

* wsl
* choco (package manager for Windows)
* adb (Android Debug Bridge)

### 2. Install WSL on Windows 10/11

1. On Windows 10/11, search: **Command Prompt** app
2. Right-click on the app -> Select **Run as administrator** option.
3. When the App is opened, copy & paste the following command:

```bash
wsl --install
```

4. Restart your Windows to take effect -> After restarting, Windows will open the **Command Prompt** which asks the user to create a new Username / Password -> Follow this instruction
5. Open the Command Prompt app again, execute:

```
wsl
```

6. Verify that the command is successful, with no errors:

<figure><img src="https://1856518738-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LlPt_6BePnJ3oK3saP1%2Fuploads%2F0KiuitXtLhZlLyIGq2SI%2FCleanShot%202024-03-29%20at%209%E2%80%AF.43.29%402x.jpg?alt=media&#x26;token=db043567-0163-4af1-82d7-725f608c7eeb" alt=""><figcaption></figcaption></figure>

7. Done ✅

### 2. Install **Choco** on Windows 10/11

1. Open PowerShell with Run as Administrator
2. Paste and run it:

```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

3. Wait a few seconds for the command to complete.&#x20;
4. If you don't see any errors, you are ready to use Chocolatey! Type choco or choco -? now, or see Getting Started for usage instructions.

Choco Installation Guide: <https://chocolatey.org/install#individual>

### 3. Install **adb** on Windows 10/11

1. Open PowerShell with Run as Administrator
2. Run:

```
choco install adb -y
```

3. Verify the **adb** is successfully installed and there is no error

### 4. ✅ Done. Try to Use Android Automatic Script again on Proxyman app

### 5. References:

* <https://learn.microsoft.com/en-us/windows/wsl/install>
* <https://pureinfotech.com/install-wsl-windows-11/#install_wsl2_single_command>
