def detect_clicks(timestamps):
    """
    Analyzes a list of timestamps to detect double clicks.
    
    Args:
        timestamps (list): A list of floats representing time of button presses in seconds.
    """
    print(f"Analyzing timestamps: {timestamps}")
    
    # Iterate through the list starting from the second element (index 1)
    for i in range(1, len(timestamps)):
        current_time = timestamps[i]
        previous_time = timestamps[i-1]
        
        # Calculate the time difference (delta t) between the current and previous press
        diff = current_time - previous_time
        
        # Logic: Double Click Threshold
        # If two presses happen within 0.5 seconds, it counts as a Double Click.
        if diff < 0.5:
            print(f"Time {current_time}: DOUBLE CLICK detected (diff={diff:.1f}s)")
        else:
            # Otherwise, it's just a separate Single Click
            print(f"Time {current_time}: SINGLE CLICK (diff={diff:.1f}s)")

if __name__ == "__main__":
    # Example data:
    # 1.0 -> Start
    # 1.2 -> 0.2s diff -> Double Click
    # 5.0 -> 3.8s diff -> Single Click
    # 5.8 -> 0.8s diff -> Single Click (Too slow for double)
    # 8.0 -> 2.2s diff -> Single Click
    timestamps = [1.0, 1.2, 5.0, 5.8, 8.0]
    detect_clicks(timestamps)
