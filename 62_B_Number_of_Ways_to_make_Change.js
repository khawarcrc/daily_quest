function numberOfWaysToMakeChange(n, denoms) {
    // Create an array to store the number of ways to make change for each amount
    const ways = new Array(n + 1).fill(0);
    ways[0] = 1; // There is one way to make change for zero amount: use no coins

    console.log(`Initial ways array: ${ways}`);
    
    // Iterate through each denomination
    for (let denom of denoms) {
        console.log(`Using denomination: ${denom}`);
        // For each amount from 1 to n
        for (let amount = 1; amount <= n; amount++) {
            // If the denomination is less than or equal to the current amount
            if (denom <= amount) {
                // Update the ways to make change for the current amount
                ways[amount] += ways[amount - denom];
                console.log(`  For amount ${amount}: ways[${amount}] += ways[${amount} - ${denom}] => ${ways[amount]} (new value)`);
            }
        }
        console.log(`Ways array after processing denomination ${denom}: ${ways}`);
    }

    console.log(`Final ways array: ${ways}`);
    return ways[n]; // Return the number of ways to make change for amount n
}

// Dummy data
const n = 5; // Amount for which we need to make change
const denoms = [1, 2, 5]; // Denominations available

// Function execution with dummy data
const result = numberOfWaysToMakeChange(n, denoms);
console.log(`Number of ways to make change for ${n} using denominations ${denoms}: ${result}`);
