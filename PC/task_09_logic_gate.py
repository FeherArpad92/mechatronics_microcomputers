def logic_gate(input_a, input_b, gate_type):
    if gate_type == "AND":
        return input_a and input_b
    elif gate_type == "OR":
        return input_a or input_b
    elif gate_type == "XOR":
        return input_a != input_b
    else:
        return None

def test_logic_gates():
    print("Logic Gate Simulator")
    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    gates = ["AND", "OR", "XOR"]
    
    print(f"{'A':<5} {'B':<5} | {'AND':<5} {'OR':<5} {'XOR':<5}")
    print("-" * 30)
    
    for a, b in inputs:
        res_and = int(logic_gate(a, b, "AND"))
        res_or = int(logic_gate(a, b, "OR"))
        res_xor = int(logic_gate(a, b, "XOR"))
        
        print(f"{a:<5} {b:<5} | {res_and:<5} {res_or:<5} {res_xor:<5}")

if __name__ == "__main__":
    test_logic_gates()
