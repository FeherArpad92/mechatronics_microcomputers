from machine import Pin
import time

# Hardware Setup
btn_left = Pin(10, Pin.IN, Pin.PULL_DOWN)  # B0
btn_right = Pin(13, Pin.IN, Pin.PULL_DOWN) # B3
leds = [
    Pin(16, Pin.OUT), # Y0 (Left End)
    Pin(17, Pin.OUT), # Y1
    Pin(18, Pin.OUT), # Y2
    Pin(19, Pin.OUT)  # Y3 (Right End)
]

# Game State
# Position 0=Y0, 1=Y1, 2=Y2, 3=Y3
# Start in middle (between 1 and 2? Or just light up 1 and 2?)
# Prompt says: "Start with LEDs Y1 and Y2 ON (Center)."
# Shift left/right.
# Let's define position as a float or integer index.
# If we shift left, we light up lower indices.
# Let's say "Center" means index 1.5.
# Let's simplify: Position 0 to 5.
# 0: Left Win
# 1: Y0
# 2: Y1
# 3: Y2
# 4: Y3
# 5: Right Win
# Start at 2.5? No, let's start with Y1 and Y2 ON.
# Let's track a "balance" variable.
# -2 (Left Win), -1 (Y0), 0 (Y1+Y2), 1 (Y3), 2 (Right Win) - this is getting complicated.

# Alternative Logic:
# Rope Position: 0 to 3.
# Start: 1 and 2 ON.
# Left Press: Shift Left.
# Right Press: Shift Right.

# Let's implement a virtual position 0-10 like PC, but map to LEDs.
# Center = 5.
# 0-2: Y0
# 3-4: Y1
# 5-6: Y2
# 7-9: Y3
# <0: Left Win
# >9: Right Win

position = 5

def update_leds(pos):
    for led in leds: led.value(0)
    
    if pos < 0: # Left Win
        return "LEFT"
    elif pos > 9: # Right Win
        return "RIGHT"
    
    if 0 <= pos <= 2: leds[0].value(1)
    elif 3 <= pos <= 4: leds[1].value(1)
    elif 5 <= pos <= 6: leds[2].value(1)
    elif 7 <= pos <= 9: leds[3].value(1)
    return None

# Initial State
leds[1].value(1)
leds[2].value(1)

last_l, last_r = 0, 0

while True:
    curr_l = btn_left.value()
    curr_r = btn_right.value()
    
    # Rising Edge Detection
    if curr_l == 1 and last_l == 0:
        position -= 1
        print(f"Left Pull! Pos: {position}")
    
    if curr_r == 1 and last_r == 0:
        position += 1
        print(f"Right Pull! Pos: {position}")
        
    last_l = curr_l
    last_r = curr_r
    
    win = update_leds(position)
    
    if win:
        print(f"{win} WINS!")
        # Flash all
        for _ in range(5):
            for led in leds: led.value(1)
            time.sleep(0.2)
            for led in leds: led.value(0)
            time.sleep(0.2)
        position = 5 # Reset
        leds[1].value(1)
        leds[2].value(1)
        
    time.sleep(0.05)
