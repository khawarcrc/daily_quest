/*
 * Problem Statement:
 * Given an array of integers, the task is to find the first duplicate value 
 * in the array. A duplicate value is defined as a number that appears more 
 * than once in the array. The function should return the first duplicate 
 * value that is encountered as we traverse the array from left to right. 
 * If no duplicate values are found, the function should return -1.
 *
 * Example:
 * Input: [5, 3, 4, 5, 2, 2, 3, 1]
 * Output: 5
 *
 * Steps to Solve the Problem:
 * 1. Initialize an empty object to store the first occurrence index of each element.
 * 2. Loop through each element in the array using a for loop.
 * 3. For each element:
 *    a. Check if the element already exists in the object (indicating it's a duplicate).
 *    b. If it exists, log the duplicate found and return the element.
 *    c. If it doesn't exist, store the element in the object with its index.
 * 4. If the loop completes without finding any duplicates, log that no duplicates were found.
 * 5. Return -1 to indicate that there are no duplicates in the array.
 */


function firstDuplicateValue(array) {
  // Object to store the first occurrence index of each element
  const seen = {};
  console.log("Initial array:", array);

  // Loop through the array
  for (let i = 0; i < array.length; i++) {
    const value = array[i];
    console.log(`Checking value: ${value} at index: ${i}`);

    // If value is already in the object, it's a duplicate
    if (seen[value]) {
      console.log(`Duplicate found: ${value}`);
      return value; // Return the duplicate value
    }

    // Otherwise, store the index of the first occurrence
    seen[value] = i;
    console.log(`Storing ${value} in seen at index ${i}`);
    console.log(`Current seen object:`, seen);
  }

  // If no duplicate is found, return -1
  console.log("No duplicates found.");
  return -1;
}

// Dummy data for testing
const testArray = [5, 3, 4, 5, 2, 2, 3, 1];
console.log("First duplicate value:", firstDuplicateValue(testArray)); // Output will be 5
