from machine import Pin
import time

# --- HARDWARE CONFIGURATION ---
button = Pin(10, Pin.IN, Pin.PULL_DOWN) # B0: Start/Stop Toggle
led = Pin(16, Pin.OUT)                  # Y0: Status Indicator

# --- VARIABLES ---
running = False
start_time = 0

while True:
    # Check for Button Press
    if button.value() == 1:
        
        if not running:
            # EVENT: Start Timer
            running = True
            start_time = time.ticks_ms() # Record start time
            led.value(1) # Turn LED ON to indicate running
            print("Stopwatch Started...")
        else:
            # EVENT: Stop Timer
            running = False
            end_time = time.ticks_ms() # Record stop time
            led.value(0) # Turn LED OFF
            
            # Calculate duration
            duration = time.ticks_diff(end_time, start_time)
            print(f"Elapsed time: {duration} ms")
            
        # DEBOUNCE & WAIT FOR RELEASE
        # We wait here to ensure one press = one toggle
        time.sleep(0.2) 
        while button.value() == 1:
            time.sleep(0.01) # Wait until user lets go of the button
            
    time.sleep(0.01) # Loop delay
