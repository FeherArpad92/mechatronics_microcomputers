import time

def staircase_light():
    # Initialize the timer variable.
    # This represents the remaining time in seconds for the light to stay on.
    timer = 0
    
    print("Staircase Light Timer Simulation")
    print("Instructions:")
    print(" - Press 'Enter' to simulate pressing the light switch (Button).")
    print(" - Type 'w' and Enter to wait 1 second (simulate time passing).")
    print(" - Type 'exit' to quit the simulation.")

    while True:
        # Get user input to simulate events
        user_input = input("Input: ").strip().lower()
        
        if user_input == 'exit':
            break
        
        if user_input == '':
            # EVENT: Button Pressed
            # Logic: The timer is reset to 10 seconds.
            # This makes the timer "retriggerable" - pressing it again extends the time back to full.
            timer = 10
            print(f"Button pressed! Timer reset to {timer} seconds.")
            
        elif user_input == 'w':
            # EVENT: Time Passing
            # Logic: Decrease the timer by 1 second, but don't go below 0.
            if timer > 0:
                timer -= 1
            print(f"1 second passed. Timer remaining: {timer}")
        
        # OUTPUT: Check the state of the light based on the timer
        if timer > 0:
            print(">> LIGHT ON")
        else:
            print(">> DARK")

if __name__ == "__main__":
    staircase_light()
