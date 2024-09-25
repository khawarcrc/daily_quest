function generateDocument(characters, document) {
    // Create an empty object to count occurrences of each character in 'characters'
    const characterCounts = {};

    // Count how many times each character appears in 'characters'
    for (let character of characters) {
        if (!(character in characterCounts)) {
            characterCounts[character] = 0; // Initialize count to 0 if character is not present
        }
        characterCounts[character] += 1; // Increase the count of this character
    }

    // Check if we have enough characters to fulfill the 'document'
    for (let character of document) {
        // If the character doesn't exist or has been used up, return false
        if (!(character in characterCounts) || characterCounts[character] === 0) {
            return false; // Cannot fulfill the document
        }
        characterCounts[character] -= 1; // Use one of the characters to fulfill part of the document
    }

    // If the entire document can be fulfilled, return true
    return true;
}

// Example usage with dummy data
const characters = "aabbcc"; // Available characters
const document = "abc";      // Document we want to create

const result = generateDocument(characters, document);
console.log(result); // Expected output: true
