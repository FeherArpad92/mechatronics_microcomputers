from machine import Pin
import time

# Hardware Setup
btn_a = Pin(10, Pin.IN, Pin.PULL_DOWN) # B0
btn_b = Pin(11, Pin.IN, Pin.PULL_DOWN) # B1
led_and = Pin(16, Pin.OUT)             # Y0
led_or = Pin(17, Pin.OUT)              # Y1
led_xor = Pin(18, Pin.OUT)             # Y2

while True:
    a = btn_a.value()
    b = btn_b.value()
    
    # AND Gate
    if a == 1 and b == 1:
        led_and.value(1)
    else:
        led_and.value(0)
        
    # OR Gate
    if a == 1 or b == 1:
        led_or.value(1)
    else:
        led_or.value(0)
        
    # XOR Gate
    if a != b:
        led_xor.value(1)
    else:
        led_xor.value(0)
        
    time.sleep(0.05)
