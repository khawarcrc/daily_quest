def isPalindrome(string):
    # Initialize leftIndex to the first character (index 0)
    leftIndex = 0
    
    # Initialize rightIndex to the last character (index len(string) - 1)
    rightIndex = len(string) - 1
    
    # Loop until leftIndex is less than rightIndex (i.e., until the middle of the string)
    while leftIndex < rightIndex:
        # If characters at leftIndex and rightIndex don't match, it's not a palindrome
        if string[leftIndex] != string[rightIndex]:
            return False
        
        # Move towards the middle by updating left and right indices
        leftIndex += 1
        rightIndex -= 1
    
    # If all characters match, the string is a palindrome
    return True


# Example usage with dummy data
data = "racecar"  # Palindrome string
result = isPalindrome(data)
print(f"Is '{data}' a palindrome? {result}")

data2 = "hello"  # Non-palindrome string
result2 = isPalindrome(data2)
print(f"Is '{data2}' a palindrome? {result2}")
