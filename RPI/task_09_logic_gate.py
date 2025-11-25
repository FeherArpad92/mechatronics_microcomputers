from machine import Pin
import time

# --- HARDWARE CONFIGURATION ---
btn_a = Pin(10, Pin.IN, Pin.PULL_DOWN) # B0: Input A
btn_b = Pin(11, Pin.IN, Pin.PULL_DOWN) # B1: Input B

led_and = Pin(16, Pin.OUT)             # Y0: Result of AND
led_or = Pin(17, Pin.OUT)              # Y1: Result of OR
led_xor = Pin(18, Pin.OUT)             # Y2: Result of XOR

while True:
    # Read Inputs
    a = btn_a.value()
    b = btn_b.value()
    
    # --- LOGIC GATES ---
    
    # 1. AND Gate
    # Output is High only if BOTH inputs are High
    if a == 1 and b == 1:
        led_and.value(1)
    else:
        led_and.value(0)
        
    # 2. OR Gate
    # Output is High if EITHER input is High
    if a == 1 or b == 1:
        led_or.value(1)
    else:
        led_or.value(0)
        
    # 3. XOR Gate (Exclusive OR)
    # Output is High if inputs are DIFFERENT (one High, one Low)
    if a != b:
        led_xor.value(1)
    else:
        led_xor.value(0)
        
    time.sleep(0.05) # Loop delay
