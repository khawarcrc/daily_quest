def minHeightBst(array):
    return constructMinHeightBst(array, None, 0, len(array) - 1)


def constructMinHeightBst(array, bst, startIdx, endIdx):
    # Base case: if end index is less than start index, stop the recursion
    if endIdx < startIdx:
        return

    midIdx = (startIdx + endIdx) // 2
    bst = BST(array[midIdx])
    bst.left = constructMinHeightBst(array, startIdx, midIdx - 1)
    bst.right = constructMinHeightBst(array, midIdx + 1, endIdx)
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
