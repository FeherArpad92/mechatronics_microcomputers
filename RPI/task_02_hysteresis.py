from machine import Pin
import time

# --- HARDWARE CONFIGURATION ---
btn_up = Pin(10, Pin.IN, Pin.PULL_DOWN)   # B0: Increase Temp
btn_down = Pin(11, Pin.IN, Pin.PULL_DOWN) # B1: Decrease Temp
heater_led = Pin(16, Pin.OUT)             # Y0: Heater Indicator

# --- VARIABLES ---
temperature = 20 # Initial virtual temperature
heater_state = False # Initial heater state (Off)

def update_heater(temp, current_state):
    """
    Determines the heater state based on temperature and hysteresis.
    """
    # Logic 1: Too Cold -> Turn ON
    if temp < 18:
        return True 
    # Logic 2: Too Hot -> Turn OFF
    elif temp > 22:
        return False 
    # Logic 3: Hysteresis Zone -> Keep Current State
    else:
        return current_state 

while True:
    # INPUT HANDLING: Increase Temperature
    if btn_up.value() == 1:
        temperature += 1
        print(f"Temp: {temperature}")
        time.sleep(0.2) # Debounce
        
    # INPUT HANDLING: Decrease Temperature
    if btn_down.value() == 1:
        temperature -= 1
        print(f"Temp: {temperature}")
        time.sleep(0.2) # Debounce
        
    # CONTROL LOGIC: Update heater state
    heater_state = update_heater(temperature, heater_state)
    
    # OUTPUT CONTROL: Set LED
    if heater_state:
        heater_led.value(1) # ON
    else:
        heater_led.value(0) # OFF
        
    time.sleep(0.05) # Loop delay
