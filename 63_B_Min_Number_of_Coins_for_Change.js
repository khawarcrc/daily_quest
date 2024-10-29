// Problem Statement:
// Given an integer `n` representing a target amount of money, and a list `denoms` representing
// the available denominations of coins, write a function that determines the minimum number
// of coins required to make up exactly `n` units. If it's not possible to make the target
// amount with the available denominations, return -1.

// Execution Theory:
// 1. We initialize an array, `numOfCoins`, where each index represents the minimum number of coins
//    required to reach that amount. Initially, all values are set to Infinity to represent
//    unachievable amounts.
// 2. We set `numOfCoins[0] = 0` as 0 coins are needed to make an amount of 0.
// 3. For each denomination, we iterate through `numOfCoins` starting from the value of the denomination.
// 4. For each amount that can be achieved by adding the current denomination, we update the
//    minimum number of coins required to reach that amount.
// 5. If the final amount `n` has not changed from Infinity, we return -1 as it is not achievable
//    with the available denominations; otherwise, we return `numOfCoins[n]`.

// Function to calculate minimum number of coins for change
function minNumberOfCoinsForChange(n, denoms) {
    // Initialize an array to store minimum coins required for each amount
    const numOfCoins = new Array(n + 1).fill(Infinity);
    numOfCoins[0] = 0; // Base case: no coins needed for amount 0

    // Loop through each denomination
    for (const denom of denoms) {
        // Loop through each amount from the denomination value up to n
        for (let amount = denom; amount <= n; amount++) {
            // Update minimum coins if the current denomination can be used
            numOfCoins[amount] = Math.min(numOfCoins[amount], numOfCoins[amount - denom] + 1);
        }
    }

    // Return result for amount n, or -1 if not achievable
    return numOfCoins[n] !== Infinity ? numOfCoins[n] : -1;
}

// Dummy data
const n = 7; // Target amount
const denoms = [1, 5, 10]; // Available denominations

// Calling the function with dummy data
console.log(minNumberOfCoinsForChange(n, denoms)); // Expected output: 3 (as 7 = 5 + 1 + 1)

