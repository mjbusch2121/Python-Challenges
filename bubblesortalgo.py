# bubble sort algorithm
# repeatedly compares adjacent elements and swaps them if they're in wrong order
# each full pass "bubbles" the largest unsorted value to the end

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range (0, n- i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# test 
numbers = [64,34,25,12,22,11,90]
print("Before:", numbers)
print("After: ", bubble_sort(numbers))