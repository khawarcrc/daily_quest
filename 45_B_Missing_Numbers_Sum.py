# Problem Statement:
# Given a list of numbers from a sequence where exactly two numbers are missing, write a function to find and return
# those two missing numbers. The input list `nums` contains numbers from a range starting at 1, but two numbers 
# from this range are missing. The task is to efficiently identify and return these two missing numbers.

# Steps to solve the problem:
# 1. Calculate the total sum of all numbers in the full sequence (from 1 to the maximum expected number, which is
#    len(nums) + 2). This includes the two missing numbers.
# 2. Subtract the sum of the numbers present in `nums` from this total. The result will be the sum of the two
#    missing numbers.
# 3. Divide this total sum of the two missing numbers by 2 to calculate the "average" of the two missing numbers.
#    This value helps split the problem into two parts: one missing number will be smaller than or equal to the
#    average, and the other will be larger.
# 4. Iterate through the input list `nums`, splitting the numbers into two groups:
#    - Numbers less than or equal to the average are added to the first group.
#    - Numbers greater than the average are added to the second group.
# 5. Calculate the expected sum of the numbers in the first group (numbers from 1 to the average value).
# 6. Calculate the expected sum of the numbers in the second group (numbers from the average value + 1 to the 
#    maximum expected number).
# 7. Subtract the actual sum of numbers in both groups (as determined from `nums`) from the expected sums for
#    each group. This will give the two missing numbers: one from each group.
# 8. Return these two missing numbers.

# Theory to solve the problem:
# - The key idea is based on the mathematical property of summation. The sum of a sequence of consecutive numbers 
#   (1 to N) can be calculated, and the difference between this expected sum and the sum of the numbers in the input
#   list reveals information about the missing values.
# - By splitting the problem into two parts, the code uses an efficient strategy to avoid directly searching for 
#   missing numbers. Instead, it leverages arithmetic properties to calculate the missing numbers through subtraction.
# - This approach ensures that the solution runs in linear time (O(n)) since we only need to loop through the list 
#   once and perform constant-time arithmetic operations.



def missingNumbers(nums):
    # Step 1: Calculate the total sum of numbers from 1 to len(nums) + 2
    # len(nums) + 2 because we are missing two numbers
    total = sum(range(1, len(nums) + 3))

    # Step 2: Subtract the actual numbers in the list nums from the total sum
    for num in nums:
        total -= num

    # Step 3: Divide the remaining total (which is the sum of two missing numbers) by 2
    # This will be used to split the problem into two parts
    averageMissingValue = total // 2

    # Step 4: Initialize variables to store sums of numbers in two halves
    foundFirstHalf = 0
    foundSecondHalf = 0

    # Step 5: Iterate through the list and divide the numbers into two groups:
    # Numbers less than or equal to the averageMissingValue go to foundFirstHalf
    # Numbers greater than averageMissingValue go to foundSecondHalf
    for num in nums:
        if num <= averageMissingValue:
            foundFirstHalf += num
        else:
            foundSecondHalf += num

    # Step 6: Calculate the expected sum for the first half (from 1 to averageMissingValue)
    expectedFirstHalf = sum(range(1, averageMissingValue + 1))

    # Step 7: Calculate the expected sum for the second half (from averageMissingValue + 1
    # to the maximum expected number len(nums) + 2)
    expectedSecondHalf = sum(range(averageMissingValue + 1, len(nums) + 3))

    # Step 8: Return the difference between expected and found sums for each half, 
    # which gives the two missing numbers
    return [expectedFirstHalf - foundFirstHalf, expectedSecondHalf - foundSecondHalf]


# Dummy data to test the function
nums = [1, 2, 4, 6]  # Missing numbers are 3 and 5
print(missingNumbers(nums))  # Output: [3, 5]

nums = [1, 3, 4, 5]  # Missing numbers are 2 and 6
print(missingNumbers(nums))  # Output: [2, 6]
