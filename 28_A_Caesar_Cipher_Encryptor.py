# Problem Statement:
# Given a string consisting of lowercase alphabetic characters, implement a Caesar Cipher encryption function.
# In a Caesar Cipher, each letter in the string is shifted by a specified number of positions (key) forward in the alphabet.
# The goal is to return a new string where each character is replaced by the letter found after shifting by the key value.
# If shifting a letter goes beyond 'z', it wraps around back to the start of the alphabet.
# For example, shifting 'z' by 1 will result in 'a'.

# Steps to Solve the Problem (Caesar Cipher Encryption):

# Step 1: Initialization
# - Initialize an empty list to store the new encrypted letters.
# - Ensure that the key is in the range of 0 to 25 using the modulo operator with 26 (since there are 26 letters in the alphabet).

# Step 2: Iterate Through Each Character in the Input String
# - Loop through each letter of the input string one by one.

# Step 3: Shift Each Letter
# - For each letter, find its ASCII code using the `ord()` function.
# - Add the key to the ASCII code to get the new letter's ASCII code.
# - If the new letter code exceeds the ASCII value of 'z' (which is 122), handle the wrap-around by subtracting from 122
#   and adding back the offset from the start of the alphabet.

# Step 4: Append New Letter to the List
# - Convert the new ASCII code back to a character using the `chr()` function.
# - Append the shifted letter to the list of new letters.

# Step 5: Combine the List into a New String
# - After processing all the letters, join the list of new letters into a single string using `"".join()`.
# - Return the new encrypted string.

# Step 6: Return the Encrypted String
# - Return the final string, which contains the encrypted version of the input string with all letters shifted according to the key.


def caesarCipherEncryptor(string, key):
    # Initialize an empty list to store new letters
    newLetters = []

    # Ensure key is within 0 to 25 by taking modulo 26
    newKey = key % 26

    # Iterate through each letter in the string
    for letter in string:
        # Append the new letter obtained by shifting with the key
        newLetters.append(getNewLetter(letter, newKey))

    # Join the list of new letters into a single string and return
    return "".join(newLetters)


def getNewLetter(letter, key):
    # Convert the character to its ASCII value
    # Each character (letter) has an associated ASCII code
    # For example: 'a' has ASCII 97, 'b' has ASCII 98, and 'z' has ASCII 122
    # The ord() function is used to get the ASCII code of a letter

    newLetterCode = ord(letter) + key

    # Check if the new ASCII code exceeds 'z' (ASCII 122)
    # If so, wrap it around to stay within the alphabet range
    # For example, if the shifted ASCII code exceeds 122:
    # newLetterCode = ord('z') + 2 = 124
    # To wrap around, we calculate the offset from 122 using % and add it to 96
    # This brings it back to 'a' or beyond if necessary
    # chr(96 + newLetterCode % 122) handles the wrapping logic:
    #   newLetterCode % 122 calculates the offset beyond 'z'
    #   Adding this offset to 96 ensures the new letter wraps correctly
    # Example: newLetterCode = 124 => 96 + (124 % 122) = 98 => 'b'

    # If the new letter's ASCII code is within the valid range (<= 122), return it directly

    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)


# Example usage with dummy data
# Test Case 1
input_string = "xyz"
shift_key = 2
encrypted_string = caesarCipherEncryptor(input_string, shift_key)
print(f"Encrypted string: {encrypted_string}")  # Expected output: "zab"

# Test Case 2
input_string2 = "abc"
shift_key2 = 3
encrypted_string2 = caesarCipherEncryptor(input_string2, shift_key2)
print(f"Encrypted string: {encrypted_string2}")  # Expected output: "def"

# Test Case 3
input_string3 = "hello"
shift_key3 = 1
encrypted_string3 = caesarCipherEncryptor(input_string3, shift_key3)
print(f"Encrypted string: {encrypted_string3}")  # Expected output: "ifmmp"
