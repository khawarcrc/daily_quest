# Problem Statement:
# This code defines a Node class for representing nodes in a tree structure and includes a breadthFirstSearch method.
# The purpose of this method is to perform a breadth-first search (BFS) traversal on a tree, where each node may have multiple children.
# BFS ensures that nodes are visited level by level, starting from the root node.
# Given a root node, the BFS traversal will output a list of node names in the order they are visited.

# Code Execution Theory:
# - Node Creation: Each instance of the Node class represents a node in the tree, which can have multiple child nodes.
# - Adding Children: The addChild method allows each node to add children nodes by name, returning the current node for chaining multiple calls.
# - Breadth-First Search (BFS): The breadthFirstSearch method initializes a queue with the root node. It iteratively removes nodes from the front of the queue,
#   processes them by adding their name to a result array, and enqueues their children.
#   This continues until all nodes are processed, resulting in a list of node names in BFS order.



class Node:
    # Constructor to initialize the node with a name and empty list of children
    def __init__(self, name):
        self.children = []
        self.name = name

    # Method to add a child node by name
    def addChild(self, name):
        # Append a new Node object with the given name to the children list
        self.children.append(Node(name))
        return self  # Return self to allow method chaining

    # Method to perform breadth-first search and populate the array with node names
    def breadthFirstSearch(self, array):
        queue = [self]  # Initialize the queue with the root node
        while len(queue) > 0:  # Loop until the queue is empty
            current = queue.pop(0)  # Remove the first element from the queue
            array.append(current.name)  # Append the current node's name to the result array
            # Add all children of the current node to the queue for further exploration
            for child in current.children:
                queue.append(child)
        return array  # Return the array containing node names in BFS order

# Dummy data to test the breadthFirstSearch function
# Creating a root node and adding children
root = Node("A")
root.addChild("B").addChild("C").addChild("D")
root.children[0].addChild("E").addChild("F")
root.children[2].addChild("G").addChild("H")

# Performing breadth-first search on the tree and storing the result
result = root.breadthFirstSearch([])  # Expected order: ["A", "B", "C", "D", "E", "F", "G", "H"]

print(result)  # Output the BFS traversal order
