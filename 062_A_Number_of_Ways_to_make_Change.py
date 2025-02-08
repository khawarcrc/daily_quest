
# Problem Statement:
# Given an amount n and a list of denominations, 
# determine the number of ways to make change for that amount using the given denominations.
# You can use any denomination multiple times.

# Problem Explanation:
# The goal of the problem is to find out how many different combinations of coins (or denominations)
# can sum up to a given target amount n. You can use any denomination multiple times.

# Key Points:
# Denominations: The different coin values you have available.
# Target Amount (n): The amount you want to make change for.
# Combinations: Different ways to combine the denominations to reach the target amount

# Code Execution Theory:
# 1. Initialize a list 'ways' of size (n + 1) to hold the number of ways to make change 
#    for amounts from 0 to n, starting with 'ways[0]' set to 1 (base case).
# 2. Iterate through each denomination in 'denoms':
#    - For each denomination, iterate through all amounts from 1 to n.
#    - If the current denomination is less than or equal to the current amount,
#      update 'ways[amount]' by adding 'ways[amount - denom]'.
# 3. By the end of the iterations, 'ways[n]' will contain the total number of ways 
#    to make change for the amount n using the available denominations


def numberOfWaysToMakeChange(n, denoms):
    # Create a list to store the number of ways to make change for each amount
    ways = [0 for amount in range(n + 1)]
    ways[0] = 1  # There is one way to make change for zero amount: use no coins

    # Iterate through each denomination
    for denom in denoms: 
        # For each amount from 1 to n
        for amount in range(1, n + 1): 
            # If the denomination is less than or equal to the current amount
            if denom <= amount: 
                # Update the ways to make change for the current amount
                ways[amount] += ways[amount - denom]
    
    return ways[n]  # Return the number of ways to make change for amount n

# Dummy data
n = 5  # Amount for which we need to make change
denoms = [1, 2, 5]  # Denominations available

# Function execution with dummy data
result = numberOfWaysToMakeChange(n, denoms)
print(f"Number of ways to make change for {n} using denominations {denoms}: {result}")


