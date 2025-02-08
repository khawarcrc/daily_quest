# Problem Statement:
# Write a function that takes a string as input and returns the index of the first non-repeating character.
# If all characters in the string repeat, the function should return -1.

# Steps to Solve the Problem:

# 1. Iterate over each character in the string using an outer loop.
#    - Use a variable `index1` to track the current position in the string.

# 2. Initialize a flag variable `foundDuplicate` to False.
#    - This flag will be used to determine if the current character has any duplicates in the string.

# 3. Use an inner loop to compare the current character with every other character in the string.
#    - Use a variable `index2` to track the position of the character being compared.

# 4. For each comparison, check if the characters at `index1` and `index2` are the same and the indices are different.
#    - If they are the same, set `foundDuplicate` to True, indicating that a duplicate has been found.
#    - Break out of the inner loop since a duplicate has been found, and there's no need to check further.

# 5. After the inner loop, check if `foundDuplicate` is still False.
#    - If it is False, it means the character at `index1` is non-repeating.
#    - Return `index1` as the index of the first non-repeating character.

# 6. If the outer loop completes without finding a non-repeating character, return -1.
#    - This indicates that all characters in the string are repeating.
def firstNonRepeatingCharacter(string):
    # Iterate over each character in the string
    for index1 in range(len(string)):
        foundDuplicate = False  # Flag to check if a duplicate is found

        # Compare the current character with every other character
        for index2 in range(len(string)):
            # Check if characters are the same and indices are different

            if string[index1] == string[index2] and index1 != index2:
                foundDuplicate = True  # Mark as duplicate found
                break  # No need to check further, break out of the inner loop

        # If no duplicate was found, return the current index
        if not foundDuplicate:
            return index1

    # If no non-repeating character is found, return -1
    return -1


# Dummy data for execution
test_string = "swiss"
result = firstNonRepeatingCharacter(test_string)
print(f"The index of the first non-repeating character is: {result}")
