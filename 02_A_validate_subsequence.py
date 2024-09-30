# Problem Statement:
# Given two arrays, array and sequence, write a function that checks if the sequence is a subsequence of the array.
# A subsequence means that all elements of sequence appear in the array in the same order, but not necessarily consecutively.
# The function should return True if sequence is a subsequence of array, otherwise it should return False.

# Steps to Solve:
# 1. Initialize two indices, one for tracking the current position in the array and another for tracking the position in the sequence.
# 2. Loop through both the array and sequence as long as neither index has reached the end.
# 3. For each element in the array, compare it to the current element in the sequence:
#    a. If the elements match, move to the next element in the sequence.
#    b. Regardless of whether there's a match, move to the next element in the array.
# 4. After the loop ends, check if the sequence index has reached the end of the sequence:
#    a. If it has, it means the entire sequence was found in the array in the correct order, so return True.
#    b. If it hasn't, return False since not all elements of the sequence were found.

def validateSubsequence(array, sequence):
    # Initialize two indices to keep track of positions in array and sequence
    arrIdx = 0
    seqIdx = 0
    
    # Loop through the array and sequence until the end of either is reached
    while arrIdx < len(array) and seqIdx < len(sequence):
        # If the current element in the array matches the current element in the sequence
        if array[arrIdx] == sequence[seqIdx]:
            # Move to the next element in the sequence
            seqIdx += 1
        
        # Move to the next element in the array
        arrIdx += 1

    # Return True if the entire sequence has been found in the array in order, otherwise False
    return seqIdx == len(sequence)

# Sample test case
array = [5, 1, 22, 25, 6, 7, 8, 10]
sequence = [1, 6, 8, 10]

# Validate subsequence
print("Result:", validateSubsequence(array, sequence))  # Should return True



# def validateSubsequence(array, sequence):
#     # Initialize two indices to keep track of positions in array and sequence
#     arrIdx = 0
#     seqIdx = 0

#     print("Starting validation of subsequence...")
#     print(f"Array: {array}")
#     print(f"Sequence: {sequence}")
    
#     # Loop through the array and sequence until the end of either is reached
#     while arrIdx < len(array) and seqIdx < len(sequence):
#         print(f"Checking array[{arrIdx}] = {array[arrIdx]} against sequence[{seqIdx}] = {sequence[seqIdx]}")
        
#         # If the current element in the array matches the current element in the sequence
#         if array[arrIdx] == sequence[seqIdx]:
#             print(f"Match found: {array[arrIdx]}")
#             # Move to the next element in the sequence
#             seqIdx += 1
#             print(f"Moving to the next element in sequence: new seqIdx = {seqIdx}")
        
#         # Move to the next element in the array
#         arrIdx += 1
#         print(f"Moving to the next element in array: new arrIdx = {arrIdx}")

#     # Final result after loop ends
#     result = seqIdx == len(sequence)
#     print(f"Entire sequence found in array: {result}")
    
#     # Return True if the entire sequence has been found in the array in order, otherwise False
#     return result

# # Sample test case
# array = [5, 1, 22, 25, 6, 7, 8, 10]
# sequence = [1, 6, 8, 10]

# # Validate subsequence
# print("Result:", validateSubsequence(array, sequence))  # Should return True
