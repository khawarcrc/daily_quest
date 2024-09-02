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



# 1. Sort the coins in ascending order.
# 2. Initialize a variable to track the maximum change that can be created so far.
# 3. Iterate through the coins:
#    - If a coin is larger than the next possible change value (currentChange + 1),
#      identify and return the smallest amount of change that cannot be created.
#    - Otherwise, add the coin to the current change value.
# 4. If no gaps are found, return the next consecutive change value that cannot be created.
