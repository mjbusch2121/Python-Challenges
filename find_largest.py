def find_largest(numbers):
    # Start by assuming the first number is the largest
    largest = numbers[0]

    # Loop through each number in the list
    for num in numbers:
        # If current number is bigger than our current largest
        if num > largest:
            # Update largest to this new number
            largest = num

    # Return the largest number we found
    return largest

# Test the function with a list of numbers
# Expected output: 15 (largest number in the list)
print(find_largest([10, 5, 8, 15, 3]))