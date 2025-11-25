def thermostat(measured_value, current_state):
    if measured_value < 18:
        return True # Heater ON
    elif measured_value > 22:
        return False # Heater OFF
    else:
        return current_state # Hold

def run_simulation():
    test_values = [17, 19, 21, 23, 21, 19, 17]
    heater_state = False # Initial state
    
    print(f"{'Measured':<10} | {'Heater State':<10}")
    print("-" * 25)
    
    for value in test_values:
        heater_state = thermostat(value, heater_state)
        state_str = "ON" if heater_state else "OFF"
        print(f"{value:<10} | {state_str:<10}")

if __name__ == "__main__":
    run_simulation()
