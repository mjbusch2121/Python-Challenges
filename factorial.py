def factorial(n):
    if n == 0: # base case: stop condition
        return 1 # 0! = 1 (definition)
    else:
        return n * factorial(n-1)

# Test the function
print(factorial(5))  # Output should be 120