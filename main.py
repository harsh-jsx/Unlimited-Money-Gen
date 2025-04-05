import time
from ppadb.client import Client as AdbClient
from PIL import Image
import numpy as np
import pyautogui


client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037
devices = client.devices()

if len(devices) == 0:
    print('No devices')
    quit()

device = devices[0]
 
print(f"Connected to device: {device.serial}")

#Make the device open an app named slice 
#List out the apps on the device and find the app id of the app you want to open
apps = device.shell("pm list packages")
#Open package:indwin.c3.shareapp
device.shell("monkey -p indwin.c3.shareapp" " -c android.intent.category.LAUNCHER 1")
time.sleep(5)
device.shell("input tap 500 500") # Tap on the screen to open the app
#Enter 6969
device.shell("input text 6969") # Enter the number 6969

pyautogui.click(867,992)
time.sleep(1)
pyautogui.click(854,280)

