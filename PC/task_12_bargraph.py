def bargraph_simulation():
    charge_level = 0
    max_level = 4
    
    print("Bargraph Display Simulation")
    print("Controls: '+' to increase, '-' to decrease, 'exit' to quit")
    
    while True:
        # Visualization
        # [ **  ] for level 2
        filled = '*' * charge_level
        empty = ' ' * (max_level - charge_level)
        print(f"Level {charge_level}: [{filled}{empty}]")
        
        user_input = input("Input: ").strip()
        
        if user_input == '+':
            if charge_level < max_level:
                charge_level += 1
        elif user_input == '-':
            if charge_level > 0:
                charge_level -= 1
        elif user_input == 'exit':
            break

if __name__ == "__main__":
    bargraph_simulation()
