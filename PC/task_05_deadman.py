import time

def deadmans_switch_simulation():
    print("Deadman's Switch Simulation")
    print("Press 'Enter' to keep alive. If you wait > 2s, ALARM triggers.")
    print("If ALARM triggers, type 'reset' to reset.")
    
    last_press_time = time.time()
    alarm_active = False
    
    while True:
        current_time = time.time()
        
        # Check timer
        if not alarm_active and (current_time - last_press_time > 2.0):
            alarm_active = True
            print("\n!!! ALARM ACTIVATED !!!")
            print("System Locked. Type 'reset' to clear.")
            
        if alarm_active:
            user_input = input("ALARM! Type 'reset': ").strip().lower()
            if user_input == 'reset':
                alarm_active = False
                last_press_time = time.time()
                print("System Reset. Normal Operation.")
            elif user_input == 'exit':
                break
        else:
            # Normal operation
            print(f"Time since last press: {current_time - last_press_time:.1f}s")
            user_input = input("Press Enter to Keep Alive (or 'exit'): ")
            if user_input == 'exit':
                break
            # Any input resets the timer in normal mode
            last_press_time = time.time()
            print("Timer Reset.")

if __name__ == "__main__":
    deadmans_switch_simulation()
