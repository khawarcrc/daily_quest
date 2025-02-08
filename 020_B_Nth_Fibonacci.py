def getNthFib(n):
    # Base case: if n is 2, return 1 (the second Fibonacci number)
    if n == 2:
        return 1
    # Base case: if n is 1, return 0 (the first Fibonacci number)
    elif n == 1:
        return 0
    # Recursive case: sum of the previous two Fibonacci numbers
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)

# Dummy data for testing
n = 5  # We want to find the 5th Fibonacci number

# Calling the function with n = 5
result = getNthFib(n)

# Output the result
print(f"The {n}th Fibonacci number is: {result}")
