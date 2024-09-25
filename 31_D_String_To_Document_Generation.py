# Problem Statement:
# Given two strings, 'availableSupplies' and 'order', determine whether you can fulfill 
# the 'order' using only the items from the 'availableSupplies' string.
# Each item in 'availableSupplies' can only be used as many times as it appears in that string.
# The goal is to return True if the order can be fulfilled, otherwise return False.

# Steps to Solve the Problem:
# 1. Create an empty dictionary to count occurrences of each supply item in 'availableSupplies'.
# 2. Loop through each supply item in 'availableSupplies':
#    a. If the supply item is not already in the dictionary, initialize its count to 0.
#    b. Increment the count of this supply item by 1.
# 3. Loop through each supply item in 'order':
#    a. If the supply item doesn't exist in the dictionary or its count is zero, 
#       return False because the order cannot be fulfilled.
#    b. Decrease the count of the supply item by 1 to account for its use in fulfilling the order.
# 4. If all items in the order can be fulfilled, return True.


# Function definition
def fulfillOrder(availableSupplies, order): 
    # Create an empty dictionary to count occurrences of each supply item in 'availableSupplies'
    supplyCount = {} 
    
    # Count how many times each supply item appears in 'availableSupplies'
    for supplyItem in availableSupplies: 
        # If the supply item is not already in the dictionary, initialize its count to 0
        if supplyItem not in supplyCount: 
            supplyCount[supplyItem] = 0
        
        # Increase the count of this supply item by 1
        supplyCount[supplyItem] += 1
        
    # Check if we have enough supplies to fulfill the 'order'
    for supplyItem in order: 
        # If the supply item doesn't exist or has been used up, return False (cannot fulfill the order)
        if supplyItem not in supplyCount or supplyCount[supplyItem] == 0: 
            return False 
        
        # Use one of the supply items to fulfill part of the order
        supplyCount[supplyItem] -= 1
    
    # If the entire order can be fulfilled, return True
    return True

# Dummy data for testing
availableSupplies = "aabbccdd"  # Supplies available
order = "abc"                   # Order to fulfill

# Test the function with dummy data
result = fulfillOrder(availableSupplies, order)
print(result)  # Expected output: True, because the order "abc" can be fulfilled using "aabbccdd"
