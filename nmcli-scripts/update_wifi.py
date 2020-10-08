import subprocess
import sys
import os
import time

ssid = sys.argv[1]
pswd = sys.argv[2]

print (ssid + pswd)
subprocess.call(["nmcli", "con", "down", "Hotspot"])
subprocess.call(["sudo", "iw", "wlan0", "scan"])
subprocess.call(["nmcli", "dev", "wifi", "connect", ssid, "password", pswd])