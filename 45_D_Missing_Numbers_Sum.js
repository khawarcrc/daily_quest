// Context:
// The company is trying to reconcile the expense records for a specific period. 
// Each expense has a unique ID, but two of these records were not saved properly in the system.

// Purpose:
// The missingNumbers function helps the company’s accounting team identify which expense records are missing, 
// so they can investigate and manually add the missing data.

// Output:
// The function returns the missing expense record IDs, allowing the company to quickly fix the discrepancies 
// in the financial records.

// For example, if the company's expense records range from 1 to 6 and the records with IDs 3 and 5 are missing, 
// the function will return [3, 5]. This helps the company maintain accurate financial data.


function missingNumbers(nums) {
    // Step 1: Calculate the total sum of numbers from 1 to nums.length + 2
    // nums.length + 2 because we are missing two numbers
    const total = (nums.length + 2) * (nums.length + 3) / 2;  // Formula for sum of first n numbers
    
    // Step 2: Subtract the actual numbers in the array nums from the total sum
    let sumOfNums = 0;
    for (let num of nums) {
        sumOfNums += num;
    }
    const remainingTotal = total - sumOfNums;

    // Step 3: Divide the remaining total (sum of two missing numbers) by 2
    const averageMissingValue = Math.floor(remainingTotal / 2);

    // Step 4: Initialize variables to store sums of numbers in two halves
    let foundFirstHalf = 0;
    let foundSecondHalf = 0;

    // Step 5: Iterate through the array and divide the numbers into two groups
    for (let num of nums) {
        if (num <= averageMissingValue) {
            foundFirstHalf += num;
        } else {
            foundSecondHalf += num;
        }
    }

    // Step 6: Calculate the expected sum for the first half (from 1 to averageMissingValue)
    const expectedFirstHalf = averageMissingValue * (averageMissingValue + 1) / 2;

    // Step 7: Calculate the expected sum for the second half (from averageMissingValue + 1 to nums.length + 2)
    const expectedSecondHalf = total - expectedFirstHalf;

    // Step 8: Return the difference between expected and found sums for each half, which gives the two missing numbers
    return [expectedFirstHalf - foundFirstHalf, expectedSecondHalf - foundSecondHalf];
}

// Real-world scenario: Finding missing expense records in the company's financial system
// Suppose the expense records range from 1 to 6, but two records are missing.
let expenseRecords = [1, 2, 4, 6];  // Missing expenses should be IDs 3 and 5
console.log(missingNumbers(expenseRecords));  // Output: [3, 5]

expenseRecords = [1, 3, 4, 5];  // Missing expenses should be IDs 2 and 6
console.log(missingNumbers(expenseRecords));  // Output: [2, 6]
