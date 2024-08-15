function nonConstructibleChange(coins) {
    // Sort the coins array to process them in ascending order
    coins.sort(function(a, b) {
        return a - b;
    });

    // Initialize a variable to track the current change that can be created
    let currentChangeCreated = 0;

    // Iterate through each coin in the sorted list using a basic for loop
    for (let i = 0; i < coins.length; i++) {
        let coin = coins[i];

        // If the current coin is greater than the current change + 1, 
        // we can't create the next change value, so return it.
        if (coin > currentChangeCreated + 1) {
            console.log(`Cannot create change for ${currentChangeCreated + 1}`);
            return currentChangeCreated + 1;
        }

        // Otherwise, add the current coin to the current change value
        currentChangeCreated += coin;

        // Debugging: Print the current state
        console.log(`Coin: ${coin}, Current Change Created: ${currentChangeCreated}`);
    }

    // If all coins have been used, return the next change that can't be created
    console.log(`All changes up to ${currentChangeCreated} can be created.`);
    return currentChangeCreated + 1;
}

// Demo example
let coins = [1, 1, 3, 4, 9];
console.log("Coins:", coins);
let result = nonConstructibleChange(coins);
console.log(`Minimum change that cannot be created: ${result}`);



// Sort the coins array to ensure coins are processed in ascending order.
// Initialize a variable to track the smallest change that can be created.
// Iterate through each coin and check if it can create the next smallest change.
// If a coin can't create the next smallest change, return that change as the result.
// If all coins are used, return the next smallest change that can't be created.