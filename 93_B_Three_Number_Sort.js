// Problem: Sort an array containing only 0s, 1s, and 2s in linear time and constant space.
// Function to sort an array containing only 0s, 1s, and 2s 
// This algorithm sorts the array in a single pass with O(n) time complexity and O(     1) space complexity.
// The function modifies the input array in place and returns the sorted array.                         
// Time Complexity: O(n)
// Space Complexity: O(1)   


function threeNumberSort(arr) {
  let low = 0;
  let mid = 0;
  let high = arr.length - 1;

  while (mid <= high) {
    if (arr[mid] === 0) {
      [arr[low], arr[mid]] = [arr[mid], arr[low]];
      low++;
      mid++;
    } else if (arr[mid] === 1) {
      mid++;
    } else {
      [arr[mid], arr[high]] = [arr[high], arr[mid]];
      high--;
    }
  }

  return arr;
}

// Example usage:
const arr = [0, 1, 0, 2, 1, 2, 0, 1, 2];
console.log(threeNumberSort(arr)); // Output: [0, 0, 0, 1, 1, 1, 2, 2, 2]


// Test cases
const assert = require('assert');       

