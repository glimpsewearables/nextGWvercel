import os
import subprocess

os.chdir("/usr/src/app/")

subprocess.call(["./nmcli", "dev", "wifi", "rescan"])
ssid_list = subprocess.check_output(["./nmcli", "-t", "-f", "SSID", "dev", "wifi"])

print ssid_list
