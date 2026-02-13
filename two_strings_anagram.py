def is_anagram(str1, str2):
    # Convert both strings to lowercase (to ignore case differences)
    # Sort the letters alphabetically
    # Compare if the sorted letters are exactly the same
    # If they match, the words are anagrams (same letters, different order)
    return sorted(str1.lower()) == sorted(str2.lower())

# Test the function
# "listen" → sorted: ['e', 'i', 'l', 'n', 's', 't']
# "silent" → sorted: ['e', 'i', 'l', 'n', 's', 't']
# Both have the same letters, so they're anagrams!
# Expected output: True
print(is_anagram("listen", "silent"))