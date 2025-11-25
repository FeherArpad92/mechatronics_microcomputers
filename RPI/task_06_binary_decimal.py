from machine import Pin
import time

# --- HARDWARE CONFIGURATION ---
# We use 4 buttons to represent a 4-bit binary number.
# B3 is MSB (Most Significant Bit), B0 is LSB (Least Significant Bit).
b0 = Pin(10, Pin.IN, Pin.PULL_DOWN) # Bit 0 (Value 1)
b1 = Pin(11, Pin.IN, Pin.PULL_DOWN) # Bit 1 (Value 2)
b2 = Pin(12, Pin.IN, Pin.PULL_DOWN) # Bit 2 (Value 4)
b3 = Pin(13, Pin.IN, Pin.PULL_DOWN) # Bit 3 (Value 8)

while True:
    # READ INPUTS
    # Get the current state (0 or 1) of each button
    val0 = b0.value()
    val1 = b1.value()
    val2 = b2.value()
    val3 = b3.value()
    
    # CALCULATE DECIMAL VALUE
    # We shift each bit to its correct position (weight).
    # val3 << 3 is equivalent to val3 * 8
    # val2 << 2 is equivalent to val2 * 4
    # val1 << 1 is equivalent to val1 * 2
    decimal_value = (val3 << 3) + (val2 << 2) + (val1 << 1) + val0
    
    # OUTPUT
    # Print the binary representation and the calculated decimal
    print(f"Binary: {val3}{val2}{val1}{val0} -> Decimal: {decimal_value}")
    
    # Update rate: 5 times per second
    time.sleep(0.2) 
