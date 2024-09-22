function isPalindrome(string) {
    // Initialize leftIndex to the first character (index 0)
    let leftIndex = 0;
    
    // Initialize rightIndex to the last character (index string.length - 1)
    let rightIndex = string.length - 1;
    
    // Loop until leftIndex is less than rightIndex (i.e., until the middle of the string)
    while (leftIndex < rightIndex) {
        // If characters at leftIndex and rightIndex don't match, it's not a palindrome
        if (string[leftIndex] !== string[rightIndex]) {
            return false;
        }
        
        // Move towards the middle by updating left and right indices
        leftIndex++;
        rightIndex--;
    }
    
    // If all characters match, the string is a palindrome
    return true;
}

// Example usage with dummy data
const data = "racecar";  // Palindrome string
const result = isPalindrome(data);
console.log(`Is '${data}' a palindrome? ${result}`);

const data2 = "hello";  // Non-palindrome string
const result2 = isPalindrome(data2);
console.log(`Is '${data2}' a palindrome? ${result2}`);
