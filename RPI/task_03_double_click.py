from machine import Pin
import time

# --- HARDWARE CONFIGURATION ---
button = Pin(10, Pin.IN, Pin.PULL_DOWN) # B0: Input Button
led_single = Pin(16, Pin.OUT)           # Y0: Indicates Single Click
led_double = Pin(17, Pin.OUT)           # Y1: Indicates Double Click

# --- VARIABLES ---
last_press_time = 0
waiting_for_second_click = False

while True:
    current_time = time.ticks_ms()
    
    # EVENT: Button Pressed (Rising Edge)
    if button.value() == 1:
        
        if waiting_for_second_click:
            # CASE: Second click detected!
            # Check if it happened within the 400ms window
            diff = time.ticks_diff(current_time, last_press_time)
            
            if diff < 400:
                print("DOUBLE CLICK")
                # Flash Double Click LED
                led_double.value(1)
                time.sleep(0.2)
                led_double.value(0)
                
                # Reset state
                waiting_for_second_click = False
        else:
            # CASE: First click detected
            # Start the timer and wait for a potential second click
            last_press_time = current_time
            waiting_for_second_click = True
            
        # Debounce: Wait for button release/settle to avoid reading the same press twice
        time.sleep(0.2) 
        
    # TIMEOUT CHECK
    # If we are waiting for a second click, check if too much time has passed.
    if waiting_for_second_click:
        if time.ticks_diff(current_time, last_press_time) >= 400:
            # Timeout reached! It was just a Single Click.
            print("SINGLE CLICK")
            # Flash Single Click LED
            led_single.value(1)
            time.sleep(0.2)
            led_single.value(0)
            
            # Reset state
            waiting_for_second_click = False
            
    time.sleep(0.01) # Loop delay
