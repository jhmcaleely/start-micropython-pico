import time
import network
import rp2
rp2.country("GB")

# place wifi.py next to this file, with:
# ssid = "Your SSID"
# psk = "Your Wifi Password"
from wifi import ssid, psk

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, psk)

while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting for Wi-Fi connection...")
    time.sleep(1)

print(wlan.ifconfig())
print(wlan.isconnected())