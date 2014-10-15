windyLights
=========

Python code to control a set of RGB controllable christmas tree lights with live wind turbine data.

Hook this up on a Raspberry Pi with Red, Green and Blue of your lights hooked up via transistors to different raspberry Pi GPIO pins and they will change duty cycle with live wind turbine data.

Our turbine uses pusher to share its live output data (so you need their library).

Recommended you can auto-start this script by adding to crontab:

crontab -e

and then add in:

@reboot sudo python /path/to/windylights.py