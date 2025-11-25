from machine import Pin
import time
import random

# --- HARDWARE CONFIGURATION ---
button = Pin(10, Pin.IN, Pin.PULL_DOWN) # B0: Roll Button
# List of LEDs for the die faces/values (0-3)
leds = [
    Pin(16, Pin.OUT), # Y0
    Pin(17, Pin.OUT), # Y1
    Pin(18, Pin.OUT), # Y2
    Pin(19, Pin.OUT)  # Y3
]

while True:
    if button.value() == 1:
        # --- ANIMATION PHASE ---
        print("Rolling...")
        # Cycle through LEDs rapidly to simulate rolling
        for _ in range(3): # Do this 3 times
            for led in leds:
                led.value(1)
                time.sleep(0.05)
                led.value(0)
        
        # --- RESULT PHASE ---
        # Generate a random number between 0 and 3
        result = random.randint(0, 3)
        print(f"Result: {result}")
        
        # Turn on the corresponding LED
        leds[result].value(1)
        
        # WAIT FOR RELEASE
        while button.value() == 1:
            time.sleep(0.01)
            
        # Note: The LED stays ON until the next roll begins.
        # This allows the user to see the result.
        
    time.sleep(0.05) # Loop delay
