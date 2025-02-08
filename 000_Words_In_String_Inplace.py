

"""
Problem Statement:
------------------
Given a string 's', reverse the order of words in it **in-place** (without using extra space for storing words). 
A word is defined as a sequence of non-space characters. The words in 's' are separated by spaces.

The returned string should:
1. Contain words in reversed order.
2. Have only a single space separating the words.
3. Have no leading or trailing spaces.

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

Execution Flow / In-Place Approach:
-----------------------------------
1. Convert the string to a list of characters (strings in Python are immutable).
2. Remove extra spaces (leading, trailing, and multiple spaces in between) in-place.
3. Reverse the entire character list.
4. Iterate through the list and reverse each word individually.
5. Convert the list back to a string and return.
"""

# Python Code Implementation (In-place)

def reverse_words_inplace(s: str) -> str:
    """
    Reverses words in the string in-place without using extra space for words.
    """
    # Convert string to list of characters
    chars = list(s)
    
    # Step 1: Remove extra spaces in-place
    def remove_extra_spaces(chars):
        n = len(chars)
        i = 0  # read pointer
        j = 0  # write pointer

        while i < n:
            # Skip leading spaces
            while i < n and chars[i] == ' ':
                i += 1
            # Copy word characters
            while i < n and chars[i] != ' ':
                chars[j] = chars[i]
                i += 1
                j += 1
            # Skip spaces between words and add single space if next word exists
            while i < n and chars[i] == ' ':
                i += 1
            if i < n:
                chars[j] = ' '
                j += 1
        return chars[:j]  # return trimmed portion

    chars = remove_extra_spaces(chars)

    # Step 2: Reverse the entire list
    def reverse_list(chars, left, right):
        """
        Reverse a portion of the list from index 'left' to 'right'.
        Theory:
        - By reversing the entire string first, the words' order is reversed,
        but each word itself is backward.
        - This sets up for Step 3 where we reverse each word to correct their orientation.
        """
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    # Step 3: Reverse each word individually
    n = len(chars)
    start = 0
    for end in range(n + 1):
        if end == n or chars[end] == ' ':
            """
            Reverse each word to fix its orientation.
            Theory:
            - After Step 2, the entire string is reversed.
            - Each word is backward; reversing each word individually restores proper spelling
            while keeping the words in reversed order.
            """
            reverse_list(chars, start, end - 1)
            start = end + 1

    # Convert list back to string
    return ''.join(chars)

# Edge case testing
if __name__ == "__main__":
    test_cases = [
        "  hello   world  ",     # Normal case with extra spaces
        "single",               # Single word
        "",                     # Empty string
        "     ",                # String with only spaces
        "a b c",                # Multiple single-character words
     
    ]

    for i, test in enumerate(test_cases, 1):
        print(f"Test Case {i}: '{test}'")
        print(f"Output: '{reverse_words_inplace(test)}'\n")
