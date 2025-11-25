import time

def stopwatch_simulation():
    print("Stopwatch Simulation")
    
    input("Press Enter to Start")
    start_time = time.time()
    print("Stopwatch Running...")
    
    input("Press Enter to Stop")
    end_time = time.time()
    
    duration = end_time - start_time
    print(f"Elapsed time: {duration:.3f} seconds")

if __name__ == "__main__":
    stopwatch_simulation()
