# Problem Statement:
# Given a list of positive integers representing the values of coins you have, 
# determine the minimum amount of change (sum of coin values) that you cannot create.
# The goal is to find the smallest amount of money that cannot be obtained using any combination of the coins.

# Steps to Solve:
# 1. **Sort the coins**: Begin by sorting the list of coins in ascending order.
#    This allows us to process the coins incrementally, ensuring that smaller coins are used first.
#
# 2. **Initialize the current change created**: 
#    Start with a variable `currentChangeCreated` set to 0. This variable will track the largest sum of 
#    coin values (or change) that can be created up to that point.
#
# 3. **Iterate through each coin in the sorted list**: 
#    For each coin in the list:
#    - **Check if the coin is too large**: 
#      If the current coin value is greater than `currentChangeCreated + 1`, it means that we can't 
#      create the next consecutive amount of change (since adding this coin would skip the next change value).
#      In that case, return `currentChangeCreated + 1` as the smallest non-constructible change.
#    - **Update the current change created**: 
#      Otherwise, add the value of the current coin to `currentChangeCreated`, as this coin can be used to 
#      extend the range of change values we can create.
#
# 4. **Return the final result**: 
#    If all coins are processed and no gap in the change range is found, return `currentChangeCreated + 1`
#    as the smallest non-constructible change.

def nonConstructibleChange(coins):
    # Sort the coins array to process them in ascending order
    coins.sort()
    
    # Initialize a variable to track the current change that can be created
    currentChangeCreated = 0
    
    # Iterate through each coin in the sorted list
    for coin in coins:
        # If the current coin is greater than the current change + 1, 
        # we can't create the next change value, so return it.
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        
        # Otherwise, add the current coin to the current change value
        currentChangeCreated += coin
        
        # Debugging: Print the current state
        print(f"Coin: {coin}, Current Change Created: {currentChangeCreated}")
    
    # If all coins have been used, return the next change that can't be created
    return currentChangeCreated + 1

# Demo example
coins = [1, 1, 3, 4, 9]
print("Coins:", coins)
result = nonConstructibleChange(coins)
print(f"Minimum change that cannot be created: {result}")




