def find_second_smallest(numbers):
    # Step 1: set() removes duplicates → {5, 10, 3, 8, 1}
    # Step 2: sorted() sorts them → [1, 3, 5, 8, 10]
    sorted_nums = sorted(set(numbers))

    # Return the second item (index 1)
    # Index 0 = smallest (1), Index 1 = second smallest (3)
    return sorted_nums[1]

# Test the function
# Input: [5, 10, 3, 8, 1]
# After sorting: [1, 3, 5, 8, 10]
# Expected output: 3 (second smallest)
print(find_second_smallest([5, 10, 3, 8, 1]))