# Problem: Largest Range
# ------------------------------------------
# You are given an unsorted array of integers.
# Your task is to find the largest range of consecutive integers present in the array.
#
# Return the result as an array of two elements:
# [start_of_range, end_of_range]
#
# Example:
# Input:  [4, 2, 1, 3, 6, 5, 10]
# Output: [1, 6]
#
# Because numbers 1 → 6 exist in the array (continuous sequence).
#
# Constraints:
# - Numbers are NOT sorted
# - There is always exactly ONE largest range


# Imagine:
# You are analyzing user login days from server logs.
#
# Example:
# logs = [1, 3, 2, 6, 7, 8, 100]
#
# You want to find:
# The longest streak of consecutive login days.
#
# Output: [6, 8]
# (User logged in 3 consecutive days)
#
# This helps in:
# - Detecting user engagement
# - Rewarding streak-based behavior (like Duolingo, Snapchat)

# Key Idea:
# ------------------------------------------
# We need to find the longest sequence of consecutive numbers.
#
# Example:
# [1, 2, 3, 4, 100, 200]
#
# Consecutive sequences:
# - 1 → 4  (length = 4)
# - 100    (length = 1)
# - 200    (length = 1)
#
# Answer = [1, 4]
#
# Important Observations:
# - Sorting is possible but costs O(n log n)
# - We want O(n) solution → use HashSet
#
# Why HashSet?
# - O(1) lookup
# - Helps check if number exists instantly


# Approach:
# ------------------------------------------
# 1. Store all numbers in a HashSet for fast lookup
#
# 2. Iterate through each number
#
# 3. For each number:
#    - Check if it is the START of a range
#    - A number is start IF (num - 1) NOT in set
#
# 4. If it's a start:
#    - Expand forward (num + 1, num + 2...)
#    - Count length of range
#
# 5. Track the longest range found
#
# 6. Return [start, end]
#
# Example Walkthrough:
# ------------------------------------------
# Input: [4, 2, 1, 3, 6, 5]
#
# HashSet = {1,2,3,4,5,6}
#
# Start candidates:
# - 1 (since 0 not in set)
#
# Expand:
# 1 → 2 → 3 → 4 → 5 → 6
#
# Range = [1, 6]
#
# Time Complexity:
# ------------------------------------------
# O(n) → each number visited once
#
# Space Complexity:
# ------------------------------------------
# O(n) → HashSet storage


def largest_range(array):
    """
    # Problem:
    # Find the largest range of consecutive integers in an unsorted array.
    
    # Steps:
    # 1. Store all numbers in a set for O(1) lookup
    # 2. Iterate through each number
    # 3. Check if it is start of range (num - 1 not in set)
    # 4. Expand forward and calculate range length
    # 5. Track maximum range
    """

    nums = set(array)  # O(n) space
    longest_length = 0
    best_range = []

    print("Input Array:", array)
    print("Converted Set:", nums)

    for num in array:
        # Check if it's start of a sequence
        if num - 1 not in nums:
            print(f"\nStart of new range found at: {num}")

            current = num
            length = 1

            # Expand forward
            while current + 1 in nums:
                current += 1
                length += 1

            print(f"Range found: [{num}, {current}] with length {length}")

            # Update best range
            if length > longest_length:
                longest_length = length
                best_range = [num, current]
                print(f"Updated Best Range: {best_range}")

    return best_range



# Test Case 1
arr1 = [4, 2, 1, 3, 6, 5, 10]
print("\nFinal Result:", largest_range(arr1))


# Test Case 2
arr2 = [100, 4, 200, 1, 3, 2]
print("\nFinal Result:", largest_range(arr2))


# Test Case 3 (real-world style: login streaks)
arr3 = [10, 11, 15, 12, 13, 50]
print("\nFinal Result:", largest_range(arr3))