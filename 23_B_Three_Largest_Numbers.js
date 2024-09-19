function findThreeLargestNumbers(array) {
  // Initialize an array to hold the three largest numbers, starting with null values
  let threeLargest = [null, null, null];

  // Iterate through each number in the input array
  for (let num of array) {
    // Update the three largest numbers as needed
    updateLargest(threeLargest, num);
  }

  // Return the final three largest numbers in ascending order
  return threeLargest;
}

function updateLargest(threeLargest, num) {
  // Check if the current number is larger than the largest (third) value in the array
  if (threeLargest[2] === null || num > threeLargest[2]) {
    // If so, shift the array and place the number in the largest (third) position
    shiftAndUpdate(threeLargest, num, 2);
  }
  // Otherwise, check if it's larger than the second largest number
  else if (threeLargest[1] === null || num > threeLargest[1]) {
    // If so, shift the array and place the number in the second position
    shiftAndUpdate(threeLargest, num, 1);
  }
  // Otherwise, check if it's larger than the third largest number
  else if (threeLargest[0] === null || num > threeLargest[0]) {
    // If so, shift the array and place the number in the first position
    shiftAndUpdate(threeLargest, num, 0);
  }
}

function shiftAndUpdate(array, num, index) {
  // This loop shifts the array elements to the left to make room for the new number
  for (let i = 0; i <= index; i++) {
    // When we reach the index, place the new number there
    if (i === index) {
      array[i] = num;
    }
    // Otherwise, shift the number to the left by copying the next element
    else {
      array[i] = array[i + 1];
    }
  }
}

// Dummy data for testing
// Example array: [10, 5, 9, 12, 8, 20, 2]
// Expected result: [10, 12, 20]
console.log(findThreeLargestNumbers([10, 5, 9, 12, 8, 20, 2])); // Output: [10, 12, 20]

// Another test case: [1, 5, 9, 3, 7]
// Expected result: [5, 7, 9]
console.log(findThreeLargestNumbers([1, 5, 9, 3, 7])); // Output: [5, 7, 9]
