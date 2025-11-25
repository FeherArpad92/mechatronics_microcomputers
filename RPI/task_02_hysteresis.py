from machine import Pin
import time

# Hardware Setup
btn_up = Pin(10, Pin.IN, Pin.PULL_DOWN)   # B0 (+)
btn_down = Pin(11, Pin.IN, Pin.PULL_DOWN) # B1 (-)
heater_led = Pin(16, Pin.OUT)             # Y0

temperature = 20 # Start at 20
heater_state = False

def update_heater(temp, current_state):
    if temp < 18:
        return True # ON
    elif temp > 22:
        return False # OFF
    else:
        return current_state # Hold

while True:
    if btn_up.value() == 1:
        temperature += 1
        print(f"Temp: {temperature}")
        time.sleep(0.2) # Debounce
        
    if btn_down.value() == 1:
        temperature -= 1
        print(f"Temp: {temperature}")
        time.sleep(0.2) # Debounce
        
    heater_state = update_heater(temperature, heater_state)
    
    if heater_state:
        heater_led.value(1)
    else:
        heater_led.value(0)
        
    time.sleep(0.05)
