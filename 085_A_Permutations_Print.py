def getPermutations(array):
    """
    Generates all possible permutations of the given array.
    
    Args:
        array (list): The input array for which permutations need to be generated.
    
    Returns:
        list: A list containing all permutations of the input array.
    """
    # List to store all the permutations
    permutations = []
    print(f"Starting permutation generation for: {array}")
    # Call the helper function to generate permutations
    permutationsHelper(array, [], permutations)
    return permutations

def permutationsHelper(array, currentPermutation, permutations):
    """
    Recursive helper function to generate permutations.
    
    Args:
        array (list): Remaining elements to permute.
        currentPermutation (list): The current permutation being built.
        permutations (list): A list to store all the generated permutations.
    """
    print(f"Called with array={array}, currentPermutation={currentPermutation}")
    
    # Base case: If the array is empty and we have a current permutation
    if not array and currentPermutation:
        permutations.append(currentPermutation)
        print(f"Permutation complete: {currentPermutation}")
    else:
        # Iterate through each element in the array
        for i in range(len(array)):
            # Remove the current element and keep the rest in a new array
            newArray = array[:i] + array[i + 1:]
            # Add the current element to the ongoing permutation
            newPermutation = currentPermutation + [array[i]]
            
            print(f"Choosing element '{array[i]}' at index {i}: newArray={newArray}, newPermutation={newPermutation}")
            
            # Recursive call with the updated arrays
            permutationsHelper(newArray, newPermutation, permutations)
            
            print(f"Backtracking from element '{array[i]}' at index {i}")

# Example Input
input_array = [1, 2, 3]
result = getPermutations(input_array)
print("Final Permutations:", result)




            #                     []
            #                   / |  \
            #                 1   2   3        (Choose each element)
            #               /     |     \
            #            [1]    [2]   [3]      (Remaining array shrinks)
            #           /  \    /  \   /  \
            #        [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]  
            #        /      /      /     /      /     /
            #   [1,2,3] [1,3,2] [2,1,3][2,3,1][3,1,2][3,2,1]
