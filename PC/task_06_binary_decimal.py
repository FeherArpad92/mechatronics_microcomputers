def binary_to_decimal():
    bits = [1, 0, 1, 0] # Example: 1010
    print(f"Binary List: {bits}")
    
    # Calculate integer
    # bits[0] is MSB (Most Significant Bit) in this example context? 
    # The prompt says: bits = [1, 0, 1, 0] -> 10. 
    # So index 0 is 8s place (2^3), index 3 is 1s place (2^0).
    
    value = (bits[0] * 8) + (bits[1] * 4) + (bits[2] * 2) + (bits[3] * 1)
    
    print(f"Decimal Value: {value}")
    
    # Generic way
    value_generic = 0
    for bit in bits:
        value_generic = (value_generic << 1) | bit
    print(f"Calculated Generic: {value_generic}")

if __name__ == "__main__":
    binary_to_decimal()
