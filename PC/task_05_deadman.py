import time

def deadmans_switch_simulation():
    print("Deadman's Switch Simulation")
    print("Concept: You must perform an action periodically to prove you are 'alive/active'.")
    print("Instructions:")
    print(" - Press 'Enter' repeatedly to reset the timer (Keep Alive).")
    print(" - If you wait longer than 2.0 seconds, the ALARM will trigger.")
    print(" - Once ALARM is active, you must type 'reset' to stop it.")
    
    # Initialize state variables
    last_press_time = time.time()
    alarm_active = False
    
    while True:
        current_time = time.time()
        
        # CHECK: Has the timer expired?
        # Only check if alarm is NOT already active.
        if not alarm_active and (current_time - last_press_time > 2.0):
            alarm_active = True
            print("\n!!! ALARM ACTIVATED !!!")
            print("System Locked. The normal 'Enter' key won't work anymore.")
            print("Type 'reset' to clear the alarm.")
            
        if alarm_active:
            # ALARM STATE LOGIC
            # In this state, we block normal operation and wait for a specific reset command.
            user_input = input("ALARM! Type 'reset': ").strip().lower()
            
            if user_input == 'reset':
                # Reset the system to normal
                alarm_active = False
                last_press_time = time.time() # Reset timer immediately
                print("System Reset. Normal Operation restored.")
            elif user_input == 'exit':
                break
        else:
            # NORMAL STATE LOGIC
            # Show how much time has passed since last check-in
            elapsed = current_time - last_press_time
            print(f"Time since last check-in: {elapsed:.1f}s (Timeout at 2.0s)")
            
            user_input = input("Press Enter to Keep Alive (or 'exit'): ")
            
            if user_input == 'exit':
                break
                
            # Any input here counts as a "Keep Alive" signal
            last_press_time = time.time()
            print("Timer Reset.")

if __name__ == "__main__":
    deadmans_switch_simulation()
