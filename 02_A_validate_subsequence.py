# Initialize two pointers: 'arrIdx' for the main array and 'seqIdx' for the sequence to track current positions.
# Iterate through both the main array and sequence until either pointer reaches the end.
# If the current element of the array matches the current element of the sequence, move the sequence pointer ('seqIdx') to the next element.
# Always move the array pointer ('arrIdx') to the next element regardless of a match.
# After the loop, check if the sequence pointer ('seqIdx') has reached the end of the sequence.
# If 'seqIdx' equals the length of the sequence, the sequence is valid; otherwise, it is not.

def validateSubsequence(array, sequence):
    # Initialize two indices to keep track of positions in array and sequence
    arrIdx = 0
    seqIdx = 0

    print("Starting validation of subsequence...")
    print(f"Array: {array}")
    print(f"Sequence: {sequence}")
    
    # Loop through the array and sequence until the end of either is reached
    while arrIdx < len(array) and seqIdx < len(sequence):
        print(f"Checking array[{arrIdx}] = {array[arrIdx]} against sequence[{seqIdx}] = {sequence[seqIdx]}")
        
        # If the current element in the array matches the current element in the sequence
        if array[arrIdx] == sequence[seqIdx]:
            print(f"Match found: {array[arrIdx]}")
            # Move to the next element in the sequence
            seqIdx += 1
            print(f"Moving to the next element in sequence: new seqIdx = {seqIdx}")
        
        # Move to the next element in the array
        arrIdx += 1
        print(f"Moving to the next element in array: new arrIdx = {arrIdx}")

    # Final result after loop ends
    result = seqIdx == len(sequence)
    print(f"Entire sequence found in array: {result}")
    
    # Return True if the entire sequence has been found in the array in order, otherwise False
    return result

# Sample test case
array = [5, 1, 22, 25, 6, 7, 8, 10]
sequence = [1, 6, 8, 10]

# Validate subsequence
print("Result:", validateSubsequence(array, sequence))  # Should return True
