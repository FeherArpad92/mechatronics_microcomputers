def logic_gate(input_a, input_b, gate_type):
    """
    Simulates basic digital logic gates.
    
    Args:
        input_a (int/bool): First input (0 or 1).
        input_b (int/bool): Second input (0 or 1).
        gate_type (str): Type of gate ("AND", "OR", "XOR").
        
    Returns:
        bool: The result of the logic operation.
    """
    if gate_type == "AND":
        # AND: True only if BOTH inputs are True
        return input_a and input_b
    elif gate_type == "OR":
        # OR: True if AT LEAST ONE input is True
        return input_a or input_b
    elif gate_type == "XOR":
        # XOR (Exclusive OR): True if inputs are DIFFERENT
        return input_a != input_b
    else:
        return None

def test_logic_gates():
    print("Logic Gate Simulator")
    print("Truth Table Verification:")
    
    # Define all possible input combinations for 2 bits
    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    
    # Header
    print(f"{'A':<5} {'B':<5} | {'AND':<5} {'OR':<5} {'XOR':<5}")
    print("-" * 30)
    
    # Iterate through all combinations
    for a, b in inputs:
        # Calculate results for each gate type
        res_and = int(logic_gate(a, b, "AND"))
        res_or = int(logic_gate(a, b, "OR"))
        res_xor = int(logic_gate(a, b, "XOR"))
        
        # Print row
        print(f"{a:<5} {b:<5} | {res_and:<5} {res_or:<5} {res_xor:<5}")

if __name__ == "__main__":
    test_logic_gates()
