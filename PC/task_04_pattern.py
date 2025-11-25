def pattern_recorder():
    pattern = []
    print("Pattern Recorder Simulation")
    print("Enter 5 numbers (0-3) to record a pattern.")
    
    for i in range(5):
        while True:
            try:
                val = int(input(f"Entry {i+1}: "))
                if 0 <= val <= 3:
                    pattern.append(val)
                    break
                else:
                    print("Please enter a number between 0 and 3.")
            except ValueError:
                print("Invalid input. Enter a number.")
    
    print("\nRecording complete. Playing back pattern:")
    for val in pattern:
        print(f"Pattern Value: {val}")

if __name__ == "__main__":
    pattern_recorder()
