function semordnilap(words) {
    // Create a set from the input words for faster lookup
    let wordSet = new Set(words);
    
    // Initialize an empty array to store semordnilap pairs
    let semordnilapPairs = [];
    
    // Iterate over each word in the input array
    for (let word of words) {
        // Reverse the current word
        let reverse = word.split('').reverse().join('');
        
        // Check if the reversed word is in the set and is not the same as the original word
        if (wordSet.has(reverse) && reverse !== word) {
            // Add the word and its reverse as a pair to the result array
            semordnilapPairs.push([word, reverse]);
            
            // Remove both the word and its reverse from the set to avoid rechecking
            wordSet.delete(word);
            wordSet.delete(reverse);
        }
    }
    
    // Return the list of semordnilap pairs
    return semordnilapPairs;
}

// Dummy data for testing
const words = ['stressed', 'desserts', 'evil', 'live', 'diaper', 'repaid', 'test', 'hello'];

// Call the function and print the result
console.log(semordnilap(words));
