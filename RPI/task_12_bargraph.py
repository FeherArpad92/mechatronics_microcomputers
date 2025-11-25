from machine import Pin
import time

# Hardware Setup
btn_up = Pin(10, Pin.IN, Pin.PULL_DOWN)   # B0
btn_down = Pin(11, Pin.IN, Pin.PULL_DOWN) # B1
leds = [
    Pin(16, Pin.OUT), # Y0 (Level 1)
    Pin(17, Pin.OUT), # Y1 (Level 2)
    Pin(18, Pin.OUT), # Y2 (Level 3)
    Pin(19, Pin.OUT)  # Y3 (Level 4)
]

level = 0 # 0 to 4

def update_leds(lvl):
    for i in range(4):
        if i < lvl:
            leds[i].value(1)
        else:
            leds[i].value(0)

while True:
    if btn_up.value() == 1:
        if level < 4:
            level += 1
            update_leds(level)
            print(f"Level: {level}")
        time.sleep(0.2) # Debounce
        
    if btn_down.value() == 1:
        if level > 0:
            level -= 1
            update_leds(level)
            print(f"Level: {level}")
        time.sleep(0.2) # Debounce
        
    time.sleep(0.05)
