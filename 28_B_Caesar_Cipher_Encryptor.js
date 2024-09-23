function caesarCipherEncryptor(string, key) {
    // Initialize an empty array to store new letters
    let newLetters = [];
    
    // Ensure key is within 0 to 25 by taking modulo 26
    let newKey = key % 26;
    
    // Iterate through each letter in the string
    for (let letter of string) {
        // Append the new letter obtained by shifting with the key
        newLetters.push(getNewLetter(letter, newKey));
    }
    
    // Join the list of new letters into a single string and return
    return newLetters.join('');
}

function getNewLetter(letter, key) {
    // Convert the character to its ASCII value using charCodeAt
    let newLetterCode = letter.charCodeAt(0) + key;
    
    // Check if the new ASCII code exceeds 'z' (ASCII 122)
    // Wrap around if necessary
    return newLetterCode <= 122 
        ? String.fromCharCode(newLetterCode) 
        : String.fromCharCode(96 + newLetterCode % 122);
}

// Example usage with dummy data
// Test Case 1: 'xyz' shifted by 2 should wrap around to 'zab'
let inputString = "xyz";
let shiftKey = 2;
let encryptedString = caesarCipherEncryptor(inputString, shiftKey);
console.log(`Encrypted string: ${encryptedString}`);  // Expected output: "zab"
