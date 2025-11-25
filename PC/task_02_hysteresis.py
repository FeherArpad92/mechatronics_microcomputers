def thermostat(measured_value, current_state):
    """
    Simulates a thermostat with hysteresis.
    
    Args:
        measured_value (float): The current temperature reading.
        current_state (bool): The current state of the heater (True=ON, False=OFF).
        
    Returns:
        bool: The new state of the heater.
    """
    
    # Logic 1: Low Threshold
    # If temperature is below 18, we MUST turn the heater ON to warm up.
    if measured_value < 18:
        return True # Heater ON
        
    # Logic 2: High Threshold
    # If temperature is above 22, we MUST turn the heater OFF to cool down.
    elif measured_value > 22:
        return False # Heater OFF
        
    # Logic 3: Hysteresis Zone (Deadband)
    # If temperature is between 18 and 22, we do NOT change the state.
    # This prevents rapid toggling (flickering) if the temp hovers around a single point.
    else:
        return current_state # Maintain previous state

def run_simulation():
    # Test values simulating a temperature rising and then falling
    test_values = [17, 19, 21, 23, 21, 19, 17]
    
    # Initial state of the heater (assume OFF)
    heater_state = False 
    
    print(f"{'Measured Temp':<15} | {'Heater State':<15}")
    print("-" * 35)
    
    for value in test_values:
        # Update the state based on the new measurement
        heater_state = thermostat(value, heater_state)
        
        # Visualize the output
        state_str = "ON" if heater_state else "OFF"
        print(f"{value:<15} | {state_str:<15}")

if __name__ == "__main__":
    run_simulation()
