/**
 * Problem Statement:
 * The task is to generate all possible permutations of a given array of unique elements.
 * A permutation is a unique arrangement of the elements in the array where the order matters.
 * For example, for the input array [1, 2, 3], the possible permutations are:
 * [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].
 * 
 * Explanation of the Problem:
 * 1. A permutation is a rearrangement of the elements in an array in every possible order.
 * 2. The total number of permutations of an array with 'n' elements is n! (n factorial).
 *    For example, an array with 3 elements has 3! = 6 permutations.
 * 3. The solution involves recursively generating each permutation by selecting elements
 *    one by one and combining them in all possible ways until all permutations are created.
 * 
 * Code Execution Theory:
 * 1. The main function initializes an empty array to store the final permutations and 
 *    calls a recursive helper function to build permutations dynamically.
 * 
 * 2. The recursive helper function uses a backtracking approach:
 *    - If the length of the current permutation matches the input array length, it adds
 *      the permutation to the result array.
 *    - Otherwise, it iterates over the input array and tries to include each element
 *      in the current permutation:
 *        a. If the element is already used (tracked via a `used` array), it is skipped.
 *        b. Otherwise, the element is added to the ongoing permutation, and a recursive 
 *           call is made to generate the rest of the permutation.
 *        c. After the recursive call, the element is removed (backtracked), and its 
 *           "used" state is reverted to explore other possibilities.
 * 
 * 3. The backtracking approach ensures that every possible permutation is explored without 
 *    duplicating or skipping any.
 * 
 * 4. Once all recursive calls complete, the main function returns the array of all generated 
 *    permutations to the caller.
 * 
 * Time Complexity Analysis:
 * - The algorithm generates n! permutations for an array of size n.
 * - For each permutation, the helper function performs O(n) operations to build it.
 * - Overall time complexity: O(n * n!).
 * 
 * Space Complexity Analysis:
 * - Space complexity is O(n!) for storing the permutations.
 * - Additional space is used for the recursion stack, which has a depth of O(n).
 * - Overall space complexity: O(n + n!).
 */


/**
 * Generates all possible permutations of a given array.
 * 
 * @param {number[]} array - The input array for which permutations need to be generated.
 * @returns {number[][]} - A 2D array containing all permutations.
 */
function getPermutations(array) {
    const result = []; // Array to store all permutations

    /**
     * Backtracking helper function.
     * 
     * @param {number[]} currentPermutation - The current permutation being built.
     * @param {boolean[]} used - Array to track which elements are already used.
     */
    function backtrack(currentPermutation, used) {
        // Base case: If the permutation length matches the input array length
        if (currentPermutation.length === array.length) {
            result.push([...currentPermutation]); // Add a copy of the permutation to the result
            return;
        }

        // Iterate through each element in the array
        for (let i = 0; i < array.length; i++) {
            // Skip already used elements
            if (used[i]) continue;

            // Include the current element in the permutation
            currentPermutation.push(array[i]);
            used[i] = true;

            // Recursive call to build the next part of the permutation
            backtrack(currentPermutation, used);

            // Backtrack: Remove the last element and mark it as unused
            currentPermutation.pop();
            used[i] = false;
        }
    }

    backtrack([], new Array(array.length).fill(false)); // Initialize recursion
    return result; // Return the generated permutations
}

// Example usage
const inputArray = [1, 2, 3]; // Example input
const permutations = getPermutations(inputArray); // Generate permutations
console.log("Permutations:", permutations); // Display the permutations
