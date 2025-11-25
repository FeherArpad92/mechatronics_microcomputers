from machine import Pin
import time

# --- HARDWARE CONFIGURATION ---
btn_alive = Pin(10, Pin.IN, Pin.PULL_DOWN) # B0: Keep-Alive Button
btn_reset = Pin(11, Pin.IN, Pin.PULL_DOWN) # B1: Reset Alarm Button
led_status = Pin(16, Pin.OUT)              # Y0: Green Status LED (Normal)
led_alarm = Pin(17, Pin.OUT)               # Y1: Red Alarm LED (Danger)

# --- VARIABLES ---
last_press_time = time.ticks_ms()
alarm_active = False

while True:
    current_time = time.ticks_ms()
    
    # --- INPUT HANDLING ---
    
    # Check Keep-Alive Button (B0)
    if btn_alive.value() == 1:
        # Only accept keep-alive if alarm is NOT active
        if not alarm_active:
            last_press_time = current_time # Reset the watchdog timer
            print("Alive signal received.")
        time.sleep(0.1) # Debounce
        
    # Check Reset Button (B1)
    if btn_reset.value() == 1:
        # Only useful if alarm IS active
        if alarm_active:
            alarm_active = False # Clear alarm state
            last_press_time = current_time # Reset timer
            led_alarm.value(0) # Turn off Red LED
            print("System Reset.")
        time.sleep(0.5) # Long debounce for reset
        
    # --- STATE LOGIC ---
    
    if not alarm_active:
        # NORMAL STATE
        led_status.value(1) # Green ON
        
        # Check Watchdog Timer: Has it been > 2000ms?
        if time.ticks_diff(current_time, last_press_time) > 2000:
            # TRANSITION TO ALARM STATE
            alarm_active = True
            led_status.value(0) # Green OFF
            print("ALARM TRIGGERED!")
    else:
        # ALARM STATE
        # Blink Red LED to indicate danger
        led_alarm.toggle()
        time.sleep(0.2)
        
    time.sleep(0.01) # Loop delay
