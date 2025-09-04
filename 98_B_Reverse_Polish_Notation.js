// ----------------------------------------------
// Problem Statement
// ----------------------------------------------
// You are given an expression in Reverse Polish Notation (RPN), 
// also known as Postfix Notation. 
// The task is to evaluate the expression and return the result.
//
// Reverse Polish Notation (RPN) is a mathematical notation 
// where every operator follows all of its operands.
//
// Example:
//   Input: ["2", "1", "+", "3", "*"]
//   Explanation:
//       Step 1: (2 + 1) = 3
//       Step 2: (3 * 3) = 9
//   Output: 9
//
// Key Rule:
//   - Numbers (operands) are pushed onto a stack.
//   - When an operator (+, -, *, /) is encountered, 
//     pop the top two numbers from the stack,
//     apply the operator, and push the result back to the stack.
//   - At the end, the stack will contain the final answer.
//
// ----------------------------------------------
// Code Execution Theory
// ----------------------------------------------
// 1. Initialize an empty stack.
// 2. Loop through each token in the input expression.
// 3. If the token is a number → push it onto the stack.
// 4. If the token is an operator (+, -, *, /):
//       - Pop two numbers from the stack.
//       - Apply the operation.
//       - Push the result back on the stack.
// 5. After processing all tokens, 
//    the stack will have one element (final answer).
// 6. Return this final result.

function reversePolishNotation(tokens) {
    // Initialize an empty stack to hold numbers during evaluation
    let stack = [];

    // Classic for loop to iterate over tokens
    for (let i = 0; i < tokens.length; i++) {
        let token = tokens[i];  // current token

        if (token === "+") {
            // Pop last two numbers, add them, and push result back
            stack.push(stack.pop() + stack.pop());

        } else if (token === "-") {
            // Subtraction (order matters)
            let right = stack.pop();
            let left = stack.pop();
            stack.push(left - right);

        } else if (token === "*") {
            // Multiplication
            stack.push(stack.pop() * stack.pop());

        } else if (token === "/") {
            // Division (order matters)
            let right = stack.pop();
            let left = stack.pop();
            // Truncate towards zero
            stack.push(Math.trunc(left / right));

        } else {
            // Convert string number to integer and push to stack
            stack.push(parseInt(token));
        }
    }

    // Final result will be the last element left in the stack
    return stack.pop();
}


// ----------------------------------------------
// Dummy Data for Testing
// ----------------------------------------------

let tokens1 = ["2", "1", "+", "3", "*"];   // (2 + 1) * 3 = 9
console.log(reversePolishNotation(tokens1));  // Output: 9

let tokens2 = ["4", "13", "5", "/", "+"];  // 4 + (13 / 5) = 6
console.log(reversePolishNotation(tokens2));  // Output: 6

let tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"];
// This is a complex expression, expected output = 22
console.log(reversePolishNotation(tokens3));  // Output: 22

