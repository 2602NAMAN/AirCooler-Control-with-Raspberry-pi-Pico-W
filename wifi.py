import network
import time

# Connect to WiFi
ssid = 'Tatasky'
password = '<#1054_$2602>'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Function to get RSSI
def get_wifi_strength():
    if wlan.isconnected():
        rssi = wlan.status('rssi')
        return rssi
    else:
        return None

# Print WiFi signal strength
signal_strength = get_wifi_strength()
if signal_strength is not None:
    print("WiFi Signal Strength:", signal_strength)
else:
    print("WiFi not connected")

