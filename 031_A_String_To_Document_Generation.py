# Problem Statement:
# Given two strings, 'characters' and 'document', determine whether you can generate 
# the 'document' string using only the characters from the 'characters' string.
# Each character in 'characters' can only be used as many times as it appears in that string.
# The goal is to return True if the document can be created, otherwise return False.

# Steps to Solve the Problem:

# 1. Loop through each character in the 'document' string.
# 2. For each character in the 'document', calculate how many times it appears in the 'document' itself.
# 3. Then, calculate how many times that character appears in the 'characters' string.
# 4. If the character appears more times in the 'document' than in 'characters', return False, 
#    because we don't have enough of that character to generate the document.
# 5. If all characters in the 'document' are available in 'characters' in sufficient quantity, return True.


def generateDocument(characters, document):
    # Loop through each character in the document
    for character in document:
        
        # Get how many times this character appears in the document
        documentFrequency = countCharacterFrequency(character, document)
        
        # Get how many times this character appears in the available characters
        charactersFrequency = countCharacterFrequency(character, characters)
        
        # If the document requires more of a character than we have, return False
        if documentFrequency > charactersFrequency:
            return False
    
    # If all characters are available in sufficient quantity, return True
    return True

def countCharacterFrequency(character, target):
    # Start a counter for the frequency of the character
    frequency = 0
    
    # Loop through each character in the target string
    for char in target:
        
        # If the character matches the target character, increase the frequency
        if char == character:
            frequency += 1
            
    # Return the final count
    return frequency

# Testing the function with dummy data
# Dummy data for testing
characters = "aabbcc"  # Available characters
document = "abc"       # Document we want to create
result = generateDocument(characters, document)
print(result)  # Expected output: True, because "abc" can be made from "aabbcc"
