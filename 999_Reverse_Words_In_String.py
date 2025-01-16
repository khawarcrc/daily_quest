# reverse_words_in_string.py

"""
Problem Statement:
------------------
Given a string 's', reverse the order of words in it. 
A word is defined as a sequence of non-space characters. 
The words in 's' will be separated by at least one space. 

The returned string should have only a single space separating the words. 
There should be no leading or trailing spaces.

Example:
Input: "  hello   world  "
Output: "world hello"

Constraints / Edge Cases:
-------------------------
1. The string may have leading or trailing spaces.
2. The string may have multiple spaces between words.
3. The string may contain only one word.
4. The string may be empty.
5. The string may contain only spaces.
6. The string may contain special characters or numbers as part of words.

Execution Flow / Approach:
--------------------------
1. Trim the string to remove leading and trailing spaces.
2. Split the string by spaces to extract words.
3. Remove empty strings from the list (caused by multiple spaces).
4. Reverse the list of words.
5. Join the reversed words using a single space.
6. Return the final reversed string.
"""

# Python Code Implementation

def reverse_words_in_string(s: str) -> str:
    """
    Reverses the words in the input string s.
    """
    # Step 1: Trim leading and trailing spaces
    trimmed_s = s.strip()

    # Step 2: Split the string by spaces
    words = trimmed_s.split(' ')

    # Step 3: Remove empty strings caused by multiple spaces
    words = [word for word in words if word]

    # Step 4: Reverse the list of words
    words.reverse()

    # Step 5: Join the reversed words with a single space
    reversed_s = ' '.join(words)

    return reversed_s

# Edge case testing
if __name__ == "__main__":
    test_cases = [
        "  hello   world  ",     # Normal case with extra spaces
        "single",               # Single word
        "",                     # Empty string
        "     ",                # String with only spaces
        "a b c",                # Multiple single-character words
        "abc 3.10 is great!",# Words with special characters / punctuation
    ]

    for i, test in enumerate(test_cases, 1):
        print(f"Test Case {i}: '{test}'")
        print(f"Output: '{reverse_words_in_string(test)}'\n")
