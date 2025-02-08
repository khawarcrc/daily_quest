# Problem Explanation
# Objective: Implement a depth-first search (DFS) algorithm for a tree structure.
# Conditions:
# - The tree is represented by nodes where each node can have multiple children.
# - Traverse the entire tree, starting from the root, and visit each node in a depth-first manner.

# Approach to Solve the Problem

# Step 1: Node Initialization
# - Create a Node class with a name and a list of children.
# - Implement methods to add children and perform depth-first search.

# Step 2: Add Children
# - Use the addChild method to add child nodes to a given parent node.

# Step 3: Depth-First Search (DFS)
# - Start DFS from the root node.
# - Traverse to each child node recursively, visiting nodes from top to bottom.
# - Append each visited node's name to an array to keep track of the traversal order.

# Step 4: Print and Return
# - Print the current state of the DFS array during traversal for debugging.
# - Print statements to indicate when a node is visited, when diving deeper into a child node, and when backtracking.
# - Return the final DFS array showing the order in which nodes were visited.


class Node: 
    def __init__(self, name): 
        # Initialize the node with a name and an empty list of children
        self.children = [] 
        self.name = name 
        
    def addChild(self, name): 
        # Add a new child node with the given name to the current node
        self.children.append(Node(name)) 
        
    def depthFirstSearch(self, array): 
        # Print statement to indicate the function has started executing for a specific node
        print(f"Visiting node: {self.name}")

        # Append the current node's name to the traversal array
        array.append(self.name)

        # Print the current state of the array
        print(f"Current DFS array: {array}")
        
        # Recursively call depthFirstSearch on all children
        for child in self.children:
            print(f"Going deeper into child: {child.name} of parent: {self.name}")
            child.depthFirstSearch(array)

        # Print statement to indicate backtracking from a node
        print(f"Backtracking from node: {self.name}")
        
        # Return the array after traversing all nodes
        return array 

# Creating a root node
root = Node("A")

# Adding children to the root node
root.addChild("B")
root.addChild("C")
root.addChild("D")

# Adding children to the "B" node
root.children[0].addChild("E")
root.children[0].addChild("F")

# Adding children to the "D" node
root.children[2].addChild("G")
root.children[2].addChild("H")

# Perform depth-first search starting from the root node
result = root.depthFirstSearch([])

# Print the final result of depth-first search
print(f"Final DFS result: {result}")
