from machine import Pin
import time

# Hardware Setup
btn_alive = Pin(10, Pin.IN, Pin.PULL_DOWN) # B0
btn_reset = Pin(11, Pin.IN, Pin.PULL_DOWN) # B1
led_status = Pin(16, Pin.OUT)              # Y0 (Green)
led_alarm = Pin(17, Pin.OUT)               # Y1 (Red)

last_press_time = time.ticks_ms()
alarm_active = False

while True:
    current_time = time.ticks_ms()
    
    # Check Keep-Alive Button
    if btn_alive.value() == 1:
        if not alarm_active:
            last_press_time = current_time
            print("Alive signal received.")
        time.sleep(0.1) # Debounce
        
    # Check Reset Button
    if btn_reset.value() == 1:
        if alarm_active:
            alarm_active = False
            last_press_time = current_time
            led_alarm.value(0)
            print("System Reset.")
        time.sleep(0.5) # Long debounce for reset
        
    # Logic
    if not alarm_active:
        led_status.value(1)
        # Check timeout (2000ms)
        if time.ticks_diff(current_time, last_press_time) > 2000:
            alarm_active = True
            led_status.value(0)
            print("ALARM TRIGGERED!")
    else:
        # Alarm Mode: Blink Red LED
        led_alarm.toggle()
        time.sleep(0.2)
        
    time.sleep(0.01)
