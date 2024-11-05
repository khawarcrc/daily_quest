/**
 * Determines whether the jumps in the array form a single cycle, meaning each element in the array
 * is visited exactly once before returning to the starting position (index 0).
 
 */
function hasSingleCycle(array) {
  // Handle edge case where the array is empty or has only one element
  if (array.length === 0) return false;
  if (array.length === 1) return array[0] === 0;

  let numElementsVisited = 0;
  let currentIdx = 0;

  // Continue looping until all elements are visited
  while (numElementsVisited < array.length) {
    // If we return to the start index before all elements are visited, it's not a single cycle
    if (numElementsVisited > 0 && currentIdx === 0) {
      return false;
    }

    // Increment the count of visited elements and update the current index
    numElementsVisited++;
    currentIdx = getNextIdx(currentIdx, array);
  }

  // Check if we ended up back at the starting index
  return currentIdx === 0;
}

/**
 * Computes the next index in the array based on the jump value at the current index.
 * Wraps around the array if necessary using modular arithmetic.

 */
function getNextIdx(currentIdx, array) {
  const jump = array[currentIdx];
  const nextIdx = (currentIdx + jump) % array.length;

  // Ensure the next index is positive (handle wrap-around for negative indices)
  return nextIdx >= 0 ? nextIdx : nextIdx + array.length;
}

// Dummy Data
const array = [2, 3, 1, -4, -4, 2];
console.log(hasSingleCycle(array)); // Expected output: true
