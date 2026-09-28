# Burp-Endpoint-Namer

A simple Burp Suite extension that sends the current HTTP request to Repeater and automatically names the Repeater tab using the endpoint name.

## Features

* Press `Ctrl+R` inside a Burp HTTP message editor.
* Sends the current request directly to Repeater.
* Automatically names the Repeater tab using the endpoint name.
* Ignores query parameters.
* Removes trailing slashes from endpoint names.

### Example

```text
/api/users/123/reset-password?token=abc
```

The Repeater tab will be named:

```text
reset-password
```

## Installation

### Option 1 — Download the ready-made JAR

Download the latest release:

**[Download Burp-Endpoint-Namer](https://github.com/hak-mz-team/Burp-Endpoint-Namer/releases/latest)**

Then in Burp Suite:

**Extensions → Installed → Add → Java**

Select:

```text
burp-endpoint-namer-1.0.0.jar
```

### Option 2 — Build from source

Requirements:

* Java 17+
* Maven

Clone the repository and build:

```bash
git clone https://github.com/hak-mz-team/Burp-Endpoint-Namer.git
cd Burp-Endpoint-Namer
mvn clean package
```

The JAR will be created at:

```text
target/burp-endpoint-namer-1.0.0.jar
```

## Important: Ctrl+R Shortcut Conflict

Before using the extension, make sure Burp Suite does not already have another action assigned to `Ctrl+R`.

If `Ctrl+R` is already assigned:

1. Open Burp Suite settings.
2. Go to the keyboard shortcuts / hotkeys settings.
3. Find the existing `Ctrl+R` shortcut.
4. Remove it or assign it to another key.
5. Keep `Ctrl+R` available for Burp-Endpoint-Namer.

The extension registers `Ctrl+R` for HTTP message editors.

## Requirements

* Burp Suite with Montoya API support.
* Java 17+ compatible runtime.

## Project Structure

```text
Burp-Endpoint-Namer/
├── src/
│   └── main/
│       └── java/
│           └── Extension.java
├── .gitignore
├── pom.xml
└── README.md
```

Build artifacts such as `target/` are intentionally excluded from the repository.


