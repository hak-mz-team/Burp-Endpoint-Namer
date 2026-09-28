# Burp Endpoint Namer

A lightweight Burp Suite extension written in Java using the official PortSwigger Montoya API.

Burp Endpoint Namer adds a Ctrl+R shortcut that sends the current HTTP request directly to Repeater and automatically names the Repeater tab using the request endpoint.

## Features

- Send the current request to Repeater with Ctrl+R
- Automatically name the Repeater tab
- Ignore query parameters when generating the name
- Remove trailing slashes from the path
- Use the last path component as the Repeater tab name

## Examples

    /punctual/v1/refreshCreds?foo=123
    -> refreshCreds

    /api/users/123/reset-password?token=abc
    -> reset-password

    /api/users/123/profile/
    -> profile

## Requirements

- Burp Suite with Montoya API support
- Java 17 or newer
- Maven 3.x

## Build

Clone the repository:

    git clone https://github.com/hak-mz-team/Burp-Endpoint-Namer.git
    cd Burp-Endpoint-Namer

Build the extension:

    mvn clean package

The compiled JAR will be created at:

    target/burp-endpoint-namer-1.0.0.jar

The extension has been built and tested successfully.

## Install

1. Open Burp Suite.
2. Go to Extensions.
3. Click Add.
4. Select Java as the extension type.
5. Select:

       target/burp-endpoint-namer-1.0.0.jar

6. Load the extension.

After loading, the extension registers:

    Send request to Repeater -> Ctrl+R

## Usage

Open an HTTP message editor in Burp Suite and press:

    Ctrl+R

The request will be sent to Repeater and the tab will automatically be named after the endpoint.

For example:

    GET /api/account/reset-password?token=123 HTTP/1.1

creates a Repeater tab named:

    reset-password

## Ctrl+R Conflict

If Burp Suite already has another action assigned to Ctrl+R, remove or change that shortcut in Burp Suite's keyboard shortcut settings before using this extension.

## Project Structure

    Burp-Endpoint-Namer/
    ├── pom.xml
    ├── README.md
    └── src/
        └── main/
            └── java/
                └── Extension.java

## License

See the repository for licensing information.
