#!/bin/bash
OLD_LAYOUT=$(setxkbmap -query | awk '/layout/{print $2}')
setxkbmap us
xdotool keyup Control_L Control_R Alt_L Alt_R r
xdotool click 3
sleep 0.03
xdotool key Escape
touch /tmp/burp_trigger_repeater
setxkbmap $OLD_LAYOUT
