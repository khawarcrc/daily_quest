# def commonCharacter(strings): 
#     characterCount = {} 
#     for string in strings: 
#         uniqueStringCharacters = set(string)
#         for character in uniqueStringCharacters: 
#             if character not in characterCount: 
#                 characterCount[character] = 0
#             characterCount[character] += 1    
    
#     finalCharacters = []
    
#     for character, count in characterCount.items(): 
#         if count == len(strings): 
#             finalCharacters.append(character)  
#     return finalCharacters      


# Problem Statement:
# You are tasked with writing a function that identifies characters that are common 
# across a list of strings. The function should return a list of characters that 
# appear in every string of the input list.

# Steps to Solve the Problem:

# 1. Initialize a Dictionary for Character Counts:
#    - Create an empty dictionary (characterCount) to store characters as keys 
#      and the number of strings in which each character appears as values.

# 2. Iterate Through Each String:
#    - Loop through each string in the input list of strings.

# 3. Create a Set of Unique Characters:
#    - For each string, convert it into a set to get the unique characters, 
#      ensuring that duplicates within the same string are ignored.

# 4. Count Occurrences of Each Character:
#    - Loop through the set of unique characters:
#      - If a character is not in the dictionary, initialize its count to 0.
#      - Increment the count for that character to indicate it has been found in 
#        the current string.

# 5. Initialize a List for Common Characters:
#    - Create an empty list (finalCharacters) to store the characters that are 
#      found in all strings.

# 6. Identify Common Characters:
#    - Loop through the dictionary of character counts:
#      - Check if the count of each character equals the total number of strings.
#      - If it does, append the character to the list of common characters.

# 7. Return the List of Common Characters:        


def commonCharacter(strings): 
    # Dictionary to store characters and the number of strings they appear in
    characterCount = {} 
    
    print("Initial character count dictionary:", characterCount)
    
    # Iterate through each string in the list of strings
    for string in strings: 
        # Create a set of unique characters in the current string to avoid duplicates
        uniqueStringCharacters = set(string)
        print(f"\nProcessing string: '{string}', Unique characters: {uniqueStringCharacters}")
        
        # Iterate through each unique character in the string
        for character in uniqueStringCharacters: 
            # If the character is not already in the dictionary, add it with a count of 0
            if character not in characterCount: 
                print(f"Adding character '{character}' to the dictionary with initial count 0.")
                characterCount[character] = 0
            # Increment the count for the character (for each string it appears in)
            characterCount[character] += 1  
            print(f"Incrementing count for character '{character}'. Current count: {characterCount[character]}")
    
    print("\nFinal character count after processing all strings:", characterCount)
    
    # List to store the characters that are common in all strings
    finalCharacters = []
    
    # Iterate through the dictionary of character counts
    for character, count in characterCount.items(): 
        # If the count of the character equals the number of strings, it's common to all
        if count == len(strings): 
            print(f"Character '{character}' is common to all strings.")
            finalCharacters.append(character)  # Add the common character to the list
    
    print("\nFinal list of common characters:", finalCharacters)
    
    # Return the list of common characters
    return finalCharacters


# Test case 1: Strings with common characters 'a' and 'b'
input1 = ["aaabcdfg", "bcakdshkjds", "cabiewoiuew"]
print(f"Common characters in {input1}: {commonCharacter(input1)}")  
# Output: ['a', 'b', 'c'] 

