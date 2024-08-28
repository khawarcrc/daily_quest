class BinaryTree:
    # Constructor to initialize the node with a value and set left and right children to None
    def __init__(self, value):
        self.value = value  # Assigns the given value to the node
        self.left = None    # Initially, the left child is set to None
        self.right = None   # Initially, the right child is set to None

def branchSums(root):
    # Function to calculate the sums of all branches in the binary tree
    # root -- the root node of the binary tree
    # Returns a list containing the sums of each branch
    sums = []  # Initialize an empty list to store the sums
    calculateBranchSums(root, 0, sums)  # Call the helper function to compute branch sums
    return sums  # Return the list of sums

def calculateBranchSums(node, runningSum, sums):
    # Helper function to calculate the sum of each branch and append it to the sums list
    # node -- the current node in the binary tree
    # runningSum -- the sum accumulated up to this node
    # sums -- list that stores the sum of each branch
    
    if node is None:  # Base case: if the node is None, return
        return
    
    newRunningSum = runningSum + node.value  # Update the running sum by adding the current node's value
    print(f"At node with value {node.value}, running sum is {newRunningSum}")  # Print current node and running sum
    
    if node.left is None and node.right is None:  # Check if the current node is a leaf
        sums.append(newRunningSum)  # Append the running sum to the list if it's a leaf node
        print(f"Leaf node found with value {node.value}, appending sum {newRunningSum} to sums")  # Print leaf node and sum
        return
    
    # Recursively call the function for the left and right children
    calculateBranchSums(node.left, newRunningSum, sums)  # Traverse left child
    calculateBranchSums(node.right, newRunningSum, sums)  # Traverse right child

# Dummy data for testing
root = BinaryTree(1)  # Create the root node with value 1
root.left = BinaryTree(2)  # Create left child of root with value 2
root.right = BinaryTree(3)  # Create right child of root with value 3
root.left.left = BinaryTree(4)  # Create left child of node 2 with value 4
root.left.right = BinaryTree(5)  # Create right child of node 2 with value 5
root.right.left = BinaryTree(6)  # Create left child of node 3 with value 6
root.right.right = BinaryTree(7)  # Create right child of node 3 with value 7

# The structure of the tree is:
#        1
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7

# Calculate the branch sums
sums = branchSums(root)  # Get the branch sums from the tree
print("Branch sums:", sums)  # Print the list of branch sums
