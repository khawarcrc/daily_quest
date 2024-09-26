function firstNonRepeatingCharacter(string) {
    // Iterate over each character in the string
    for (let index1 = 0; index1 < string.length; index1++) {
        let foundDuplicate = false;  // Flag to check if a duplicate is found

        // Compare the current character with every other character
        for (let index2 = 0; index2 < string.length; index2++) {
            // Check if characters are the same and indices are different
            if (string[index1] === string[index2] && index1 !== index2) {
                foundDuplicate = true;  // Mark as duplicate found
                break;  // No need to check further, break out of the inner loop
            }
        }

        // If no duplicate was found, return the current index
        if (!foundDuplicate) {
            return index1;
        }
    }

    // If no non-repeating character is found, return -1
    return -1;
}

// Dummy data for execution
const testString = "swiss";
const result = firstNonRepeatingCharacter(testString);
console.log(`The index of the first non-repeating character is: ${result}`);