def bargraph_simulation():
    # Initialize charge level (0 to 4)
    charge_level = 0
    max_level = 4
    
    print("Bargraph Display Simulation")
    print("Controls:")
    print(" '+' : Increase Level")
    print(" '-' : Decrease Level")
    print(" 'exit' : Quit")
    
    while True:
        # VISUALIZATION LOGIC
        # We want to display a bar like [**  ]
        # 'filled' contains asterisks equal to the current level
        filled = '*' * charge_level
        # 'empty' contains spaces for the remaining capacity
        empty = ' ' * (max_level - charge_level)
        
        print(f"\nLevel {charge_level}: [{filled}{empty}]")
        
        # INPUT HANDLING
        user_input = input("Input: ").strip()
        
        if user_input == '+':
            # Limit check: Don't exceed max level
            if charge_level < max_level:
                charge_level += 1
            else:
                print("Max level reached!")
                
        elif user_input == '-':
            # Limit check: Don't go below 0
            if charge_level > 0:
                charge_level -= 1
            else:
                print("Min level reached!")
                
        elif user_input == 'exit':
            break

if __name__ == "__main__":
    bargraph_simulation()
