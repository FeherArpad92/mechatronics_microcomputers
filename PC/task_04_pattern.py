def pattern_recorder():
    # Initialize an empty list to store the sequence.
    # Lists are dynamic arrays in Python, perfect for storing unknown amounts of data.
    pattern = []
    
    print("Pattern Recorder Simulation")
    print("We will record 5 inputs and then play them back.")
    print("Valid inputs are numbers 0, 1, 2, 3.")
    
    # RECORDING PHASE
    for i in range(5):
        while True:
            try:
                # Get input from user
                val = int(input(f"Enter value {i+1}/5: "))
                
                # Validation: Ensure input is within the allowed range
                if 0 <= val <= 3:
                    # Append valid input to our list (memory)
                    pattern.append(val)
                    break # Exit the validation loop and move to next input
                else:
                    print("Invalid! Please enter a number between 0 and 3.")
            except ValueError:
                print("Error! That's not a number.")
    
    # PLAYBACK PHASE
    print("\nRecording complete. Playing back pattern...")
    print("-" * 20)
    
    # Iterate through the stored list and display values
    for index, val in enumerate(pattern):
        print(f"Step {index+1}: Output Value {val}")

if __name__ == "__main__":
    pattern_recorder()
