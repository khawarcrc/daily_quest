// --------------------- Problem Statement ---------------------
// Given a staircase of 'height' steps and a maxSteps value,
// compute the number of distinct ways to reach the top by climbing
// 1 to maxSteps steps at a time.

// --------------------- Code Execution Theory ---------------------
// Initialize an array 'waysToTop' where each index i represents the
// number of ways to reach step i. We use a sliding window to keep track
// of the sum of the last 'maxSteps' entries.

// Time Complexity: O(n)
// Space Complexity: O(n)

function staircaseTraversal(height, maxSteps) {
    // waysToTop[0] = 1 (1 way to stay at the bottom)
    const waysToTop = [1]; 

    // Initialize running sum of the last maxSteps steps
    let currentNumberOfWays = 0;

    // Loop through all heights from 1 to final height
    for (let currentHeight = 1; currentHeight <= height; currentHeight++) {
        const startOfWindow = currentHeight - maxSteps - 1;
        const endOfWindow = currentHeight - 1;

        // Subtract the value that is sliding out of the window
        if (startOfWindow >= 0) {
            currentNumberOfWays -= waysToTop[startOfWindow];
        }

        // Add the new value into the window
        if (endOfWindow >= 0) {
            currentNumberOfWays += waysToTop[endOfWindow];
        }

        // Append total ways to reach currentHeight
        waysToTop.push(currentNumberOfWays);
    }

    // Return number of ways to reach the top step
    return waysToTop[height];
}

// --------------------- Dummy Test Case ---------------------

const height = 4;
const maxSteps = 2;

console.log("Number of ways to climb the staircase:", staircaseTraversal(height, maxSteps));

// Expected Output: 5
