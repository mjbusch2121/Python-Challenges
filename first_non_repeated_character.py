# Import Counter - a tool that counts how many times each item appears
from collections import Counter

def find_first_non_repeated(string):
    # Count how many times each character appears in the string
    # Counter creates a dictionary: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
    char_counts = Counter(string)

    # Loop through characters in the ORIGINAL order
    for char in string:
        # Check if this character appears exactly once
        if char_counts[char] == 1:
            # Return the first character that appears only once
            return char

    # If no non-repeated character is found, return None
    return None

# Test the function
# "abracadabra" → 'c' is first non-repeated character
# a=5, b=2, r=2, c=1✓, d=1
# Expected output: c
print(find_first_non_repeated("abracadabra"))