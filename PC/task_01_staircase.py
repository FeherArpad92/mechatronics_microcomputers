import time

def staircase_light():
    timer = 0
    print("Staircase Light Timer Simulation")
    print("Press 'Enter' to simulate button press, or wait.")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("Input (Press Enter for button, 'w' to wait 1s, 'exit' to quit): ").strip().lower()
        
        if user_input == 'exit':
            break
        
        if user_input == '':
            # Button pressed
            timer = 10
            print(f"Button pressed! Timer reset to {timer}")
        elif user_input == 'w':
            # Wait 1 second
            if timer > 0:
                timer -= 1
            print(f"Time passed. Timer: {timer}")
        
        if timer > 0:
            print("LIGHT ON")
        else:
            print("DARK")

if __name__ == "__main__":
    staircase_light()
