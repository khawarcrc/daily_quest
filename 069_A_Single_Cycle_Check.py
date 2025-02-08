# Problem Statement:
# Write a function  that takes in an array of integers where each element represents a "jump" of its value in the array.
# This function should determine whether starting at the first index and following the jumps results in a single cycle through all elements,
# meaning each element in the array is visited exactly once before returning to the starting position (index 0).
# If it's a single cycle, return True; otherwise, return False.

# Code Execution Theory:
# 1. Initialize `numElementsVisited` to count how many elements we've visited and `currentIdx` to track our position.
# 2. Begin a loop that continues until all elements in the array have been visited.
# 3. If we revisit the starting index (`currentIdx == 0`) before all elements are visited, return False because it’s not a valid single cycle.
# 4. Increment the number of elements visited and update `currentIdx` using the `getNextIdx` helper function.
# 5. The `getNextIdx` function computes the next index by adding the jump value (array[currentIdx]) to the current index, using modulus to keep the index within bounds.
# 6. After visiting all elements, check if we’re back at index 0. If so, return True (it’s a single cycle); otherwise, return False.


def hasSingleCycle(array):
    # Initialize the number of elements visited and the current index
    numElementsVisited = 0
    currentIdx = 0

    # Loop until the number of visited elements reaches the array's length
    while numElementsVisited < len(array):
        # If we revisit the start index before visiting all elements, it’s not a single cycle
        if numElementsVisited > 0 and currentIdx == 0:
            return False

        # Move to the next index according to the jump and increment the visit count
        numElementsVisited += 1
        currentIdx = getNextIdx(currentIdx, array)

    # Check if we returned to the starting index after visiting all elements
    return currentIdx == 0

def getNextIdx(currentIdx, array):
    # Calculate the next index based on the jump value at the current index
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)  # Use modulus to wrap around the array

    # Adjust the index for negative jumps to stay within bounds
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)

# Dummy Data
array = [2, 3, 1, -4, -4, 2]
print(hasSingleCycle(array))  # Expected output: True


# Execution Example for array = [2, 3, 1, -4, -4, 2]

# Initial setup:
# - `numElementsVisited = 0` to keep track of visited elements.
# - `currentIdx = 0` to start the traversal at index 0.

# Step 1:
# - `currentIdx = 0`
# - Jump value at index 0 is `2`.
# - Calculate the next index: `(0 + 2) % 6 = 2`.
# - Move to `currentIdx = 2`.
# - Increment `numElementsVisited = 1`.

# Step 2:
# - `currentIdx = 2`
# - Jump value at index 2 is `1`.
# - Calculate the next index: `(2 + 1) % 6 = 3`.
# - Move to `currentIdx = 3`.
# - Increment `numElementsVisited = 2`.

# Step 3:
# - `currentIdx = 3`
# - Jump value at index 3 is `-4`.
# - Calculate the next index: `(3 + (-4)) % 6 = 5`.
# - Move to `currentIdx = 5`.
# - Increment `numElementsVisited = 3`.

# Step 4:
# - `currentIdx = 5`
# - Jump value at index 5 is `2`.
# - Calculate the next index: `(5 + 2) % 6 = 1`.
# - Move to `currentIdx = 1`.
# - Increment `numElementsVisited = 4`.

# Step 5:
# - `currentIdx = 1`
# - Jump value at index 1 is `3`.
# - Calculate the next index: `(1 + 3) % 6 = 4`.
# - Move to `currentIdx = 4`.
# - Increment `numElementsVisited = 5`.

# Step 6:
# - `currentIdx = 4`
# - Jump value at index 4 is `-4`.
# - Calculate the next index: `(4 + (-4)) % 6 = 0`.
# - Move to `currentIdx = 0`.
# - Increment `numElementsVisited = 6`.

# End of Loop:
# - All elements have been visited (`numElementsVisited == len(array)`).
# - `currentIdx` is back at the start (index 0), confirming a single cycle.
# - The function returns `True` because a single cycle is confirmed.
