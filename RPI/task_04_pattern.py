from machine import Pin
import time

# Hardware Setup
btn_mode = Pin(10, Pin.IN, Pin.PULL_DOWN)  # B0 (Record when held)
btn_input = Pin(11, Pin.IN, Pin.PULL_DOWN) # B1 (Input beat)
led = Pin(16, Pin.OUT)                     # Y0

pattern = [] # List to store timestamps
recording = False
start_time = 0

while True:
    current_time = time.ticks_ms()
    
    # Check Mode Button (B0)
    if btn_mode.value() == 1:
        if not recording:
            # Start Recording
            print("Recording Started...")
            pattern = [] # Clear previous
            start_time = current_time
            recording = True
        
        # Record Input Button (B1)
        if btn_input.value() == 1:
            timestamp = time.ticks_diff(current_time, start_time)
            pattern.append(timestamp)
            print(f"Recorded beat at {timestamp}ms")
            led.value(1) # Visual feedback
            time.sleep(0.2) # Debounce
            led.value(0)
            
    else:
        if recording:
            # Stop Recording
            print("Recording Stopped. Playing back...")
            recording = False
            
            # Playback
            play_start = time.ticks_ms()
            if not pattern:
                print("No pattern recorded.")
            else:
                # Iterate through recorded timestamps
                for beat_time in pattern:
                    # Wait until the correct time
                    while time.ticks_diff(time.ticks_ms(), play_start) < beat_time:
                        pass # Busy wait for precision
                    
                    # Flash LED
                    led.value(1)
                    time.sleep(0.1)
                    led.value(0)
                print("Playback finished.")
                
    time.sleep(0.01)
