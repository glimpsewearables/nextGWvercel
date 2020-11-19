import subprocess
import sys
import os
import time

ssid = sys.argv[1]
pswd = sys.argv[2]
HOTSPOT_NAME = "balena-hotspot"
print (ssid + pswd)
os.chdir('/usr/src/app')
subprocess.call(["./nmcli", "con", "down", HOTSPOT_NAME])
subprocess.call(["iw", "wlan0", "scan"])
subprocess.call(["./nmcli", "dev", "wifi", "connect", ssid, "password", pswd])