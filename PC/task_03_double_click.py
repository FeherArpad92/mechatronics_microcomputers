def detect_clicks(timestamps):
    print(f"Analyzing timestamps: {timestamps}")
    
    for i in range(1, len(timestamps)):
        current_time = timestamps[i]
        previous_time = timestamps[i-1]
        diff = current_time - previous_time
        
        if diff < 0.5:
            print(f"Time {current_time}: DOUBLE CLICK detected (diff={diff:.1f}s)")
        else:
            print(f"Time {current_time}: SINGLE CLICK (diff={diff:.1f}s)")

if __name__ == "__main__":
    timestamps = [1.0, 1.2, 5.0, 5.8, 8.0]
    detect_clicks(timestamps)
