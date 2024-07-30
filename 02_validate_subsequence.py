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
print(validateSubsequence(array, sequence))  # Should return True
