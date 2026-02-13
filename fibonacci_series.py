def fibonacci_series(n): # define function that takes max value
    a, b = 0, 1 # initialize first two Fibonacci numbers
    series = [] # create empty list to store results
    while a <= n: # continue while current number <= n
        series.append(a) # add current number to list
        a, b = b, a + b # update: a becomes b, b becomes a+b (next Fibonacci)
    return series # return the complete list

# Test the function
n = 100 
fib_series = fibonacci_series(n)
print(fib_series)   