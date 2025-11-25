from machine import Pin
import time
import random

# Hardware Setup
button = Pin(10, Pin.IN, Pin.PULL_DOWN) # B0
leds = [
    Pin(16, Pin.OUT), # Y0
    Pin(17, Pin.OUT), # Y1
    Pin(18, Pin.OUT), # Y2
    Pin(19, Pin.OUT)  # Y3
]

while True:
    if button.value() == 1:
        # Animation: Cycle through LEDs
        print("Rolling...")
        for _ in range(3): # 3 full cycles
            for led in leds:
                led.value(1)
                time.sleep(0.05)
                led.value(0)
        
        # Random Result
        result = random.randint(0, 3)
        print(f"Result: {result}")
        
        # Turn on the resulting LED
        leds[result].value(1)
        
        # Wait for release
        while button.value() == 1:
            time.sleep(0.01)
            
        # Keep lit for a moment or until next press?
        # Let's keep it lit until next press (or just leave it)
        # To restart, we just loop.
        
    time.sleep(0.05)
