from machine import Pin
import time

# --- HARDWARE CONFIGURATION ---
led_red = Pin(16, Pin.OUT)    # Y0: Red Light
led_yellow = Pin(17, Pin.OUT) # Y1: Yellow Light
led_green = Pin(18, Pin.OUT)  # Y2: Green Light
btn_night = Pin(10, Pin.IN, Pin.PULL_DOWN) # B0: Night Mode Toggle

# --- VARIABLES ---
night_mode = False # Global state variable for Night Mode

# --- INTERRUPT HANDLER ---
# This function runs automatically when the button is pressed.
# It interrupts the main loop immediately.
def toggle_night_mode(pin):
    global night_mode
    # Simple software debounce inside interrupt (not ideal for complex apps but okay here)
    time.sleep_ms(50)
    
    if pin.value() == 1:
        # Toggle the state (True -> False, False -> True)
        night_mode = not night_mode
        print(f"Night Mode: {night_mode}")

# Attach the interrupt to the button
# Trigger on RISING edge (when button is pressed down)
btn_night.irq(trigger=Pin.IRQ_RISING, handler=toggle_night_mode)

def set_lights(r, y, g):
    """Helper function to set all 3 LEDs at once."""
    led_red.value(r)
    led_yellow.value(y)
    led_green.value(g)

while True:
    if night_mode:
        # --- NIGHT MODE SEQUENCE ---
        # Blink Yellow continuously
        set_lights(0, 1, 0) # Yellow ON
        time.sleep(0.5)
        set_lights(0, 0, 0) # All OFF
        time.sleep(0.5)
    else:
        # --- NORMAL TRAFFIC SEQUENCE ---
        
        # 1. RED (Stop)
        if night_mode: continue # Check if mode changed
        set_lights(1, 0, 0)
        # We use a loop for delay to allow faster reaction to night mode switch
        for _ in range(30): # 30 * 0.1s = 3 seconds
            if night_mode: break
            time.sleep(0.1)
            
        # 2. RED + YELLOW (Prepare)
        if night_mode: continue
        set_lights(1, 1, 0)
        for _ in range(10): # 1 second
            if night_mode: break
            time.sleep(0.1)
            
        # 3. GREEN (Go)
        if night_mode: continue
        set_lights(0, 0, 1)
        for _ in range(30): # 3 seconds
            if night_mode: break
            time.sleep(0.1)
            
        # 4. YELLOW (Slow)
        if night_mode: continue
        set_lights(0, 1, 0)
        for _ in range(10): # 1 second
            if night_mode: break
            time.sleep(0.1)
