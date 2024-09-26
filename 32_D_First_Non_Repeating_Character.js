function firstNonRepeatingCharacter(string) {
    const characterFrequencies = {};  // Object to store character frequencies

    // Count the frequency of each character in the string
    for (const character of string) {
        characterFrequencies[character] = (characterFrequencies[character] || 0) + 1;
    }

    // Find the first character with a frequency of 1
    for (let index = 0; index < string.length; index++) {
        const character = string[index];
        if (characterFrequencies[character] === 1) {
            return index;  // Return the index of the first non-repeating character
        }
    }

    return -1;  // Return -1 if no non-repeating character is found
}

// Dummy data for execution
const testString = "swiss";
const result = firstNonRepeatingCharacter(testString);
console.log(`The index of the first non-repeating character is: ${result}`);