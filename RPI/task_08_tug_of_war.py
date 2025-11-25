from machine import Pin
import time

# --- HARDWARE CONFIGURATION ---
btn_left = Pin(10, Pin.IN, Pin.PULL_DOWN)  # B0: Player Left
btn_right = Pin(13, Pin.IN, Pin.PULL_DOWN) # B3: Player Right

# We use a list to manage the 4 LEDs easily
leds = [
    Pin(16, Pin.OUT), # Y0 (Left End)
    Pin(17, Pin.OUT), # Y1
    Pin(18, Pin.OUT), # Y2
    Pin(19, Pin.OUT)  # Y3 (Right End)
]

# --- GAME STATE ---
# We map the "rope position" (0-9) to the LEDs.
# 0-2: Y0 lit (Left winning)
# 3-4: Y1 lit
# 5-6: Y2 lit
# 7-9: Y3 lit (Right winning)
# <0: Left Wins Game
# >9: Right Wins Game
position = 5 # Start in the middle

def update_leds(pos):
    """Updates LEDs based on rope position and checks for win condition."""
    # Turn all off first
    for led in leds: led.value(0)
    
    # Check Win Conditions
    if pos < 0: 
        return "LEFT"
    elif pos > 9: 
        return "RIGHT"
    
    # Map position to LED
    if 0 <= pos <= 2: leds[0].value(1)
    elif 3 <= pos <= 4: leds[1].value(1)
    elif 5 <= pos <= 6: leds[2].value(1)
    elif 7 <= pos <= 9: leds[3].value(1)
    
    return None # No winner yet

# Initial State: Turn on center LEDs
leds[1].value(1)
leds[2].value(1)

# Variables for Edge Detection
last_l, last_r = 0, 0

while True:
    # Read current button states
    curr_l = btn_left.value()
    curr_r = btn_right.value()
    
    # EDGE DETECTION: Left Button
    # We only act when the button changes from 0 to 1 (Rising Edge)
    if curr_l == 1 and last_l == 0:
        position -= 1
        print(f"Left Pull! Pos: {position}")
    
    # EDGE DETECTION: Right Button
    if curr_r == 1 and last_r == 0:
        position += 1
        print(f"Right Pull! Pos: {position}")
        
    # Update history for next loop
    last_l = curr_l
    last_r = curr_r
    
    # Update Display and Check Win
    win = update_leds(position)
    
    if win:
        print(f"{win} WINS!")
        # VICTORY ANIMATION: Flash all LEDs
        for _ in range(5):
            for led in leds: led.value(1)
            time.sleep(0.2)
            for led in leds: led.value(0)
            time.sleep(0.2)
            
        # RESET GAME
        position = 5 
        leds[1].value(1)
        leds[2].value(1)
        
    time.sleep(0.05) # Loop delay
