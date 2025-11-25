import time

def stopwatch_simulation():
    print("Stopwatch Simulation")
    print("This program measures the time elapsed between two user inputs.")
    
    # 1. START EVENT
    input("Press Enter to START the stopwatch...")
    
    # Capture the current time (in seconds since Epoch)
    start_time = time.time()
    print(">> Stopwatch Running... (Time is passing)")
    
    # 2. STOP EVENT
    input("Press Enter to STOP the stopwatch...")
    
    # Capture the stop time
    end_time = time.time()
    
    # 3. CALCULATION
    # The duration is simply the difference between the two timestamps
    duration = end_time - start_time
    
    # Display result formatted to 3 decimal places (milliseconds precision)
    print(f"Elapsed time: {duration:.3f} seconds")

if __name__ == "__main__":
    stopwatch_simulation()
