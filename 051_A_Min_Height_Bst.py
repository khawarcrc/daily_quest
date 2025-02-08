# Problem Statement:
# Given a sorted array, construct a Binary Search Tree (BST) with minimal height. 
# A BST is a binary tree where for each node, the value of the left subtree is less than the node's value,
# and the value of the right subtree is greater than or equal to the node's value.
# The task is to efficiently build a BST such that the resulting tree has the smallest possible height.

# How the Code Works Step-by-Step:
# - Initially, `minHeightBst` is called with the sorted array.
# - `constructMinHeightBst` is then called with the array and the indices of the entire array (from `0` to `len(array) - 1`).
# - The middle element of the array becomes the root of the tree, and the array is divided into two subarrays: 
#   the left half and the right half.
# - The middle element of the left half becomes the root of the left subtree, and the middle element of the right half 
#   becomes the root of the right subtree.
# - The recursion continues, further dividing the array until each subarray contains only one element or becomes empty.
# - For each subarray, a new node is created, and it is added to the correct position in the tree.
# - The `BST` class ensures that the values are inserted in the correct order: smaller values to the left, larger values to the right.
# - The recursion builds the tree level by level, starting from the middle of the array and working outward.
# - The resulting tree is balanced, meaning that it has the minimal possible height, because the middle element is always chosen 
#   as the root of each subtree, evenly dividing the elements between the left and right subtrees.
# - Once the entire array has been processed, the final BST is returned, with all elements inserted in their correct positions.

# Execution Theory:
# 1. `minHeightBst(array)` is called with a sorted array as input. 
#    This function acts as the entry point and calls the helper function `constructMinHeightBst` to begin constructing the BST.
# 2. `constructMinHeightBst` is a recursive function that selects the middle element of the current subarray, 
#    creates a new node for it, and recursively adds the remaining elements to the left and right subtrees.
# 3. The base case of the recursion is when the subarray is invalid (i.e., `startIdx > endIdx`), at which point the function returns.
# 4. The middle element of the array is used to create a new `BST` node. If the BST is not yet created, the middle element becomes the root.
#    Otherwise, the middle element is inserted into the existing BST using the `insert` method.
# 5. Once the middle element is inserted, the function recursively constructs the left subtree using the left half of the array
#    (from `startIdx` to `midIdx - 1`) and the right subtree using the right half (from `midIdx + 1` to `endIdx`).
# 6. This process continues recursively, each time selecting the middle element of the subarray, creating a node, and building
#    the left and right subtrees.
# 7. Eventually, all elements of the array are added to the BST, and the function returns the fully constructed tree.


# this code 

# Uses insert() Method: 
# The tree is constructed using the insert() method within the BST class, 
# which handles node placement and recursion internally.

# Abstract Recursion: 
# Recursion happens within the insert() method, so the recursive function 
# focuses only on selecting the middle element and calling insert().

# BST Structure Evolves Automatically: 
# The tree is built step by step as each element is inserted, 
# without manually updating references to left or right subtrees.



# Function to create a BST with minimal height from a sorted array
def minHeightBst(array):
    # Call the helper function to construct the BST and return the resulting tree
    return constructMinHeightBst(array, None, 0, len(array) - 1)


# Helper function to recursively construct a BST with minimal height
def constructMinHeightBst(array, bst, startIdx, endIdx):
    # Base case: if the subarray is invalid, return
    if endIdx < startIdx:
        return
    # Calculate the middle index of the current subarray
    midIdx = (startIdx + endIdx) // 2
    # Get the value at the middle index to add to the BST
    valueToAdd = array[midIdx]
    
    # If BST is not yet created, initialize it with the middle value
    if bst is None:
        bst = BST(valueToAdd)
    else:
        # Otherwise, insert the value into the existing BST
        bst.insert(valueToAdd)
    
    # Recursively build the left and right subtrees
    constructMinHeightBst(array, bst, startIdx, midIdx - 1)  # Left subtree
    constructMinHeightBst(array, bst, midIdx + 1, endIdx)    # Right subtree
    
    # Return the constructed BST
    return bst


# Class to represent a node in the Binary Search Tree (BST)
class BST:
    def __init__(self, value):
        # Initialize the node with the given value and set left and right children to None
        self.value = value
        self.left = None
        self.right = None

    # Method to insert a value into the BST
    def insert(self, value):
        # If the value to be inserted is less than the current node's value
        if value < self.value:
            # If left child is empty, insert the new value here
            if self.left is None:
                self.left = BST(value)
            else:
                # Otherwise, recursively insert it into the left subtree
                self.left.insert(value)
        else:
            # If the value is greater or equal, insert into the right subtree
            if self.right is None:
                self.right = BST(value)
            else:
                # Recursively insert it into the right subtree
                self.right.insert(value)


# Dummy data to test the function
# Sorted array
array = [1, 2, 5, 7, 10, 13, 14, 15, 22]

# Creating the minimal height BST from the sorted array
bst = minHeightBst(array)

# The resulting BST will have a balanced structure with minimal height
