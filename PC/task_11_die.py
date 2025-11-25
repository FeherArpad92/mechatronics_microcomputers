import random
import time

def electronic_die_simulation():
    print("Electronic Die Simulation")
    
    while True:
        user_input = input("Press Enter to Roll (or 'exit'): ")
        if user_input.lower() == 'exit':
            break
            
        print("Rolling...", end="", flush=True)
        # Simulate animation delay
        for _ in range(3):
            time.sleep(0.2)
            print(".", end="", flush=True)
        print()
        
        result = random.randint(1, 4) # 1-4 as per prompt (or 0-3 for LEDs)
        print(f"Result: {result}")

if __name__ == "__main__":
    electronic_die_simulation()
