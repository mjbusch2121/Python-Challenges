def sort_by_length(strings):
    # sorted() sorts the list
    # key=len tells it to sort by LENGTH instead of alphabetically
    # len is a function that returns the length of each string
    return sorted(strings, key=len)

# Test the function
# "date"=4, "apple"=5, "banana"=6, "blueberry"=9
# Expected output: ['date', 'apple', 'banana', 'blueberry']
print(sort_by_length(["apple", "banana", "blueberry", "date"]))