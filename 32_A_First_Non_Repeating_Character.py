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
