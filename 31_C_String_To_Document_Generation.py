def generateDocument(characters, document):

    alreadyCounted = set()
    # Loop through each character in the document
    for character in document:
        if character in alreadyCounted:
            continue

        # Get how many times this character appears in the document
        documentFrequency = countCharacterFrequency(character, document)

        # Get how many times this character appears in the available characters
        charactersFrequency = countCharacterFrequency(character, characters)

        # If the document requires more of a character than we have, return False
        if documentFrequency > charactersFrequency:
            return False

        alreadyCounted.add(character)

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
document = "abc"  # Document we want to create
result = generateDocument(characters, document)
print(result)  # Expected output: True, because "abc" can be made from "aabbcc"
