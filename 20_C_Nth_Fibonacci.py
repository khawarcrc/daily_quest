def getNthFib(n, memoize={1: 0, 2: 1}):
    # Check if the Fibonacci number for 'n' is already in the memoization dictionary
    if n in memoize:
        return memoize[n]  # Return the precomputed Fibonacci number
    
    # If not, compute it recursively and store it in the memoize dictionary
    else:
        # Recursively compute the (n-1)th and (n-2)th Fibonacci numbers
        memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize)
        return memoize[n]  # Return the computed Fibonacci number

# Dummy data for testing
n = 6  # We want to find the 6th Fibonacci number

# Calling the function with n = 6
result = getNthFib(n)

# Output the result
print(f"The {n}th Fibonacci number is: {result}")
