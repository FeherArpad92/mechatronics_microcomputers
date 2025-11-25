from machine import Pin
import time

# Hardware Setup
button = Pin(10, Pin.IN, Pin.PULL_DOWN) # B0
led_single = Pin(16, Pin.OUT)           # Y0
led_double = Pin(17, Pin.OUT)           # Y1

last_press_time = 0
waiting_for_second_click = False

while True:
    current_time = time.ticks_ms()
    
    if button.value() == 1:
        # Rising edge detected
        if waiting_for_second_click:
            # Second click detected!
            diff = time.ticks_diff(current_time, last_press_time)
            if diff < 400:
                print("DOUBLE CLICK")
                led_double.value(1)
                time.sleep(0.2)
                led_double.value(0)
                waiting_for_second_click = False
        else:
            # First click
            last_press_time = current_time
            waiting_for_second_click = True
            
        time.sleep(0.2) # Debounce to avoid reading same press twice
        
    # Timeout check
    if waiting_for_second_click:
        if time.ticks_diff(current_time, last_press_time) >= 400:
            print("SINGLE CLICK")
            led_single.value(1)
            time.sleep(0.2)
            led_single.value(0)
            waiting_for_second_click = False
            
    time.sleep(0.01)
