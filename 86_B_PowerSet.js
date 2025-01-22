/*
Explanation of the code:

1. The function `powerset` computes the powerset of the input array.
   - The powerset is the set of all subsets of the given array, including the empty subset and the array itself.

2. The `reduce` method is used to build the powerset step by step:
   - `subsets` is the accumulator, which starts with `[[]]` (the empty subset).
   - For each `element` in the array, new subsets are created by adding the element to each subset already in `subsets`.
   - These new subsets are then concatenated to the existing subsets.

3. The `subsets.map(subset => [...subset, element])`:
   - Creates a new subset by appending the current element to each subset.
   - `...subset` ensures a new array is created for immutability.

4. The `concat` method:
   - Combines the original subsets with the new subsets created in the current iteration.

5. The final result is the complete powerset of the input array.
*/


function powerset(array) {
    // Use the reduce method to build the powerset
    return array.reduce(
        (subsets, element) => 
            // For each element, concatenate the existing subsets with new subsets
            // formed by adding the current element to each subset
            subsets.concat(subsets.map(subset => [...subset, element])),
        // Start with an initial array containing the empty subset
        [[]]
    );
}

// Dummy data for testing the function
const inputArray = [1, 2, 3];

// Call the function and print the powerset of the input array
console.log(powerset(inputArray));

