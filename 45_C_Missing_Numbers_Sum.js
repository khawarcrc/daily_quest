//  Context:
//  A teacher has a class with student IDs ranging from 1 to 20. However, due to various reasons, some students are absent, 
//  and their IDs are missing from the attendance list.

//  Purpose:
//  The teacher uses the missingNumbers function to determine which student IDs are missing from the enrolled list.
//  This helps the teacher identify which students were not present and might need to catch up on missed work.

//  Output:
//  The code outputs an array of missing student IDs, allowing the teacher to easily see which IDs were not accounted for.



function missingNumbers(nums) {
    // Convert the input array nums to a Set for faster lookup
    const includedNums = new Set(nums);

    // Initialize an empty array to store missing numbers
    const solution = [];

    // Use the maximum number in nums as the upper bound
    const maxNum = Math.max(...nums); // Get the maximum number from the input array
    console.log(`Max number: ${maxNum}`);

    // Iterate through numbers from 1 to the maximum number in the list
    for (let num = 1; num < maxNum; num++) {
        // If the current number is not in the Set of included numbers
        if (!includedNums.has(num)) {
            // Add it to the solution array as it's a missing number
            solution.push(num);
        }
    }

    // Return the array of missing numbers
    return solution;
}

// Real-world scenario: Finding missing student IDs in attendance
// Assume we have student IDs from 1 to 20, but some IDs are missing
const enrolledStudentIds = [1, 2, 4, 20]; // Example of enrolled student IDs
const missingStudentIds = missingNumbers(enrolledStudentIds);
console.log(`Missing student IDs: ${missingStudentIds}`); // Output should be [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
