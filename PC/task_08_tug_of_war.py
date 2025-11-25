def tug_of_war_simulation():
    rope_pos = 0
    print("Tug of War Simulation")
    print("Player A: Enter 'a' | Player B: Enter 'b'")
    print("Goal: Reach -10 (A wins) or +10 (B wins)")
    
    while abs(rope_pos) < 10:
        print(f"Rope Position: {rope_pos}")
        visual = ['-'] * 21
        visual[rope_pos + 10] = 'O' # Center is index 10
        print("".join(visual))
        
        move = input("Move: ").strip().lower()
        
        if move == 'a':
            rope_pos -= 1
        elif move == 'b':
            rope_pos += 1
        elif move == 'exit':
            return
            
    if rope_pos <= -10:
        print("\nPLAYER A WINS!")
    else:
        print("\nPLAYER B WINS!")

if __name__ == "__main__":
    tug_of_war_simulation()
