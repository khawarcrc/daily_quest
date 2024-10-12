# Problem Statement:
# Given an array of integers, find the majority element. The majority element is defined as the element
# that appears more than n // 2 times in the array, where n is the size of the array. 
# You are tasked to find this majority element using bit manipulation.

# Steps to Solve the Problem:
# 1. Understand the bit representation: Each integer is represented by a 32-bit binary number. 
# The idea is to determine, bit by bit, which value occurs in more than half of the elements for each bit position.

# 2. Iterate over all 32 bit positions: For each bit position (from 0 to 31), 
# we will count how many numbers in the array have that particular bit set to 1.

# 3. Count the ones for each bit position: For each bit, count how many numbers 
# in the array have a 1 in the current bit position.

# 4. Rebuild the majority element: If more than half of the numbers have a 1 in the current bit position, 
# this bit must be part of the majority element. Set that bit in the answer variable.

# 5. Return the final result: Once all bit positions are evaluated, 
# the answer variable will hold the majority element, reconstructed bit by bit.

# Theory of Problem and Solution:
# This problem uses bit manipulation to solve the majority element problem.
# The main idea is to count how often each bit is set to 1 across all the numbers in the array. 
# Since the majority element appears more than n // 2 times, its binary representation will also dominate the bit positions.
# By checking each bit position separately, we can reconstruct the majority element's binary form and return it.

# This approach avoids directly counting occurrences of each number, 
# making it an efficient solution, particularly for large datasets.



def majorityElement(array): 
    # Initialize answer to 0, which will store the majority element bit by bit
    answer = 0
    
    # Iterate through all 32 bit positions (assuming 32-bit integers)
    for currentBit in range(32): 
        # Create a mask with a 1 in the current bit position using bit shifting
        currentBitValue = 1 << currentBit
        
        # Count how many numbers have this bit set to 1
        onesCount = 0 
        
        # Loop through each number in the array
        for num in array: 
            # Check if the current bit in num is set (i.e., equal to 1)
            if (num & currentBitValue) != 0: 
                # Increment count if the bit is 1
                onesCount += 1 
        
        # If more than half of the numbers have a 1 in this bit position
        if onesCount > len(array) / 2:
            # Add this bit to the answer (set it in the majority element)
            answer += currentBitValue
    
    # Return the final answer, which is the majority element
    return answer

# Dummy data to test the function
# Test case 1: Majority element is 3 (binary 11), appears more than half the time
array1 = [3, 3, 4, 2, 3]
print(majorityElement(array1))  # Output: 3

# Test case 2: Majority element is 5 (binary 101), appears more than half the time
array2 = [5, 5, 5, 6, 5, 6]
print(majorityElement(array2))  # Output: 5

# Test case 3: Majority element is 2 (binary 10), appears more than half the time
array3 = [2, 2, 1, 1, 2, 2, 1, 2, 2]
print(majorityElement(array3))  # Output: 2




# def majorityElement(array): 
#     answer = 0
    
#     for currentBit in range(32): 
#         currentBitValue = 1 << currentBit
#         print(f"Checking bit position: {currentBit}, currentBitValue: {bin(currentBitValue)}")  # Print current bit position and value
        
#         onesCount = 0 
        
#         for num in array: 
#             if (num & currentBitValue) != 0: 
#                 onesCount += 1
        
#         print(f"Count of ones at bit position {currentBit}: {onesCount}")  # Print count of ones for current bit
        
#         if onesCount > len(array) / 2:
#             answer += currentBitValue
#             print(f"Setting bit {currentBit} in answer, new answer: {bin(answer)}")  # Print updated answer after setting the bit
    
#     print(f"Final majority element in binary: {bin(answer)}")  # Print final majority element in binary
#     return answer

# # Dummy data to test the function
# array1 = [3, 3, 4, 2, 3]
# print("Majority Element:", majorityElement(array1))  # Output: 3

# array2 = [5, 5, 5, 6, 5, 6]
# print("Majority Element:", majorityElement(array2))  # Output: 5

# array3 = [2, 2, 1, 1, 2, 2, 1, 2, 2]
# print("Majority Element:", majorityElement(array3))  # Output: 2
