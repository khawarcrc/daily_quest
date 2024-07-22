def validateSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)

# Sample test case
array = [5, 1, 22, 25, 6, 7, 8, 10]
sequence = [1, 6,8, 10]

# Validate subsequence
print(validateSubsequence(array, sequence))  # Should return True
