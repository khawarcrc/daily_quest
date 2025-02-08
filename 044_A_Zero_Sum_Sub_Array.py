# Problem Statement:
# Given an array of integers, the task is to determine whether there exists a 
# subarray (continuous segment of the array) that sums to zero. 
# A subarray is defined as a contiguous part of the array.

# Steps to Solve the Problem:

# 1. Initialize a set called `sums` to keep track of the cumulative sums encountered so far.
#    - Start with the sum of 0 in the set, as a sum of zero can occur if 
#      the cumulative sum matches a previously seen sum.

# 2. Initialize a variable `currentSum` to keep track of the cumulative sum of the elements
#    as we iterate through the array.

# 3. Loop through each number in the input array `nums`:
#    - For each number, update `currentSum` by adding the current number to it.

# 4. Check if the `currentSum` is already present in the `sums` set:
#    - If it is found, return True immediately, as this indicates that there exists a 
#      subarray which sums to zero (the subarray between the previous occurrence of this sum 
#      and the current index).

# 5. If `currentSum` is not in `sums`, add `currentSum` to the `sums` set for future reference.

# 6. If the loop completes without finding any zero-sum subarray, return False.


def zeroSumSubarray(nums):
    # Initialize a set to keep track of the cumulative sums encountered so far, starting with 0
    sums = set([0])
    # Initialize the current cumulative sum
    currentSum = 0
    
    # Iterate through each number in the input list
    for num in nums:
        # Update the current cumulative sum by adding the current number
        currentSum += num
        
        # Check if the current cumulative sum has been seen before
        if currentSum in sums:
            # If yes, a subarray with a sum of zero exists
            return True
        
        # Add the current cumulative sum to the set for future reference
        sums.add(currentSum)
    
    # If no zero-sum subarray is found, return False
    return False


# Dummy data for testing
test_nums = [4, 2, -2, 3, 1]  # This array contains a zero-sum subarray [2, -2]
print(zeroSumSubarray(test_nums))  # Output: True
