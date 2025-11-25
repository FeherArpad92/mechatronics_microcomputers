def binary_to_decimal():
    # Define a list representing 4 bits.
    # Index 0 is the Most Significant Bit (MSB) -> Value 8
    # Index 3 is the Least Significant Bit (LSB) -> Value 1
    # Example: [1, 0, 1, 0] represents binary 1010
    bits = [1, 0, 1, 0] 
    
    print(f"Binary List: {bits}")
    
    # METHOD 1: Manual Calculation
    # We multiply each bit by its corresponding weight (power of 2)
    # bits[0] * 2^3 = 8
    # bits[1] * 2^2 = 4
    # bits[2] * 2^1 = 2
    # bits[3] * 2^0 = 1
    value = (bits[0] * 8) + (bits[1] * 4) + (bits[2] * 2) + (bits[3] * 1)
    
    print(f"Decimal Value (Manual): {value}")
    
    # METHOD 2: Algorithmic Loop (Generic)
    # This works for any number of bits.
    # We shift the accumulated value left (multiply by 2) and add the new bit.
    value_generic = 0
    for bit in bits:
        # Shift current total to the left by 1 bit (equivalent to x * 2)
        # OR operation adds the new bit to the LSB position (equivalent to + bit)
        value_generic = (value_generic << 1) | bit
        
    print(f"Decimal Value (Loop):   {value_generic}")

if __name__ == "__main__":
    binary_to_decimal()
