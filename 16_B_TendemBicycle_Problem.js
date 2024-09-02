function tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) {
    // Sort both speed arrays in ascending order
    redShirtSpeeds.sort((a, b) => a - b);
    blueShirtSpeeds.sort((a, b) => a - b);

    console.log(`Sorted red shirt speeds: ${redShirtSpeeds}`);
    console.log(`Sorted blue shirt speeds: ${blueShirtSpeeds}`);

    // If we're not looking for the fastest possible outcome,
    // reverse the redShirtSpeeds array to pair the slowest red shirt rider
    // with the fastest blue shirt rider to minimize speed.
    if (!fastest) {
        reverseArrayInPlace(redShirtSpeeds);
        console.log(`Reversed red shirt speeds for slowest total speed: ${redShirtSpeeds}`);
    }

    let totalSpeed = 0;

    // Calculate total speed by selecting the maximum speed for each pair
    for (let idx = 0; idx < redShirtSpeeds.length; idx++) {
        const rider1 = redShirtSpeeds[idx];
        const rider2 = blueShirtSpeeds[blueShirtSpeeds.length - idx - 1]; // Pairing the fastest available blue rider with red rider

        // Print current rider speeds for debugging
        console.log(`Pair ${idx + 1}: Red shirt rider speed = ${rider1}, Blue shirt rider speed = ${rider2}`);

        totalSpeed += Math.max(rider1, rider2); // Add the maximum speed of the two riders in each pair
    }

    // Print the total speed calculated
    console.log(`Total speed: ${totalSpeed}`);
    
    return totalSpeed;
}

function reverseArrayInPlace(array) {
    // Reverses the given array in place
    let start = 0;
    let end = array.length - 1;
    while (start < end) {
        const temp = array[start];
        array[start] = array[end];
        array[end] = temp;
        start++;
        end--;
    }
}

// Test the function with sample data
const redShirtSpeeds = [5, 5, 3, 9, 2];
const blueShirtSpeeds = [3, 6, 7, 2, 1];

// Example of fastest possible speed
console.log("Calculating fastest possible total speed:");
let fastest = true;
console.log(`Maximum total speed: ${tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)}\n`);

// Example of slowest possible speed
console.log("Calculating slowest possible total speed:");
fastest = false;
console.log(`Minimum total speed: ${tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)}`);

// Time Complexity:
// The overall time complexity of the function is O(n log n) due to the sorting step,
// which dominates the O(n) time complexity of the pairing step.
