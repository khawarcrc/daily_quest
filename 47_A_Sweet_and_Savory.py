
# Problem Statement:
# You are given a list of integers representing the flavor intensity of various dishes.
# Negative values represent sweet dishes, and positive values represent savory dishes.
# Your task is to find one sweet dish and one savory dish whose combined flavor intensity
# is as close as possible to a given target value without exceeding it. 
# You must return the pair of dishes (one sweet and one savory) that satisfies this condition.

# Steps to Solve the Problem:

# 1. Separate the sweet dishes (negative integers) from the savory dishes (positive integers).
#    - Use a list comprehension to create a list of sweet dishes (negative values) and savory dishes (positive values).
# 2. Sort the sweet dishes by their absolute values, as we want to process the least negative (closest to 0) sweet dishes first.
#    - Sort the savory dishes in ascending order to efficiently process lower savory values first.
# 3. Initialize two variables to store:
#    - The best pair of sweet and savory dishes found so far.
#    - The smallest difference between the sum of a pair and the target value.
# 4. Use the two-pointer technique:
#    - Start with two pointers, one pointing to the first sweet dish and one pointing to the first savory dish.
#    - Calculate the sum of the current sweet and savory dish.
# 5. If the sum is less than or equal to the target:
#    - Calculate the difference between the target and the sum.
#    - If this difference is smaller than the smallest difference found so far:
#      - Update the best pair and store the current sweet and savory dish as the best option.
#    - Move the savory dish pointer forward to check the next savory dish (try increasing the sum).
# 6. If the sum exceeds the target:
#    - Move the sweet dish pointer forward (try reducing the sum by choosing a less negative sweet dish).
# 7. Continue iterating until all pairs of sweet and savory dishes have been checked, or the closest possible sum is found.
# 8. Return the best pair of dishes whose sum is as close as possible to the target without exceeding it.

# Complete Theory of Code:

# 1. **Sweet and Savory Separation**:
#    - Dishes with negative values are treated as sweet dishes, while dishes with positive values are savory.
#    - The reason for separating and sorting them is to efficiently navigate the list when searching for pairs.

# 2. **Sorting the Sweet and Savory Dishes**:
#    - Sweet dishes are sorted by their absolute values (i.e., the least negative ones first).
#    - Sorting allows us to handle the least extreme values early on, which are more likely to give sums close to the target.

# 3. **Two-Pointer Approach**:
#    - The two-pointer technique is ideal for this problem because it lets us minimize the difference by strategically moving
#      either the sweet or savory pointer based on the current sum relative to the target.
#    - One pointer starts at the beginning of the sweet dishes, and the other pointer starts at the beginning of the savory dishes.
#    - We adjust the pointers based on whether the sum of the current pair exceeds or is less than the target value.
#    - This approach ensures that we find the closest possible sum without needing to try every combination (which would be inefficient).

# 4. **Best Pair and Best Difference**:
#    - We track the best pair of dishes found so far by storing both the dish pair and the difference between their sum and the target.
#    - As we explore new pairs, we update the best pair only if we find a sum that is closer to the target.

# 5. **Edge Case Handling**:
#    - If there are no valid sweet or savory dishes (i.e., no negative or positive values), the algorithm ensures no pair is returned.
#    - If no sum is less than or equal to the target, the algorithm will return the best possible pair it can find.

# 6. **Time Complexity**:
#    - Sorting the dishes takes O(n log n) time, where `n` is the total number of dishes.
#    - The two-pointer loop iterates through both lists in O(n) time.
#    - The overall time complexity of this solution is O(n log n), which ensures efficient processing for large lists of dishes.

# 7. **Final Output**:
#    - The function returns the best pair of one sweet and one savory dish that, when combined, gets as close as possible to
#      the target value without exceeding it. If multiple pairs have the same sum, the function returns the first one found.



def sweetAndSavory(dishes, target):
    # Separate sweet dishes (negative values) and savory dishes (positive values)
    sweetDishes = sorted([dish for dish in dishes if dish < 0], key=abs)  # Sort by absolute values for efficiency
    savoryDishes = sorted([dish for dish in dishes if dish > 0])  # Sort naturally in ascending order

    # Initialize best pair and smallest difference
    bestPair = [0, 0]
    bestDifference = float("inf")  # Infinite as initial comparison value
    sweetIndex, savoryIndex = 0, 0  # Two pointers for sweet and savory dishes

    # Use a two-pointer technique to find the closest sum <= target
    while sweetIndex < len(sweetDishes) and savoryIndex < len(savoryDishes):
        currentSum = sweetDishes[sweetIndex] + savoryDishes[savoryIndex]  # Sum of the current sweet and savory dish

        # Check if the current sum is less than or equal to the target
        if currentSum <= target:
            currentDifference = target - currentSum  # Calculate how close the sum is to the target

            # If the difference is smaller than the best difference found so far, update best pair
            if currentDifference < bestDifference:
                bestDifference = currentDifference  # Update the best difference
                bestPair = [sweetDishes[sweetIndex], savoryDishes[savoryIndex]]  # Update the best pair

            # Move the savory pointer to explore the next dish (since currentSum <= target)
            savoryIndex += 1
        else:
            # If the current sum exceeds the target, move the sweet pointer to reduce the sum
            sweetIndex += 1

    return bestPair

# Dummy data example
dishes = [-10, -5, -3, 2, 4, 8]
target = 5

print(sweetAndSavory(dishes, target))  # Expected output: [-5, 8] or any valid pair where the sum is <= 5
