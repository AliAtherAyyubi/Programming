def roman_to_integer(roman):
    # Mapping of Roman numerals to integers
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0  # To track the previous numeral's value

    # Iterate through the Roman numeral string in reverse
    for char in reversed(roman):
        current_value = roman_values[char]
        
        if current_value < prev_value:
            # If the current value is less than the previous one, subtract it
            total -= current_value
        else:
            # Otherwise, add it
            total += current_value
        
        # Update the previous value for the next iteration
        prev_value = current_value

    return total

# Test cases
print(roman_to_integer('IV'))  