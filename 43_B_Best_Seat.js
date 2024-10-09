function bestSeat(seats) {
  // Initialize the variable to store the index of the best seat, -1 means no best seat found initially
  let bestSeat = -1;
  // Initialize maxSpace to 0, which keeps track of the largest segment of empty seats
  let maxSpace = 0;

  // Initialize left pointer to 0, which will scan the row from left to right
  let left = 0;

  // Loop through the seating arrangement
  while (left < seats.length) {
    // Initialize the right pointer to one seat ahead of the left pointer
    let right = left + 1;

    // Move the right pointer to the end of a segment of consecutive empty seats (0s)
    while (right < seats.length && seats[right] === 0) {
      right++;
    }

    // Calculate the number of empty seats between two occupied seats (left and right pointers)
    const availableSpace = right - left - 1;

    // If the available empty space is larger than the previously recorded max space
    if (availableSpace > maxSpace) {
      // Update the bestSeat to be the middle seat in the current empty segment
      bestSeat = Math.floor((left + right) / 2);
      // Update the maxSpace to the size of the current segment
      maxSpace = availableSpace;
    }

    // Move the left pointer to the current right position to continue the search
    left = right;
  }

  // Return the index of the best seat found, or -1 if no empty seat exists
  return bestSeat;
}

// Dummy data
const seats = [1, 0, 0, 0, 1, 0, 0, 1];
console.log("Best seat is at index:", bestSeat(seats)); // Output: 2 (middle of the longest empty segment [0, 0, 0])
