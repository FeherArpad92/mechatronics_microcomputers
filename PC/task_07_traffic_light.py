import time

def traffic_light_simulation():
    # Define the states of our Finite State Machine (FSM)
    states = ["RED", "RED-YELLOW", "GREEN", "YELLOW"]
    
    # Start at the first state (RED)
    current_state_idx = 0
    
    print("Traffic Light Simulator (Finite State Machine)")
    print("Press Ctrl+C to stop the simulation.")
    
    try:
        while True:
            # Get the name of the current state
            state_name = states[current_state_idx]
            
            # STATE LOGIC: Determine output and duration based on current state
            if state_name == "RED":
                print("[R]  (Stop)")
                duration = 3 # Red stays on longer
            elif state_name == "RED-YELLOW":
                print("[RY] (Prepare)")
                duration = 1 # Short transition
            elif state_name == "GREEN":
                print("[G]  (Go)")
                duration = 3 # Green stays on longer
            elif state_name == "YELLOW":
                print("[Y]  (Slow)")
                duration = 1 # Short transition
            
            # Wait for the duration of the current state
            time.sleep(duration)
            
            # TRANSITION LOGIC: Move to the next state
            # We use modulo (%) operator to cycle back to 0 after the last state (3)
            # 0 -> 1 -> 2 -> 3 -> 0 ...
            current_state_idx = (current_state_idx + 1) % 4
            
    except KeyboardInterrupt:
        print("\nSimulation Stopped.")

if __name__ == "__main__":
    traffic_light_simulation()
