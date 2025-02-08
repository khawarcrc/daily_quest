# Problem Statement:
# You are given an undirected graph represented by a list of adjacency lists (edges).
# Your task is to determine if the graph can be colored with two colors such that no two adjacent nodes have the same color.
# If it is possible, return True; otherwise, return False.

# Explanation of the Problem:
# The graph is 2-colorable if its nodes can be divided into two sets where:
# 1. Every edge connects a node from one set to a node from the other set.
# 2. No two nodes within the same set share an edge.
# If the graph can be divided like this, it is called a bipartite graph.
# The problem asks you to check whether the graph is bipartite.

# Example 1:
# Graph 1: [[1, 2], [0, 2], [0, 1]] 
# This graph can be 2-colored, as it can be divided into two sets: {0, 2} and {1}, with no two adjacent nodes sharing the same color.

# Example 2:
# Graph 2: [[1], [0, 2], [1]] 
# This graph cannot be 2-colored, as there is an edge between two nodes in the same set (i.e., a cycle of odd length).

# Code Execution Theory:
# Start coloring the graph:
# Begin by coloring the first node with one color (say True).

# Traverse the graph:
# Use a graph traversal method (like Depth-First Search or DFS) to visit all the nodes.
# For each node, try to color its neighbors with the opposite color.

# Check for conflicts:
# If any two adjacent nodes have the same color, return False because the graph cannot be 2-colored.

# Return the result:
# If all nodes are colored without any conflicts, return True, indicating the graph is 2-colorable (bipartite).



def twoColorable(edges):
    # Initialize the color array with None, representing uncolored nodes
    # color[0] = True is assigned to the first node, indicating its color as True (can represent color 1)
    colors = [None for _ in range(len(edges))]
    colors[0] = True  # Start coloring node 0 with color True
    stack = [0]  # Stack for DFS-like traversal, starting with node 0

    # Continue processing until the stack is empty
    while len(stack) > 0:
        node = stack.pop()  # Pop a node from the stack to process it
        
        # Loop through all the connected nodes (adjacent nodes) of the current node
        for connection in edges[node]:
            # If the connected node is not yet colored, color it with the opposite color of the current node
            if colors[connection] is None:
                colors[connection] = not colors[node]  # Opposite color
                stack.append(connection)  # Add the connected node to the stack for further processing
            # If the connected node has the same color as the current node, the graph is not bipartite
            elif colors[connection] == colors[node]:
                return False  # Not 2-colorable

    # If all nodes are successfully colored with no conflicts, return True
    return True

# Example of a 2-colorable graph (Bipartite Graph)
# Nodes: 0, 1, 2
# Edges: 0-1, 1-2, 0-2 (this is a triangle, not bipartite)
graph1 = [[1, 2], [0, 2], [0, 1]]

# Example of a graph that is not 2-colorable
# Nodes: 0, 1, 2
# Edges: 0-1, 1-2, 2-0 (this forms a cycle of odd length, not bipartite)
graph2 = [[1], [0, 2], [1]]

print(twoColorable(graph1))  # Output: False (This graph cannot be 2-colored)
print(twoColorable(graph2))  # Output: False (This graph cannot be 2-colored)
