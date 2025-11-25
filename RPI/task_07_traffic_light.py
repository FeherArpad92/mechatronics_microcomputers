from machine import Pin
import time

# Hardware Setup
led_red = Pin(16, Pin.OUT)    # Y0
led_yellow = Pin(17, Pin.OUT) # Y1
led_green = Pin(18, Pin.OUT)  # Y2
btn_night = Pin(10, Pin.IN, Pin.PULL_DOWN) # B0

night_mode = False

# Interrupt Handler
def toggle_night_mode(pin):
    global night_mode
    # Simple software debounce in IRQ (not ideal but works for simple tasks)
    time.sleep_ms(50)
    if pin.value() == 1:
        night_mode = not night_mode
        print(f"Night Mode: {night_mode}")

# Attach Interrupt
btn_night.irq(trigger=Pin.IRQ_RISING, handler=toggle_night_mode)

def set_lights(r, y, g):
    led_red.value(r)
    led_yellow.value(y)
    led_green.value(g)

while True:
    if night_mode:
        # Night Mode: Blink Yellow
        set_lights(0, 1, 0)
        time.sleep(0.5)
        set_lights(0, 0, 0)
        time.sleep(0.5)
    else:
        # Normal Sequence
        # Red (3s)
        if night_mode: continue
        set_lights(1, 0, 0)
        for _ in range(30): # Check night mode every 100ms
            if night_mode: break
            time.sleep(0.1)
            
        # Red + Yellow (1s)
        if night_mode: continue
        set_lights(1, 1, 0)
        for _ in range(10):
            if night_mode: break
            time.sleep(0.1)
            
        # Green (3s)
        if night_mode: continue
        set_lights(0, 0, 1)
        for _ in range(30):
            if night_mode: break
            time.sleep(0.1)
            
        # Yellow (1s)
        if night_mode: continue
        set_lights(0, 1, 0)
        for _ in range(10):
            if night_mode: break
            time.sleep(0.1)
