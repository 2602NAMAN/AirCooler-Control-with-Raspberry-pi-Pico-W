import machine
import network
import socket
import time
import wifi_credentials
from machine import Pin
import _thread
from html_template import HTML_TEMPLATE

# Access the SSID and password from the credentials module
ssid = wifi_credentials.SSID
password = wifi_credentials.PASSWORD

relay1 = Pin(19, Pin.OUT) #change according to your need
relay2 = Pin(20, Pin.OUT) #change according to your need
relay3 = Pin(21, Pin.OUT) #change according to your need

relay1.value(0)
relay2.value(0)
relay3.value(0)

relayState = "Relays are OFF"

led = Pin("LED", Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0])
    for i in range(6):
        led.toggle()
        time.sleep_ms(200)

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

addr = socket.getaddrinfo('0.0.0.0', 1025)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on', addr)

loop_running = False
global_timer_running = False
global_timer_stop = False

def loop_relay(on_duration, off_duration, relay):
    global loop_running
    loop_running = True
    while loop_running:
        relay.value(0)
        time.sleep(on_duration)
        relay.value(1)
        time.sleep(off_duration)
    print("Loop stopped")

def stop_loop():
    global loop_running
    loop_running = False
    print("Stopping loop...")

def start_loop(on_duration, off_duration):
    global loop_running
    if not loop_running:
        _thread.start_new_thread(loop_relay, (on_duration, off_duration, relay3))
        print("Loop started")
    else:
        print("Loop is already running")

def global_timer(hours, minutes):
    global global_timer_running, loop_running, global_timer_stop
    
    global_timer_running = True
    global_timer_stop = False

    total_seconds = (hours * 3600) + (minutes * 60)
    for _ in range(total_seconds):
        if global_timer_stop:
            break
        time.sleep(1)
    
    # Stop the relay loop if running
    if loop_running:
        stop_loop()
        time.sleep(1)  # Ensure the loop stops completely before turning off relays
    
    # Turn off all relays
    relay1.value(1)
    relay2.value(1)
    relay3.value(1)
    global_timer_running = False

def stop_global_timer():
    global global_timer_stop
    global_timer_stop = True

def reset_all():
    global loop_running, global_timer_stop, global_timer_running
    
    if loop_running:
        stop_loop()
        time.sleep(1)  # Ensure the loop stops completely
    
    if global_timer_running:
        stop_global_timer()
        time.sleep(1)  # Ensure the global timer stops completely
    
    relay1.value(1)
    relay2.value(1)
    relay3.value(1)
    loop_running = False
    global_timer_running = False
    global_timer_stop = False

def parse_query(query_string):
    params = {}
    pairs = query_string.split('&')
    for pair in pairs:
        key, value = pair.split('=')
        params[key] = value
    return params

def turn_all_relays(on):
    if on:
        relay1.value(0)
        relay2.value(0)
        relay3.value(0)
        return "All relays are ON"
    else:
        relay1.value(1)
        relay2.value(1)
        relay3.value(1)
        return "All relays are OFF"

while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024)
        print(request)

        request = str(request)
        relay1_on = request.find('/relay1/on')
        relay1_off = request.find('/relay1/off')
        relay2_on = request.find('/relay2/on')
        relay2_off = request.find('/relay2/off')
        relay3_on = request.find('/relay3/on')
        relay3_off = request.find('/relay3/off')
        relays_on = request.find('/relays/on')
        relays_off = request.find('/relays/off')
        loop = request.find('/loop')
        stop_loop_request = request.find('/stop-loop')
        global_timer_request = request.find('/global-timer')
        stop_global_timer_request = request.find('/stop-global-timer')
        reset_request = request.find('/reset')

        if relay1_on == 6:
            print("relay 1 on")
            relay1.value(0)
            relayState = "Relay 1 is ON"
        elif relay1_off == 6:
            print("relay 1 off")
            relay1.value(1)
            relayState = "Relay 1 is OFF"

        if relay2_on == 6:
            print("relay 2 on")
            relay2.value(0)
            relayState = "Relay 2 is ON"
        elif relay2_off == 6:
            print("relay 2 off")
            relay2.value(1)
            relayState = "Relay 2 is OFF"

        if relay3_on == 6:
            print("relay 3 on")
            relay3.value(0)
            relayState = "Relay 3 is ON"
        elif relay3_off == 6:
            print("relay 3 off")
            relay3.value(1)
            relayState = "Relay 3 is OFF"

        if relays_on == 6:
            relayState = turn_all_relays(True)
        elif relays_off == 6:
            relayState = turn_all_relays(False)

        if loop == 6:
            params_start = request.find('?') + 1
            params_end = request.find(' ', params_start)
            query_string = request[params_start:params_end]
            params = parse_query(query_string)
            on_duration = int(params.get('on-duration', 1)) * 60
            off_duration = int(params.get('off-duration', 1)) * 60
            stop_loop()  # Stop the loop before starting a new one
            start_loop(on_duration, off_duration)
            relayState = f"Loop started with on duration {on_duration//60} min and off duration {off_duration//60} min"

        if stop_loop_request == 6:
            stop_loop()
            relayState = "Pump loop stopped"

        if global_timer_request == 6:
            params_start = request.find('?') + 1
            params_end = request.find(' ', params_start)
            query_string = request[params_start:params_end]
            params = parse_query(query_string)
            hours = int(params.get('hours', 0))
            minutes = int(params.get('minutes', 0))
            if global_timer_running:
                stop_global_timer()
                time.sleep(1)  # Ensure the previous timer stops completely
            _thread.start_new_thread(global_timer, (hours, minutes))
            relayState = f"Global timer set for {hours} hours and {minutes} minutes"

        if stop_global_timer_request == 6:
            stop_global_timer()
            relayState = "Global timer stopped"

        if reset_request == 6:
            reset_all()
            relayState = "All settings reset"

        response = HTML_TEMPLATE % relayState
        cl.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()

    except OSError as e:
        cl.close()
        print('connection closed')
    except Exception as e:
        print('Error:', str(e))
        cl.close()
