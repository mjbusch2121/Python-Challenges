# Import all lowercase letters: 'abcdefghijklmnopqrstuvwxyz'
from string import ascii_lowercase

def is_pangram(string):
    # Create a set of all 26 letters in the alphabet
    # set() removes duplicates: {'a', 'b', 'c', ..., 'z'}
    alphabet = set(ascii_lowercase)

    # Convert input to lowercase, then to a set of unique characters
    # Check if the string's character set contains ALL letters (>=)
    # >= means "is superset of" (contains all elements from alphabet)
    return set(string.lower()) >= alphabet

# Test with a famous pangram
# A pangram is a sentence that contains EVERY letter of the alphabet at least once
# Expected output: True
print(is_pangram("The quick brown fox jumps over the lazy dog"))