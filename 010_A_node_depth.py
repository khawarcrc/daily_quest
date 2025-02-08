# function that calculates the sum of the depths of all nodes in the tree
# Initialize a stack with the root node at depth 0; use it for iterative DFS to calculate node depths.
# Pop nodes from the stack, adding their depths to a cumulative sum; skip if node is None.
# For each visited node, print its value, depth, and cumulative depth sum.
# Push left and right children of each node to the stack with an incremented depth.
# Use a stack to perform DFS iteratively, which allows handling large trees without recursion depth limits.
# Continue until all nodes are processed; return the total sum of all node depths.

class BinaryTree:
    # Represents a node in the binary tree with a given value and left/right children set to None initially.
    def __init__(self, value):
        self.value = value  # Assigns the given value to the node.
        self.left = None    # The left child is initially set to None.
        self.right = None   # The right child is initially set to None.

def nodeDepths(root): 
    # Initialize the sum of depths and the stack for iterative DFS
    sumOfDepths = 0  # To store the cumulative depth sum of all nodes
    stack = [{"node": root, "depth": 0}]  # Stack initialized with the root node at depth 0
    
    # Iterative traversal using a stack
    while len(stack) > 0: 
        # Pop the top element from the stack
        nodeInfo = stack.pop() 
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        
        # If the node is None, continue to the next iteration
        if node is None: 
            continue 
        
        # Add the depth of the current node to the total sum
        sumOfDepths += depth 
        print(f"Visiting node with value {node.value} at depth {depth}, cumulative sum of depths: {sumOfDepths}")
        
        # Add the left and right children to the stack with updated depths
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    
    # Return the total sum of depths after traversing all nodes
    return sumOfDepths     

# Create a binary tree for testing
root = BinaryTree(1)  # Create root node with value 1
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

# Calculate the sum of node depths
sumDepths = nodeDepths(root)  # Get the sum of all node depths
print("Sum of all node depths:", sumDepths)  # Print the sum of all node depths
