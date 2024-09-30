function threeNumberSum(array, targetSum) {
  //  Sort the input array for proper pointer movement
  array.sort((a, b) => a - b);

  //  Initialize an empty array to store the triplets
  const triplets = [];

  //  Loop through the array, leaving out the last two elements for the pointers
  for (let i = 0; i < array.length - 2; i++) {
    // Initialize the left pointer to the element next to i
    let left = i + 1;
    // Initialize the right pointer to the last element of the array
    let right = array.length - 1;

    //  Use a while loop to move the left and right pointers
    while (left < right) {
      // Calculate the sum of the three elements
      const currentSum = array[i] + array[left] + array[right];

      //  Check if the current sum is equal to the target sum
      if (currentSum === targetSum) {
        // If a valid triplet is found, add it to the triplets array
        triplets.push([array[i], array[left], array[right]]);
        // Move both pointers inward to check for other potential triplets
        left++;
        right--;
      }
      //  If the current sum is less than the target, increment the left pointer
      else if (currentSum < targetSum) {
        left++;
      }
      //  If the current sum is greater than the target, decrement the right pointer
      else {
        right--;
      }
    }
  }

  //  Return the array of triplets that sum to the target value
  return triplets;
}

// Test the function with a sample array and target sum
const array = [12, 3, 1, 2, -6, 5, -8, 6];
const targetSum = 0;
const result = threeNumberSum(array, targetSum);

console.log(result); // Expected output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
