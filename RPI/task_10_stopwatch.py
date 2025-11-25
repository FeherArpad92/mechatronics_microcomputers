from machine import Pin
import time

# Hardware Setup
button = Pin(10, Pin.IN, Pin.PULL_DOWN) # B0
led = Pin(16, Pin.OUT)                  # Y0

running = False
start_time = 0

while True:
    if button.value() == 1:
        if not running:
            # Start
            running = True
            start_time = time.ticks_ms()
            led.value(1)
            print("Stopwatch Started...")
        else:
            # Stop
            running = False
            end_time = time.ticks_ms()
            led.value(0)
            duration = time.ticks_diff(end_time, start_time)
            print(f"Elapsed time: {duration} ms")
            
        # Debounce / Wait for release
        time.sleep(0.2)
        while button.value() == 1:
            time.sleep(0.01)
            
    time.sleep(0.01)
