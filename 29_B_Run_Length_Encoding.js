function runLengthEncoding(string) {
    // Array to store the encoded string parts (run lengths and characters)
    let encodedStringCharacters = [];
    
    // Variable to track the current run length (consecutive occurrences of the same character)
    let currentRunLength = 1;
    
    // Loop through the string, starting from the second character (index 1)
    for (let i = 1; i < string.length; i++) {
        let currentCharacter = string[i];       // Current character in the string
        let previousCharacter = string[i - 1];  // Previous character
        
        // If the current character is different from the previous one,
        // or the current run length has reached 9, append the encoded segment
        if (currentCharacter !== previousCharacter || currentRunLength === 9) {
            // Append the run length (maximum 9) and the previous character to the encoded list
            encodedStringCharacters.push(currentRunLength.toString());
            encodedStringCharacters.push(previousCharacter);
            
            // Reset the run length for the next sequence of characters
            currentRunLength = 0;
        }
        
        // Increment the run length for the current character
        currentRunLength += 1;
    }
    
    // After the loop, append the last character's run length and the character itself
    encodedStringCharacters.push(currentRunLength.toString());
    encodedStringCharacters.push(string[string.length - 1]);
    
    // Join the array into a single string and return the encoded result
    return encodedStringCharacters.join('');
}

// Testing the function with some dummy data

// Test cases
let input1 = "AAAAAAAAAAAAABBCCCCDD";
let input2 = "************^^^^^^^$$$$$$%%%%%%%!!!!!!AAAAAAAAAAAAAAAAAAAA";

// Print outputs for each test case
console.log(`Input: ${input1} -> Encoded: ${runLengthEncoding(input1)}`);
console.log(`Input: ${input2} -> Encoded: ${runLengthEncoding(input2)}`);
