def getNthFib(n):
    # Initialize the first two numbers in the Fibonacci sequence
    lastTwo = [1, 3]  # We start with 1 and 3 instead of the traditional 0 and 1
    
    # Initialize a counter starting from 3, as we already know the first two numbers
    counter = 3
    
    # Loop to calculate the Fibonacci sequence until we reach the nth number
    while counter <= n:
        # Calculate the next Fibonacci number as the sum of the previous two
        nextFib = lastTwo[0] + lastTwo[1]
        
        
        lastTwo[0] = lastTwo[1]   # The first number in lastTwo is updated to the second number.
        lastTwo[1] = nextFib      # The second number in lastTwo is updated to the new Fibonacci  
        
        # Increment the counter to move to the next Fibonacci number
        counter += 1
    
    # If n is greater than 1, return the second number in lastTwo
    # Otherwise, return the first number (which would be the nth Fibonacci number)
    return lastTwo[1] if n > 1 else lastTwo[0]

# Dummy data for testing
n = 5  # We want to find the 5th Fibonacci number in this custom sequence

# Calling the function with n = 5
result = getNthFib(n)

# Output the result
print(f"The {n}th Fibonacci number is: {result}")
