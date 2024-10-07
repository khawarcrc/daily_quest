# Problem Statement:
# A store wants to calculate the total value of its inventory 
# without including the value of the current product being evaluated. 
# Each product's price is represented in an array. 
# The goal is to determine how much value is contributed by all 
# other products to assist in decision-making, such as discounts or promotions.

# Steps to Solve the Problem:
# 1. Initialize an array 'totalValue' of the same length as 'prices', 
#    filled with initial values (e.g., 1 or 0).
#
# 2. Initialize a variable 'leftRunningTotal' to hold the cumulative 
#    value of all products to the left of the current index. Set it to 0.
#
# 3. Loop through the 'prices' array from left to right:
#    - For each index 'i', set 'totalValue[i]' to 'leftRunningTotal', 
#      which represents the total value of all products to the left of 'i'.
#    - Update 'leftRunningTotal' by adding the current product's price.
#
# 4. Initialize a variable 'rightRunningTotal' to hold the cumulative 
#    value of all products to the right of the current index. Set it to 0.
#
# 5. Loop through the 'prices' array from right to left:
#    - For each index 'i', add 'rightRunningTotal' to 'totalValue[i]', 
#      which now represents the total value excluding the current product's price.
#    - Update 'rightRunningTotal' by adding the current product's price.
#
# 6. Return the 'totalValue' array containing the total value of inventory 
#    excluding the current product prices.



def inventoryValueExcludingCurrent(prices):
    # Initialize an array 'totalValue' of the same length as 'prices', filled with 1s
    totalValue = [1 for _ in range(len(prices))]

    # Initialize leftRunningTotal to hold the cumulative value of all products to the left
    leftRunningTotal = 1

    # First loop: Go through each price from left to right
    for i in range(len(prices)):
        # Set the current 'totalValue[i]' to leftRunningTotal (total value of products to the left of i)
        totalValue[i] = leftRunningTotal

        # Update leftRunningTotal by adding the current price in 'prices'
        leftRunningTotal += prices[i]

    # Initialize rightRunningTotal to hold the cumulative value of all products to the right
    rightRunningTotal = 0

    # Second loop: Go through each price from right to left (reversed order)
    for i in reversed(range(len(prices))):
        # Add the rightRunningTotal to totalValue[i] (total value of products to the right of i)
        totalValue[i] += rightRunningTotal

        # Update rightRunningTotal by adding the current price in 'prices'
        rightRunningTotal += prices[i]

    # Return the final 'totalValue' array containing the result
    return totalValue


# Dummy data to test the function
prices = [10, 20, 30, 40]

# Call the function and print the final result
result = inventoryValueExcludingCurrent(prices)
print(f"\nTotal value of inventory excluding current product prices: {result}")
