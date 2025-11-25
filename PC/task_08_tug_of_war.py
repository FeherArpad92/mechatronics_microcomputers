def tug_of_war_simulation():
    # Initialize rope position. 0 is the center.
    # Negative values mean Player A is pulling (Left).
    # Positive values mean Player B is pulling (Right).
    rope_pos = 0
    
    print("Tug of War Simulation")
    print("Instructions:")
    print(" - Player A: Enter 'a' to pull left.")
    print(" - Player B: Enter 'b' to pull right.")
    print(" - Goal: Pull the rope to -10 (A wins) or +10 (B wins).")
    
    # Game Loop: Continue as long as no one has won yet
    # abs(rope_pos) < 10 means position is between -9 and 9
    while abs(rope_pos) < 10:
        # VISUALIZATION
        print(f"\nRope Position: {rope_pos}")
        visual = ['-'] * 21 # Create a list of 21 dashes
        visual[rope_pos + 10] = 'O' # Place the 'O' (rope center) at the correct index
        # Index 10 is the visual center (when rope_pos is 0)
        print("".join(visual))
        print("A <--- | ---> B")
        
        # INPUT
        move = input("Move: ").strip().lower()
        
        # LOGIC: Update position based on input
        if move == 'a':
            rope_pos -= 1 # Move left
        elif move == 'b':
            rope_pos += 1 # Move right
        elif move == 'exit':
            return
            
    # WIN CONDITION CHECK
    if rope_pos <= -10:
        print("\n!!! PLAYER A WINS !!!")
    else:
        print("\n!!! PLAYER B WINS !!!")

if __name__ == "__main__":
    tug_of_war_simulation()
