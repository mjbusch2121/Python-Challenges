def count_vowels(string):
    vowels = "aeiou"  # Define what counts as a vowel
    count = 0  # Initialize counter
    for char in string:  # Loop through each character
        if char.lower() in vowels:  # Check if lowercase version is a vowel
            count += 1  # Increment counter if it's a vowel
    return count  # Return total count AFTER loop finishes

input_string = "Hello World!"
result = count_vowels(input_string)
print("Number of vowels:", result)
