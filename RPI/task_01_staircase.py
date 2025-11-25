from machine import Pin
import time

# --- HARDWARE CONFIGURATION ---
# Button B0 is connected to GPIO 10.
# We use PULL_DOWN because the button connects to 3.3V when pressed.
# Default state (released) = 0 (Low). Pressed state = 1 (High).
button = Pin(10, Pin.IN, Pin.PULL_DOWN) 

# LED Y0 is connected to GPIO 16.
# We configure it as an OUTPUT to control it.
led = Pin(16, Pin.OUT)                  

# --- VARIABLES ---
target_time = 0 # The timestamp when the light should turn OFF

while True:
    # Get the current system time in milliseconds
    # This is a running counter since the board started.
    current_time = time.ticks_ms()
    
    # CHECK INPUT: Is the button pressed?
    if button.value() == 1:
        # LOGIC: Retriggerable Timer
        # We set the target time to be 5000ms (5 seconds) in the FUTURE.
        # time.ticks_add handles potential counter rollover safely.
        target_time = time.ticks_add(current_time, 5000)
        
        # Turn the LED ON immediately
        led.value(1) 
        
        # Simple Debounce: Wait 200ms to ignore mechanical noise
        # This prevents the code from registering multiple presses for one physical click.
        time.sleep(0.2)
        
    # CHECK TIMER: Has the time expired?
    # time.ticks_diff(a, b) calculates (a - b) handling rollover.
    # If target_time - current_time is negative, it means current_time > target_time.
    if time.ticks_diff(target_time, current_time) < 0:
        # Time is up! Turn the LED OFF.
        led.value(0) 
        
    # Short delay to prevent the loop from running too fast and consuming max power
    time.sleep(0.01) 
