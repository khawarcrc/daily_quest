function commonCharacters(strings) {
    // Find the smallest string to limit the set of potential common characters
    const smallestString = getSmallestString(strings);
    
    // Create a set of potential common characters from the smallest string
    let potentialCommonCharacters = new Set(smallestString);

    // Iterate through each string to filter out non-existent characters
    for (const string of strings) {
        removeNonexistantCharacters(string, potentialCommonCharacters);
    }
    
    // Convert the set of common characters back to an array and return it
    return [...potentialCommonCharacters];
}

function getSmallestString(strings) {
    // Initialize smallestString with the first string in the list
    let smallestString = strings[0];
    
    // Iterate through the list to find the smallest string
    for (const string of strings) {
        if (string.length < smallestString.length) {
            smallestString = string; // Update smallestString if a smaller one is found
        }
    }
    return smallestString;
}

function removeNonexistantCharacters(string, potentialCommonCharacters) {
    // Convert the current string into a set of its unique characters
    const uniqueStringCharacters = new Set(string);

    // Iterate through the list of potential common characters
    for (const character of [...potentialCommonCharacters]) {
        // Remove the character if it is not found in the current string
        if (!uniqueStringCharacters.has(character)) {
            potentialCommonCharacters.delete(character);
        }
    }
}

// Dummy data for testing the function
const dummyStrings = ["bella", "label", "roller"];
// Calling the function with dummy data
const commonChars = commonCharacters(dummyStrings);

// Output the result
console.log("Common characters:", commonChars);

