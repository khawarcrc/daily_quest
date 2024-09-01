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
