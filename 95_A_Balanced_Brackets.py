def balancedBrackets(string):
    stack = []
    openingBrackets = "([{"
    closingBrackets = ")]}"
    matchingBrackets = {")": "(", "]": "[", "}": "{"}

    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if not stack or stack[-1] != matchingBrackets[char]:
                return False
            stack.pop()

    return len(stack) == 0

