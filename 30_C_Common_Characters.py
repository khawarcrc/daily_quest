
# Problem Statement:
# Given a list of strings, write a function to determine the characters that are common to all strings.
# The output should be a list of unique characters that appear in every string from the input list.

# Steps to Solve the Problem:
# 1. Define a function `commonCharacters` that takes a list of strings as input.
# 2. Create a helper function `getSmallestString` to find the string with the smallest length in the list.
# 3. Initialize a set of potential common characters using the characters from the smallest string.
# 4. Iterate through each string in the input list:
#    a. For each string, call a helper function `removeNonexistantCharacters` to filter out characters
#       that are not present in the current string.
# 5. After processing all strings, convert the remaining characters in the set of potential common characters
#    back to a list.
# 6. Return the list of common characters as the output.

def commonCharacters(strings):
    # Find the smallest string to limit the set of potential common characters
    smallestString = getSmallestString(strings)
    print(f"Smallest string found: '{smallestString}'")  # Print the smallest string
    
    # Create a set of potential common characters from the smallest string
    potentialCommonCharacters = set(smallestString)
    print(f"Initial potential common characters: {potentialCommonCharacters}")  # Print initial common characters

    # Iterate through each string to filter out non-existent characters
    for string in strings:
        print(f"Checking string: '{string}'")  # Print the current string being checked
        removeNonexistantCharacters(string, potentialCommonCharacters)
        print(f"Potential common characters after checking '{string}': {potentialCommonCharacters}")  # Print the updated characters
    
    # Convert the set of common characters back to a list and return it
    return list(potentialCommonCharacters)


def getSmallestString(strings):
    # Initialize smallestString with the first string in the list
    smallestString = strings[0]
    
    # Iterate through the list to find the smallest string
    for string in strings:
        if len(string) < len(smallestString):
            smallestString = string  # Update smallestString if a smaller one is found
    return smallestString


def removeNonexistantCharacters(string, potentialCommonCharacters):
    # Convert the current string into a set of its unique characters
    uniqueStringCharacters = set(string)

    # Iterate through the list of potential common characters
    for character in list(potentialCommonCharacters):
        # Remove the character if it is not found in the current string
        if character not in uniqueStringCharacters:
            potentialCommonCharacters.remove(character)
            print(f"Removing character: '{character}'")  # Print the character being removed


# Dummy data for testing the function
dummy_strings = ["bella", "label", "roller"]
# Calling the function with dummy data
common_chars = commonCharacters(dummy_strings)

# Output the result
print("Common characters:", common_chars)