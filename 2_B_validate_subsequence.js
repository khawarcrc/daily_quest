function validateSubsequence(array, sequence) {
  // Initialize two indices to keep track of positions in array and sequence
  let arrIdx = 0;
  let seqIdx = 0;
  // const matchedElements = [];
  // Loop through the array and sequence until the end of either is reached
  while (arrIdx < array.length && seqIdx < sequence.length) {
    // If the current element in the array matches the current element in the sequence
    if (array[arrIdx] === sequence[seqIdx]) {
      // matchedElements.push(array[arrIdx]);
      // Move to the next element in the sequence
      seqIdx++;
    }
    // Move to the next element in the array
    arrIdx++;
  }

  // Return true if the entire sequence has been found in the array in order, otherwise false
  return seqIdx === sequence.length;
  // return seqIdx === sequence.length ? matchedElements : [];
}

// Sample test case
const array = [5, 1, 22, 25, 6, 7, 8, 10];
const sequence = [1, 6, 8, 10];

// Validate subsequence
console.log(validateSubsequence(array, sequence)); // Should return true
