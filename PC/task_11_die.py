import random
import time

def electronic_die_simulation():
    print("Electronic Die Simulation")
    print("Simulates rolling a 4-sided die (values 1-4).")
    
    while True:
        user_input = input("Press Enter to Roll (or type 'exit'): ")
        if user_input.lower() == 'exit':
            break
            
        print("Rolling...", end="", flush=True)
        
        # ANIMATION SIMULATION
        # In hardware, this would be LEDs flashing rapidly.
        # Here, we print dots with a small delay to build suspense.
        for _ in range(3):
            time.sleep(0.2)
            print(".", end="", flush=True)
        print() # Newline
        
        # RANDOM GENERATION
        # Generate a random integer between 1 and 4 (inclusive)
        result = random.randint(1, 4) 
        
        print(f"Result: {result}")
        print("-" * 20)

if __name__ == "__main__":
    electronic_die_simulation()
