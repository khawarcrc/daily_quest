# Problem Statement:
# Write a function that takes a string as input and returns the index of the first non-repeating character.
# If all characters in the string repeat, the function should return -1.

# Steps to Solve the Problem:

# 1. Initialize an empty dictionary to store the frequency of each character in the string.
#    - This dictionary will map each character to the number of times it appears in the string.

# 2. Iterate over each character in the input string.
#    - For each character, update its frequency count in the dictionary.
#    - Use the dictionary's `get` method to retrieve the current frequency of the character,
#      defaulting to 0 if the character is not yet in the dictionary.
#    - Increment the frequency count by 1 and store it back in the dictionary.

# 3. Iterate over the indices of the string to find the first non-repeating character.
#    - For each index, retrieve the character at that position in the string.
#    - Check the frequency of the character using the dictionary.
#    - If the frequency is 1, it means the character is non-repeating.
#    - Return the current index as the index of the first non-repeating character.

# 4. If the loop completes without finding a non-repeating character, return -1.
#    - This indicates that all characters in the string are repeating.

def firstNonRepeatingCharacter(string):
  characterFrequencies = {}  # Dictionary to store character frequencies

  # Count the frequency of each character in the string
  for character in string:
      characterFrequencies[character] = characterFrequencies.get(character, 0) + 1

  # Find the first character with a frequency of 1
  for index in range(len(string)):
      character = string[index]
      if characterFrequencies[character] == 1:
          return index  # Return the index of the first non-repeating character

  return -1  # Return -1 if no non-repeating character is found

# Dummy data for execution
test_string = "swiss"
result = firstNonRepeatingCharacter(test_string)
print(f"The index of the first non-repeating character is: {result}")