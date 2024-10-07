// Problem Statement:
// A business wants to evaluate the performance of its sales team. 
// Each team member's sales figures are stored in an array. 
// The goal is to calculate how much sales each team member contributes 
// to the overall sales without including their own sales figures. 
// This information will help in setting team goals and bonuses.

// Steps to Solve the Problem:
// 1. Initialize an array 'contributions' of the same length as 'sales', 
//    filled with initial values (e.g., 0 or 1).
//
// 2. Initialize a variable 'leftRunningTotal' to hold the cumulative 
//    sales of all team members to the left of the current index. Set it to 0.
//
// 3. Loop through the 'sales' array from left to right:
//    - For each index 'i', set 'contributions[i]' to 'leftRunningTotal', 
//      which represents the total sales of all team members to the left of 'i'.
//    - Update 'leftRunningTotal' by adding the current team member's sales figure.
//
// 4. Initialize a variable 'rightRunningTotal' to hold the cumulative 
//    sales of all team members to the right of the current index. Set it to 0.
//
// 5. Loop through the 'sales' array from right to left:
//    - For each index 'i', add 'rightRunningTotal' to 'contributions[i]', 
//      which now represents the total sales excluding the current team member's sales.
//    - Update 'rightRunningTotal' by adding the current team member's sales figure.
//
// 6. Return the 'contributions' array containing the total sales contribution 
//    of each team member excluding their own sales figures.


function salesContributionExcludingSelf(sales) {
    // Initialize an array 'contributions' of the same length as 'sales', filled with 1s
    const contributions = new Array(sales.length).fill(1);

    // Initialize leftRunningTotal to hold the cumulative sales of all members to the left
    let leftRunningTotal = 1;
    
    // First loop: Go through each sales figure from left to right
    for (let i = 0; i < sales.length; i++) {
        // Set the current 'contributions[i]' to leftRunningTotal (cumulative sales to the left of i)
        contributions[i] = leftRunningTotal;

        // Update leftRunningTotal by adding the current sales figure in 'sales'
        leftRunningTotal += sales[i];
    }

    // Initialize rightRunningTotal to hold the cumulative sales of all members to the right
    let rightRunningTotal = 0;
    
    // Second loop: Go through each sales figure from right to left (reversed order)
    for (let i = sales.length - 1; i >= 0; i--) {
        // Add the rightRunningTotal to contributions[i] (cumulative sales to the right of i)
        contributions[i] += rightRunningTotal;

        // Update rightRunningTotal by adding the current sales figure in 'sales'
        rightRunningTotal += sales[i];
    }

    // Return the final 'contributions' array containing the result
    return contributions;
}

// Dummy data to test the function
const sales = [100, 200, 300, 400];

// Call the function and print the final result
const result = salesContributionExcludingSelf(sales);
console.log(`\nTotal sales contribution excluding self: ${result}`);
