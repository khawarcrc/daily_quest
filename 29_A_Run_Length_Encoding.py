# Problem Statement:
# Implement a Run-Length Encoding (RLE) algorithm that compresses a string by
# replacing sequences of the same character with the character and its frequency.
# The frequency is capped at 9. If a sequence exceeds 9, split it into parts.
# Example: "AAAAAAAAAAAAABBCCCCDD" should be encoded as "9A4A2B4C2D".

# Steps to Solve:
# 1. Initialize an empty list to store the encoded string parts.
# 2. Use a variable to track the current run length of consecutive characters.
# 3. Loop through the string from the second character.
# 4. Compare each character with the previous one:
#    - If different or the run reaches 9, append the run length and character.
# 5. Reset the run length when necessary and continue.
# 6. After the loop, append the final run length and character.
# 7. Join the encoded parts and return the final encoded string.


def runLengthEncoding(string):
    # List to store the encoded string parts (run lengths and characters)
    encodedStringCharacters = []

    # Variable to track the current run length (consecutive occurrences of the same character)
    currentRunLength = 1

    # Loop through the string, starting from the second character (index 1)
    for i in range(1, len(string)):
        currentCharacter = string[i]  # Current character in the string
        previousCharacter = string[i - 1]  # Previous character

        # If the current character is different from the previous one,
        # or the current character equals '9' (this condition seems like a bug)
        if currentCharacter != previousCharacter or currentRunLength == 9:
            # Append the run length and the previous character to the encoded list
            encodedStringCharacters.append(str(currentRunLength))
            encodedStringCharacters.append(previousCharacter)

            # Reset the run length for the next sequence of characters
            currentRunLength = 0

        # Increment the run length for the current character
        currentRunLength += 1

    # After the loop, append the last character's run length and the character itself
    encodedStringCharacters.append(str(currentRunLength))
    encodedStringCharacters.append(string[len(string) - 1])

    # Join the list into a single string and return the encoded result
    return "".join(encodedStringCharacters)


# Testing the function with some dummy data

# Dummy data examples
input1 = "aaaaaaaaaaaabbccc"
input2 = "bbbbbb"
input3 = "aabbaa"
input4 = "xyz"
input5 = "AAAAAAAAAAAAABBCCCCDDDDDDDDDDD"

# Print outputs for each test case
print(f"Input: {input1} -> Encoded: {runLengthEncoding(input1)}")
print(f"Input: {input2} -> Encoded: {runLengthEncoding(input2)}")
print(f"Input: {input3} -> Encoded: {runLengthEncoding(input3)}")
print(f"Input: {input4} -> Encoded: {runLengthEncoding(input4)}")
print(f"Input: {input5} -> Encoded: {runLengthEncoding(input5)}")
