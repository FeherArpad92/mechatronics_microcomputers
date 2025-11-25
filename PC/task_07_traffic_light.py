import time

def traffic_light_simulation():
    states = ["RED", "RED-YELLOW", "GREEN", "YELLOW"]
    current_state_idx = 0
    
    print("Traffic Light Simulator (Press Ctrl+C to stop)")
    
    try:
        while True:
            state_name = states[current_state_idx]
            
            # Visual Output
            if state_name == "RED":
                print("[R]  (Stop)")
                duration = 3
            elif state_name == "RED-YELLOW":
                print("[RY] (Prepare)")
                duration = 1
            elif state_name == "GREEN":
                print("[G]  (Go)")
                duration = 3
            elif state_name == "YELLOW":
                print("[Y]  (Slow)")
                duration = 1
            
            time.sleep(duration)
            
            # Next state
            current_state_idx = (current_state_idx + 1) % 4
            
    except KeyboardInterrupt:
        print("\nSimulation Stopped.")

if __name__ == "__main__":
    traffic_light_simulation()
