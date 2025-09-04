# ----------------------------------------------
# Problem Statement
# ----------------------------------------------
# You are given an expression in Reverse Polish Notation (RPN), 
# also known as Postfix Notation. 
# The task is to evaluate the expression and return the result.
#
# Reverse Polish Notation (RPN) is a mathematical notation 
# where every operator follows all of its operands.
#
# Example:
#   Input: ["2", "1", "+", "3", "*"]
#   Explanation:
#       Step 1: (2 + 1) = 3
#       Step 2: (3 * 3) = 9
#   Output: 9
#
# Key Rule:
#   - Numbers (operands) are pushed onto a stack.
#   - When an operator (+, -, *, /) is encountered, 
#     pop the top two numbers from the stack,
#     apply the operator, and push the result back to the stack.
#   - At the end, the stack will contain the final answer.
#
# ----------------------------------------------
# Code Execution Theory
# ----------------------------------------------
# 1. Initialize an empty stack.
# 2. Loop through each token in the input expression.
# 3. If the token is a number → push it onto the stack.
# 4. If the token is an operator (+, -, *, /):
#       - Pop two numbers from the stack.
#       - Apply the operation.
#       - Push the result back on the stack.
# 5. After processing all tokens, 
#    the stack will have one element (final answer).
# 6. Return this final result.

def reversePolishNotation(tokens): 
    # Initialize an empty stack to hold numbers during evaluation
    stack = [] 
    
    # Iterate over each token in the input list
    for token in tokens: 
        
        # If token is addition operator
        if token == "+": 
            # Pop last two numbers, add them, and push result back
            stack.append(stack.pop() + stack.pop())
            
        # If token is subtraction operator
        elif token == "-": 
            # Important: order matters in subtraction
            # First popped number is the right operand
            right = stack.pop()
            left = stack.pop()
            stack.append(left - right)
            
        # If token is multiplication operator
        elif token == "*": 
            # Multiply top two numbers and push back
            stack.append(stack.pop() * stack.pop())
            
        # If token is division operator
        elif token == "/": 
            # Order matters for division too
            right = stack.pop()
            left = stack.pop()
            # Using int() to truncate towards zero as per problem definition
            stack.append(int(left / right))
            
        # If token is a number (operand)
        else: 
            # Convert string to integer and push onto stack
            stack.append(int(token))
    
    # Final result is the only number left in the stack
    return stack.pop()


# ----------------------------------------------
# Dummy Data for Testing
# ----------------------------------------------

# Example 1:
tokens1 = ["2", "1", "+", "3", "*"]   # (2 + 1) * 3 = 9
print(reversePolishNotation(tokens1))  # Output: 9

# Example 2:
tokens2 = ["4", "13", "5", "/", "+"]  # 4 + (13 / 5) = 6
print(reversePolishNotation(tokens2))  # Output: 6

# Example 3:
tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# This is a complex expression, expected output = 22
print(reversePolishNotation(tokens3))  # Output: 22


# ----------------------------------------------
# Industry Equivalent Scenario
# ----------------------------------------------
# Reverse Polish Notation (RPN) evaluation has real-world use cases:
#
# 1. **Calculator Apps**:
#    Many calculators internally convert infix expressions (like 2 + 3 * 4)
#    into postfix (RPN) before evaluation because it avoids dealing with 
#    operator precedence and parentheses.
#
# 2. **Compilers and Interpreters**:
#    Programming languages often convert mathematical expressions into RPN 
#    during parsing to make evaluation efficient in the execution phase.
#
# 3. **Stack-Based Virtual Machines**:
#    Languages like Java (JVM bytecode) or Python's interpreter 
#    internally use stack-based evaluation, which is very similar to RPN.
#
# 4. **Financial Systems / Spreadsheets**:
#    When complex formulas are evaluated in financial software 
#    or spreadsheets, postfix evaluation can be used behind the scenes 
#    to ensure correct execution order.
#
# In short: RPN is widely used wherever expression evaluation is needed 
# without the overhead of managing parentheses and operator precedence rules.
