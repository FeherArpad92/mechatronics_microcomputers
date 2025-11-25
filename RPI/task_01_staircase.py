from machine import Pin
import time

# Hardware Setup
button = Pin(10, Pin.IN, Pin.PULL_DOWN) # B0
led = Pin(16, Pin.OUT)                  # Y0

target_time = 0

while True:
    current_time = time.ticks_ms()
    
    if button.value() == 1:
        # Retriggerable: Update target time to 5 seconds from NOW
        target_time = time.ticks_add(current_time, 5000)
        led.value(1) # Turn ON
        # Simple debounce
        time.sleep(0.2)
        
    if time.ticks_diff(target_time, current_time) < 0:
        # Time expired
        led.value(0) # Turn OFF
        
    time.sleep(0.01) # Small delay to prevent CPU hogging
