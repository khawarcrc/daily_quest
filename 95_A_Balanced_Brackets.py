# ------------------------------------------------------------
# PROBLEM STATEMENT:
# ------------------------------------------------------------
# You are given a string consisting of different types of brackets:
# (), [], {}
# Your task is to write a function that determines if the brackets
# are "balanced".
#
# A string is considered balanced if:
# 1. Every opening bracket has a corresponding closing bracket.
# 2. The brackets are closed in the correct order.
#
# Example:
# "([])"  -> Balanced  ✅
# "([)]"  -> Not Balanced ❌
# "((("   -> Not Balanced ❌
#
# ------------------------------------------------------------
# PROBLEM EXPLANATION / THEORY:
# ------------------------------------------------------------
# - Brackets must always open and close in a Last-In-First-Out (LIFO) manner.
# - This means the "last" opened bracket should be the "first" one to close.
# - To achieve this behavior, we use a "stack" data structure.
#
# STEPS:
# 1. Create an empty stack.
# 2. Traverse through each character in the string.
# 3. If the character is an opening bracket ( ( { [ ), push it onto the stack.
# 4. If the character is a closing bracket ( ) } ] ):
#    - Check if the stack is empty (if yes -> unbalanced).
#    - Otherwise, compare the top of the stack with the matching opening bracket.
#    - If it matches, pop from the stack (since this pair is balanced).
#    - If it does not match, return False immediately (unbalanced).
# 5. After traversing the string:
#    - If the stack is empty, return True (all brackets matched).
#    - If the stack is not empty, return False (some brackets were not closed).
#
# ------------------------------------------------------------
# CODE IMPLEMENTATION WITH COMMENTS:
# ------------------------------------------------------------

def balancedBrackets(string):
    # Stack is used to keep track of opening brackets
    stack = []
    
    # Define the valid opening brackets
    openingBrackets = "([{"
    
    # Define the valid closing brackets
    closingBrackets = ")]}"
    
    # Create a dictionary that maps closing brackets to their opening pairs
    matchingBrackets = {
        ")": "(",   # Closing ) should match opening (
        "]": "[",   # Closing ] should match opening [
        "}": "{"    # Closing } should match opening {
    }

    # Traverse through every character in the given string
    for char in string:
        # If the character is an opening bracket, push it onto the stack
        if char in openingBrackets:
            stack.append(char)
        
        # If the character is a closing bracket
        elif char in closingBrackets:
            # Case 1: If stack is empty, there's no matching opening bracket
            if not stack:
                return False
            
            # Case 2: Check if the last bracket in the stack matches correctly
            if stack[-1] != matchingBrackets[char]:
                return False
            
            # Case 3: If it matches, remove (pop) the last bracket from the stack
            stack.pop()

    # Final check:
    # If stack is empty -> all brackets matched -> Balanced
    # If stack still has elements -> Unbalanced
    return len(stack) == 0


# ------------------------------------------------------------
# DUMMY DATA (TEST CASES):
# ------------------------------------------------------------

print(balancedBrackets("([])"))     # True -> properly nested
print(balancedBrackets("([)]"))     # False -> wrong order
print(balancedBrackets("((("))      # False -> not closed
print(balancedBrackets("{[()]}"))   # True -> perfectly nested
print(balancedBrackets("{[}]"))     # False -> mismatch
print(balancedBrackets("no brackets here")) # True -> nothing to check

# ------------------------------------------------------------
# INDUSTRY REAL-TIME APPLICATION SCENARIO:
# ------------------------------------------------------------
# 1. COMPILERS / INTERPRETERS:
#    - When a compiler reads source code, it must ensure parentheses,
#      braces, and brackets are balanced. For example:
#      if(condition) { doSomething(); }
#      If any bracket is missing, the compiler throws a syntax error.
#
# 2. HTML/XML PARSERS:
#    - Checking if tags <div> ... </div> are properly opened and closed
#      works similarly to this balanced bracket problem.
#
# 3. MATHEMATICAL EXPRESSION VALIDATION:
#    - In calculators or programming languages, mathematical expressions
#      like (a + b) * (c - d) must be validated before computation.
#
# 4. CODE EDITORS / IDEs:
#    - Text editors like VS Code or PyCharm use similar logic to highlight
#      matching brackets and help developers write correct code.
#
# ------------------------------------------------------------
