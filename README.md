# Burp Suite Endpoint Namer (Super Fast Shortcut)

An advanced Burp Suite extension written in Python (Jython) combined with a Linux automation script to automatically send HTTP requests to the **Repeater** and name the tabs based on the last 15 characters of the **Endpoint** instead of annoying numbers.

## Features
- **Ultra Fast:** Bypasses Burp Suite API limitations using a background file-trigger system.
- **Language-Proof:** Works perfectly even if your Linux keyboard layout is switched to non-English languages (like Arabic).
- **Dynamic Context Aware:** Works from Proxy History, Repeater, and Target tabs without messing up dynamic context menus.

## Installation & Setup

### 1. The Burp Extension (`RepeaterEndpointNamer.py`)
1. Open Burp Suite -> `Extensions` -> `Options` -> `Python Environment` and ensure **Jython standalone JAR** is configured.
2. Go to `Extensions` -> `Installed` -> Click **Add**.
3. Select extension type as **Python** and choose `RepeaterEndpointNamer.py`.

### 2. The Linux Automation Script (`burp_trigger.sh`)
1. Install `xdotool` on your system: `sudo apt install xdotool -y`
2. Move `burp_trigger.sh` to a permanent location (e.g., `/home/user/Burp-Endpoint-Namer/burp_trigger.sh`) and make it executable: `chmod +x burp_trigger.sh`.

### 3. Creating the Global Keyboard Shortcut
1. Go to your Linux OS Settings -> `Keyboard Shortcuts` -> `Custom Shortcuts`.
2. Add a new shortcut with the command: `/home/user/Burp-Endpoint-Namer/burp_trigger.sh`
3. Map it to: `Ctrl + Alt + R` (or any shortcut you prefer).

## Usage
Simply hover your mouse cursor over any HTTP request inside Burp Suite, press `Ctrl + Alt + R`, and watch the request instantly fly to the Repeater named properly!
