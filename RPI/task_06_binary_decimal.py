from machine import Pin
import time

# Hardware Setup
b0 = Pin(10, Pin.IN, Pin.PULL_DOWN) # Bit 0 (LSB)
b1 = Pin(11, Pin.IN, Pin.PULL_DOWN) # Bit 1
b2 = Pin(12, Pin.IN, Pin.PULL_DOWN) # Bit 2
b3 = Pin(13, Pin.IN, Pin.PULL_DOWN) # Bit 3 (MSB)

while True:
    # Read values
    val0 = b0.value()
    val1 = b1.value()
    val2 = b2.value()
    val3 = b3.value()
    
    # Calculate Decimal
    decimal_value = (val3 << 3) + (val2 << 2) + (val1 << 1) + val0
    
    print(f"Binary: {val3}{val2}{val1}{val0} -> Decimal: {decimal_value}")
    
    time.sleep(0.2) # Update rate
