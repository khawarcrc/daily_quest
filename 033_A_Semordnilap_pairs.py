# Problem Statement:
# ------------------
# Given a list of words, find all pairs of "semordnilap" words. A semordnilap is a word that forms another 
# valid word when reversed. For example, the word "stressed" reversed becomes "desserts", making them a semordnilap pair.
# The goal is to return all such semordnilap pairs from the list, ensuring that each word is used only once.

# Steps to Solve the Problem:
# ---------------------------
# 1. Convert the input list of words into a set for efficient lookups.
# 2. Initialize an empty list to store the semordnilap pairs.
# 3. Iterate through each word in the list:
#    a) Reverse the current word.
#    b) Check if the reversed word exists in the set and is not equal to the original word (to avoid palindromes).
#    c) If both conditions are met, add the original word and its reversed version as a pair to the list.
#    d) Remove both the original word and its reversed word from the set to avoid duplicate pairings.
# 4. After iterating through all the words, return the list of semordnilap pairs.


def semordnilap(words):
    # Create a set of the input words for faster lookup
    wordSet = set(words)
    
    # Initialize an empty list to store semordnilap pairs
    semordnilapPairs = []
    
    # Iterate over each word in the input list
    for word in words:
        # Reverse the current word
        reverse = word[::-1] 
        
        # Check if the reversed word is in the set and is not the same as the original word
        if reverse in wordSet and reverse != word:
            # Add the word and its reverse as a pair to the result list
            semordnilapPairs.append([word, reverse])
            
            # Remove both the word and its reverse from the set to avoid rechecking
            wordSet.remove(word)
            wordSet.remove(reverse)
    
    # Return the list of semordnilap pairs
    return semordnilapPairs        

# Dummy data for testing
words = ['stressed', 'desserts', 'evil', 'live', 'diaper', 'repaid', 'test', 'hello']

# Call the function and print the result
print(semordnilap(words))
