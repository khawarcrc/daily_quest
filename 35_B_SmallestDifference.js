function smallestDifference(arrayOne, arrayTwo) {
  // Sort both arrays to facilitate comparison
  arrayOne.sort((a, b) => a - b);
  arrayTwo.sort((a, b) => a - b);

  // Initialize pointers for both arrays
  let indexOne = 0;
  let indexTwo = 0;

  // Variables to store the smallest difference and the current difference
  let smallest = null; // Smallest difference found so far
  let current = null; // Current difference between numbers being compared

  // Variable to store the pair with the smallest difference
  let smallestPair = [];

  // Iterate over both arrays as long as there are elements in both
  while (indexOne < arrayOne.length && indexTwo < arrayTwo.length) {
    let firstNumber = arrayOne[indexOne]; // Current number from the first array
    let secondNumber = arrayTwo[indexTwo]; // Current number from the second array

    // Calculate the difference between the two numbers
    if (firstNumber < secondNumber) {
      current = secondNumber - firstNumber;
      indexOne++; // Move pointer for the first array
    } else if (secondNumber < firstNumber) {
      current = firstNumber - secondNumber;
      indexTwo++; // Move pointer for the second array
    } else {
      // If both numbers are equal, the difference is 0, which is the smallest possible
      return [firstNumber, secondNumber];
    }

    // Update the smallest difference and the corresponding pair
    if (smallest > current) {
      smallest = current;
      smallestPair = [firstNumber, secondNumber];
    }
  }

  // Return the pair with the smallest difference
  return smallestPair;
}

// Dummy data to test the function
let arrayOne = [10, 20, 14, 16, 18];
let arrayTwo = [30, 23, 54, 33, 10];

// Call the function and print the result
let result = smallestDifference(arrayOne, arrayTwo);
console.log("The pair with the smallest difference is:", result);
