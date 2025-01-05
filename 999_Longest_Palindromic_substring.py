# """
# ------------------------------------------------------------
# Problem Statement:
# ------------------------------------------------------------
# Given a string, find the longest substring within it that forms a palindrome.
# A palindrome is a sequence of characters that reads the same backward and forward 
# (e.g., "madam", "racecar", "abba").

# We must return the longest palindromic substring that exists inside the given string.
# ------------------------------------------------------------
# """


# """
# ------------------------------------------------------------
# Understanding the Problem:
# ------------------------------------------------------------
# 1. Input: A string of characters. Example: "abaxyzzyxf".
# 2. Output: The longest substring that is a palindrome. Example: "xyzzyx".
# 3. Core Concept:
#    - A palindrome expands equally on both sides from its center.
#    - A palindrome can have either:
#         a) Odd length: single center (e.g., "racecar", center = 'e').
#         b) Even length: double center (e.g., "abba", center = between 'b' and 'b').
#    - So, for each character, we try to expand around it in both cases 
#      and check the maximum palindrome length.
# ------------------------------------------------------------
# """


# """
# ------------------------------------------------------------
# Code Execution Theory (Step by Step):
# ------------------------------------------------------------
# 1. Start with a "currentLongest" placeholder that keeps track of the 
#    indices of the longest palindrome found so far. Initially set to [0, 1]
#    (meaning the first character is itself a palindrome).

# 2. Loop through each index in the string starting from 1:
#    - For each index "i", try expanding around it to find the longest palindrome
#      with:
#         a) Odd center (expanding from i-1 to i+1).
#         b) Even center (expanding from i-1 to i).
#    - Compare both results and pick the longer one.

# 3. Update "currentLongest" if the new palindrome is longer.

# 4. After the loop ends, slice the string using the "currentLongest" 
#    indices to get the actual palindrome substring.

# 5. Helper function "getLongestPalindromeFrom":
#    - Expands outward as long as left and right characters match.
#    - Stops when characters differ or boundaries are reached.
#    - Returns the indices (start, end) of the longest palindrome found.
# ------------------------------------------------------------
# """


# ------------------- Corrected and Commented Code -------------------

def longestPalindromicSubstring(string):
    # Initialize the longest palindrome with the first character
    # [0,1] means substring from index 0 up to (not including) 1
    currentLongest = [0, 1]  
    
    # Iterate through string starting from index 1
    for i in range(1, len(string)):
        # Check for odd length palindrome (center at i)
        odd = getLongestPalindromeFrom(string, i - 1, i + 1)
        
        # Check for even length palindrome (center between i-1 and i)
        even = getLongestPalindromeFrom(string, i - 1, i)
        
        # Pick the longer one between odd and even palindrome
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        
        # Update the global currentLongest if the new palindrome is longer
        currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
    
    # Return the actual substring of longest palindrome found
    return string[currentLongest[0] : currentLongest[1]]


def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    # Expand outward while the boundaries are valid and characters match
    while leftIdx >= 0 and rightIdx < len(string):  # Corrected: should be >= 0
        if string[leftIdx] != string[rightIdx]:
            break  # Stop expansion if mismatch occurs
        leftIdx -= 1  # Move left pointer one step left
        rightIdx += 1  # Move right pointer one step right

    # When mismatch occurs, we step back to the last valid palindrome indices
    return [leftIdx + 1, rightIdx]


# ------------------- Dummy Data Example -------------------

string = "abaxyzzyxf"
print(longestPalindromicSubstring(string))  # Output: "xyzzyx"


# """
# ------------------------------------------------------------
# Industry Equivalent Scenario:
# ------------------------------------------------------------
# 1. DNA / RNA Sequence Analysis:
#    - Palindromic sequences are important in genetics (restriction enzyme sites).
#    - Finding longest palindromic subsequences helps in identifying biological markers.

# 2. Text Correction and Natural Language Processing (NLP):
#    - Detecting mirrored or repetitive structures in sentences or text.
#    - Useful in plagiarism detection, cryptography, and pattern matching.

# 3. Cybersecurity:
#    - Palindromic patterns in binary/hexadecimal strings could reveal 
#      hidden patterns in malware signatures or encrypted data.

# 4. Data Compression:
#    - Palindromic patterns indicate redundancy which can be exploited 
#      for efficient data compression.
# ------------------------------------------------------------
# """
