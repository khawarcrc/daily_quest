/*
------------------------------------------------------------
Problem Statement:
------------------------------------------------------------
Given a string, find the longest substring within it that forms a palindrome.
A palindrome is a sequence of characters that reads the same backward and forward 
(e.g., "madam", "racecar", "abba").

We must return the longest palindromic substring that exists inside the given string.
------------------------------------------------------------
*/

function longestPalindromicSubstring(string) {
    // Store indices [start, end] of the current longest palindrome
    let currentLongest = [0, 1];

    // Iterate over each character in the string starting from index 1
    for (let i = 1; i < string.length; i++) {
        console.log(`\n Checking index ${i}, character '${string[i]}'`);

        // Check for odd length palindrome (center at i)
        let odd = getLongestPalindromeFrom(string, i - 1, i + 1);

        // Check for even length palindrome (center between i-1 and i)
        let even = getLongestPalindromeFrom(string, i - 1, i);

        console.log(`   Odd palindrome: '${string.slice(odd[0], odd[1])}', indices: [${odd}]`);
        console.log(`   Even palindrome: '${string.slice(even[0], even[1])}', indices: [${even}]`);

        // Pick the longer palindrome between odd and even
        let longest = (odd[1] - odd[0] > even[1] - even[0]) ? odd : even;

        // Update global currentLongest if the new palindrome is longer
        if (longest[1] - longest[0] > currentLongest[1] - currentLongest[0]) {
            currentLongest = longest;
            console.log(` Updated Longest Palindrome: '${string.slice(currentLongest[0], currentLongest[1])}'`);
        }
    }

    // Extract the substring using slice(start, end)
    return string.slice(currentLongest[0], currentLongest[1]);
}

function getLongestPalindromeFrom(string, leftIdx, rightIdx) {
    // Expand outward while characters at left and right match
    while (leftIdx >= 0 && rightIdx < string.length) {
        if (string[leftIdx] !== string[rightIdx]) {
            break; // Stop expansion if mismatch occurs
        }
        leftIdx--;   // Move left pointer one step left
        rightIdx++;  // Move right pointer one step right
    }

    // Return the valid palindrome indices
    return [leftIdx + 1, rightIdx];
}

// ------------------- Dummy Data Example -------------------
let string = "abaxyzzyxf";
console.log("\nFinal Result:", longestPalindromicSubstring(string));  
// Expected Output: "xyzzyx"
