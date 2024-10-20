# """
# Problem Statement:
# Given a Binary Search Tree (BST), write a function to find the Kth largest value in the BST.

# A Binary Search Tree (BST) is defined such that for each node:
# - All values in the left subtree are less than the node's value.
# - All values in the right subtree are greater than the node's value.

# In this problem, we need to identify the Kth largest value in the BST. The largest value is considered the highest node value, and we want to find the value that is the Kth largest.

# Theory:
# 1. **Reverse In-Order Traversal:**
#    - To find the Kth largest value, we can perform a reverse in-order traversal of the BST. This traversal visits the nodes in descending order (right, root, left).
#    - As we visit nodes in this order, the largest values are processed first, allowing us to keep track of how many nodes we've visited.

# 2. **Tracking Visited Nodes:**
#    - We can maintain a count of the number of nodes visited during the traversal using a helper class or structure (e.g., `TreeInfo`).
#    - This structure will store:
#      - The number of nodes visited so far.
#      - The value of the most recently visited node.

# 3. **Finding the Kth Largest Value:**
#    - As we perform the reverse in-order traversal, we increment our count each time we visit a node.
#    - When our count reaches K, we record the current node's value as the Kth largest value.

# 4. **Time and Space Complexity:**
#    - The time complexity for the reverse in-order traversal is O(n), where n is the number of nodes in the tree, as we may visit each node once.
#    - The space complexity is O(h), where h is the height of the tree, due to the call stack used for recursion.

# By following this approach, we can efficiently find the Kth largest value in a given Binary Search Tree.
# """


class BST:
    def __init__(self, value, left=None, right=None):
        # Initialize a Binary Search Tree node with a value and optional left and right children
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, numberOfNodesVisited, latestVisitedNodeValue):
        # Initialize TreeInfo to keep track of the number of nodes visited and the latest visited node value
        self.numberOfNodesVisited = numberOfNodesVisited
        self.latestVisitedNodeValue = latestVisitedNodeValue


def findKthLargestValueInBst(tree, k):
    # Create an instance of TreeInfo to track the number of nodes visited and the latest visited node value
    treeInfo = TreeInfo(0, -1)
    
    # Perform reverse in-order traversal of the BST
    reverseInOrderTraverse(tree, k, treeInfo)
    
    # Return the latest visited node value which corresponds to the Kth largest value
    return treeInfo.latestVisitedNodeValue


def reverseInOrderTraverse(node, k, treeInfo):
    # Base case: if the node is None or if we've already visited K nodes, return
    if node is None or treeInfo.numberOfNodesVisited >= k:
        return

    # Traverse the right subtree first (to get the largest values first)
    reverseInOrderTraverse(node.right, k, treeInfo)
    
    # If we haven't visited K nodes yet, visit this node
    if treeInfo.numberOfNodesVisited < k:
        treeInfo.numberOfNodesVisited += 1  # Increment the count of visited nodes
        treeInfo.latestVisitedNodeValue = node.value  # Update the latest visited node value
        print(f"Visited Node: {node.value}, Nodes Visited: {treeInfo.numberOfNodesVisited}")  # Print for understanding

        # Traverse the left subtree
        reverseInOrderTraverse(node.left, k, treeInfo)


# Dummy data to create a sample BST
# Example BST:
#         10
#        /  \
#       5   15
#      / \    \
#     2   5   20

root = BST(10)
root.left = BST(5)
root.right = BST(15)
root.left.left = BST(2)
root.left.right = BST(5)
root.right.right = BST(20)

# Specify the value of k to find the Kth largest value
k = 2

# Print the result
print(f"The {k}th largest value in the BST is: {findKthLargestValueInBst(root, k)}")

# To understand the execution, we will see the print statements as we visit nodes
