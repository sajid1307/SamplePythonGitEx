def fib(limit):
    a, b = 0, 1 # Initialize first two Fibonacci Numbers 
    while a < limit: # One by one yield next Fibonacci Number
        yield a
        a, b = b, a + b
x = fib(5) # Create a generator object
print(x)  # Returns iterator onject

for i in x:
    print(i)
