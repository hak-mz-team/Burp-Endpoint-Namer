# Burp Suite Endpoint Namer (Super Fast Shortcut)

An advanced Burp Suite extension written in Python (Jython) combined with a Linux automation script to automatically send HTTP requests to the **Repeater** and name the tabs.

**Check your current environment:**
Open your terminal and run:
`echo $XDG_SESSION_TYPE`
- If the output is `x11`, you are good to go!
- If the output is `wayland`, you need to switch to X11.

**How to switch to X11:**
1. Log out of your current Linux session.
2. At the login screen, select your username.
3. Click the gear icon (⚙️) located at the bottom right.
4. Select **GNOME on Xorg** (or your DE's X11 equivalent).
5. Enter your password and log in.


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
Simply press `Ctrl + Alt + R`, and watch the request instantly fly to the Repeater named properly!
