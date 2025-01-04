// ------------------------------------------------------------
// PROBLEM STATEMENT:
// ------------------------------------------------------------
// You are given:
// - A string "number" that represents a sequence of digits (0-9).
// - An integer "numDigits" that tells how many digits you are allowed to remove.
//
// Task:
// - Remove exactly "numDigits" digits from the string such that
//   the resulting number (formed by the remaining digits) is the 
//   largest possible number in lexicographical/numerical order.
//
// Return:
// - The final number as a string after removing the digits.
//
// ------------------------------------------------------------
// EXPLANATION OF THE PROBLEM:
// ------------------------------------------------------------
// Think of it like this:
// - You have a number represented as a string, e.g. "462839".
// - You are allowed to delete some digits (numDigits times).
// - Each time, you want to remove digits that prevent the number from
//   being as large as possible.
//
// Example:
// number = "462839", numDigits = 2
// Possible results after removing 2 digits:
//   "4839", "6289", "6239", "4639" ...
// Among these, the largest is "6839".
//
// The algorithm ensures we always end up with the largest possible number.
//
// ------------------------------------------------------------
// THEORY OF EXECUTION:
// ------------------------------------------------------------
// - We will use a stack (array) to store digits step by step.
// - While traversing digits:
//   * If the current digit is larger than the last digit in the stack,
//     and we still have removals left (numDigits > 0), 
//     then pop (remove) from stack.
//   * This ensures that bigger digits are kept earlier, 
//     making the number as large as possible.
// - After traversing, if we still have removals left,
//   pop digits from the end (smallest influence on the final number).
// - Finally, join the stack into a string and return.
//
// ------------------------------------------------------------
// CODE WITH DETAILED COMMENTS + DEBUG PRINTS:
// ------------------------------------------------------------

function bestDigits(number, numDigits) {
    // Stack will hold the final digits that form the largest number
    let stack = [];
    console.log(`Initial number: ${number}, Digits to remove: ${numDigits}\n`);

    // Traverse each digit in the input number
    for (let digit of number) {
        console.log(`Processing digit: ${digit}`);

        // While we can still remove digits (numDigits > 0),
        // and the current digit is larger than the last digit in the stack,
        // remove (pop) the smaller digit to maximize number.
        while (numDigits > 0 && stack.length > 0 && digit > stack[stack.length - 1]) {
            let removed = stack.pop();   // Save removed digit
            numDigits -= 1;              // Use one removal
            console.log(`  -> Removed ${removed} from stack (remaining removals: ${numDigits})`);
        }

        // Push the current digit into the stack
        stack.push(digit);
        console.log(`  -> Stack after adding ${digit}: [${stack.join(", ")}]`);
    }

    // If we still have removals left after processing all digits,
    // remove digits from the end (least impact on making number large).
    while (numDigits > 0) {
        let removed = stack.pop();
        numDigits -= 1;
        console.log(`  -> Removed ${removed} from end (remaining removals: ${numDigits})`);
    }

    // Join stack digits into a single string to form the final number
    let result = stack.join("");
    console.log(`Resulting number: ${result}\n${"-".repeat(50)}\n`);
    return result;
}

// ------------------------------------------------------------
// DUMMY DATA (EXAMPLE TEST CASES):
// ------------------------------------------------------------

console.log(bestDigits("462839", 2));    // Expected "6839"
console.log(bestDigits("765028321", 5)); // Expected "88321"
console.log(bestDigits("123456", 3));    // Expected "456"
console.log(bestDigits("98765", 2));     // Expected "987"

// ------------------------------------------------------------
// REAL-TIME APPLICATION SCENARIO:
// ------------------------------------------------------------
// This problem is similar to "optimizing priority by elimination."
//
// Example in Industry:
// - Imagine an **e-commerce platform** ranking products for a user.
// - Each product has a "popularity score" (like digits in a number).
// - You can only recommend a limited set of products (like removing digits).
// - The algorithm decides which "less valuable" products to drop 
//   so that the remaining recommendations maximize user engagement.
//
// Another Example:
// - In **financial stock selection**, you may have performance scores of stocks.
// - You are allowed to drop some underperforming ones to keep 
//   the strongest sequence (maximize profit outlook).
