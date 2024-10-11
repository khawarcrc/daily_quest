# Problem Statement:
# Given a list of numbers, identify all the missing numbers in the sequence starting from 1 up to the maximum number 
# present in the input list. The goal is to return a list of all numbers that are missing within this range.


# Theory to Solve the Problem:
# 
# The problem of identifying missing numbers in a sequence can be efficiently solved by leveraging set data 
# structures for fast membership checks and iterating through a defined range of numbers.
#
# 1. **Set for Fast Lookup:**
#    - Converting the input list to a set allows for O(1) average-time complexity for membership checks, making 
#      it easier to determine if a number is present in the list.
# 
# 2. **Determining the Maximum Number:**
#    - Using the `max()` function helps establish an upper limit for our search, ensuring we cover all possible 
#      missing numbers.
# 
# 3. **Iterating through the Range:**
#    - By looping through all integers from 1 to the maximum number, we can systematically check for the presence 
#      of each number and collect those that are missing.
# 
# 4. **Building the Solution List:**
#    - The solution list accumulates all missing numbers, allowing us to provide a complete set of results.
#




def missingNumbers(nums):
    # Convert the input list nums to a set for faster lookup
    includedNums = set(nums)

    # Initialize an empty list to store missing numbers
    solution = []

    # Use the maximum number in nums or len(nums) + 2 (whichever is larger) as the upper bound
    max_num = max(nums)  # Get the maximum number from the input list
    print(f"max number: {max_num}")

    # Iterate through numbers from 1 to the maximum number in the list
    for num in range(1, max_num):
        # If the current number is not in the set of included numbers
        if num not in includedNums:
            # Add it to the solution list as it's a missing number
            solution.append(num)
    
    # Return the list of missing numbers
    return solution

# Dummy data to test the function
nums = [1, 2, 4, 20]
print(missingNumbers(nums))  # Output should be [3, 5, 6, 7, 8, 9]




# another scenario

# def missingNumbers(nums):
#     # Convert the input list nums to a set for faster lookup
#     includedNums = set(nums)

#     # Initialize an empty list to store missing numbers
#     solution = []
    
#     # Iterate through numbers from 1 to len(nums) + 2 (inclusive)
#     # len(nums) + 3 to account for checking two extra missing numbers
#     for num in range(1, len(nums) + 3):
#         # If the current number is not in the set of included numbers
#         if not num in includedNums:
#             # Add it to the solution list as it's a missing number
#             solution.append(num)
    
#     # Return the list of missing numbers
#     return solution

# # Dummy data to test the function
# nums = [1, 2, 4, 6]
# print(missingNumbers(nums))  # Output should be [3, 5]
