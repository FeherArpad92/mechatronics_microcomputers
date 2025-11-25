from machine import Pin
import time

# --- HARDWARE CONFIGURATION ---
btn_mode = Pin(10, Pin.IN, Pin.PULL_DOWN)  # B0: Mode Button (Hold to Record)
btn_input = Pin(11, Pin.IN, Pin.PULL_DOWN) # B1: Input Button (Tap to create beat)
led = Pin(16, Pin.OUT)                     # Y0: Output LED

# --- VARIABLES ---
pattern = [] # List to store the relative timestamps of beats
recording = False
start_time = 0

while True:
    current_time = time.ticks_ms()
    
    # CHECK MODE: Is B0 held down?
    if btn_mode.value() == 1:
        # --- RECORDING MODE ---
        
        if not recording:
            # INITIALIZATION: Start of a new recording session
            print("Recording Started...")
            pattern = [] # Clear previous recording
            start_time = current_time
            recording = True
        
        # CHECK INPUT: Is B1 pressed?
        if btn_input.value() == 1:
            # Calculate when this press happened relative to start
            timestamp = time.ticks_diff(current_time, start_time)
            
            # Store it in our list
            pattern.append(timestamp)
            print(f"Recorded beat at {timestamp}ms")
            
            # Visual Feedback
            led.value(1) 
            time.sleep(0.2) # Debounce
            led.value(0)
            
    else:
        # --- PLAYBACK MODE ---
        
        if recording:
            # TRANSITION: Just released B0, so stop recording and start playback
            print("Recording Stopped. Playing back...")
            recording = False
            
            # Playback Logic
            play_start = time.ticks_ms()
            
            if not pattern:
                print("No pattern recorded.")
            else:
                # Iterate through recorded timestamps
                for beat_time in pattern:
                    # BUSY WAIT: Wait until the correct time has elapsed
                    # We check current time vs start time until it matches the recorded timestamp
                    while time.ticks_diff(time.ticks_ms(), play_start) < beat_time:
                        pass 
                    
                    # Trigger the beat (Flash LED)
                    led.value(1)
                    time.sleep(0.1)
                    led.value(0)
                    
                print("Playback finished.")
                
    time.sleep(0.01) # Loop delay
