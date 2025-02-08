# Problem Statement:
# Given a directed graph represented as an adjacency list, determine if the graph contains a cycle.
# A cycle in a directed graph occurs when there exists a path that starts and ends at the same node.
# The function should return True if any cycle exists in the graph; otherwise, it should return False.

# Explanation:
# The graph is represented by an adjacency list `edges`, where each index represents a node, and each value at that index
# is a list of nodes to which the current node has direct edges. For example, `edges[0] = [1, 2]` means node 0 has directed
# edges to nodes 1 and 2.
#
# To detect a cycle, we perform a depth-first search (DFS) starting from each unvisited node. During this search, we use:
# - A `visited` list to mark nodes that have already been fully explored.
# - A `currentlyInStack` list to mark nodes that are part of the current DFS traversal path (or stack).
#
# If during the traversal we encounter a node that is already in the `currentlyInStack`, it indicates a back edge, meaning
# a cycle is detected (since we have returned to a node that is still in the current traversal path).
# If the DFS completes without encountering any back edges, then no cycle is detected starting from that node.

# Code Execution Theory:
# 1. Initialize two lists, `visited` and `currentlyInStack`, both of the same length as the number of nodes.
#    - `visited`: keeps track of all nodes that have been fully explored.
#    - `currentlyInStack`: marks nodes that are currently in the recursion stack of the DFS.
#
# 2. Iterate over each node in the graph.
#    - If a node is already marked as visited, skip it, as it has been processed and checked for cycles.
#    - If a node is unvisited, start a DFS from that node using the helper function `isNodeInCycle`.
#
# 3. Inside `isNodeInCycle`, mark the current node as visited and add it to the `currentlyInStack`.
#    - Explore each neighbor of the current node.
#      - If a neighbor hasn't been visited, recursively call `isNodeInCycle` on the neighbor.
#      - If `isNodeInCycle` on the neighbor returns True, it indicates a cycle, so we propagate True up the call stack.
#      - If a neighbor is already in `currentlyInStack`, it indicates a cycle, so return True immediately.
#
# 4. After exploring all neighbors, remove the current node from `currentlyInStack` to mark that the path exploration
#    from this node is complete and backtracking begins.
#
# 5. If the DFS completes for all nodes without detecting any cycles, the function returns False, indicating that no cycles exist.
#



def cycleInGraph(edges):
    # Get the number of nodes in the graph
    numberOfNodes = len(edges)
    
    # Create lists to keep track of visited nodes and nodes currently in the stack
    visited = [False for _ in range(numberOfNodes)]
    currentlyInStack = [False for _ in range(numberOfNodes)]

    # Traverse each node to check for cycles
    for node in range(numberOfNodes):
        if visited[node]:
            continue  # Skip if node is already visited

        # Check if there's a cycle starting from the current node
        containsCycle = isNodeInCycle(node, edges, visited, currentlyInStack)
        if containsCycle:
            return True  # Return True if a cycle is detected

    return False  # No cycle found


def isNodeInCycle(node, edges, visited, currentlyInStack):
    # Mark the current node as visited and add it to the stack
    visited[node] = True
    currentlyInStack[node] = True

    # Get all the neighbors of the current node
    neighbors = edges[node]
    for neighbor in neighbors:
        if not visited[neighbor]:  # If neighbor hasn't been visited, visit it recursively
            containsCycle = isNodeInCycle(neighbor, edges, visited, currentlyInStack)
            if containsCycle:
                return True  # Return True if a cycle is detected
        elif currentlyInStack[neighbor]:  # If neighbor is in the stack, a cycle is found
            return True

    # Remove the node from the stack after exploring its neighbors
    currentlyInStack[node] = False
    return False


# Sample input data representing a directed graph using adjacency list format
# Each index represents a node, and the list at each index represents the nodes it points to
edges = [
    [1, 2],    # Node 0 has edges to nodes 1 and 2
    [2],       # Node 1 has an edge to node 2
    [0, 3],    # Node 2 has edges to nodes 0 and 3, forming a cycle (0 -> 1 -> 2 -> 0)
    [4],       # Node 3 has an edge to node 4
    []         # Node 4 has no edges
]

# Test the function with the sample input
print(cycleInGraph(edges))  # Output should be True, as there is a cycle in the graph


# Example:
# For an input `edges = [[1, 2], [2], [0, 3], [4], []]`, the DFS will detect a cycle through nodes 0 -> 1 -> 2 -> 0,
# thus the function will return True.

# Example:
# Given:
# edges = [
#     [1, 2],    # Node 0 has edges to nodes 1 and 2
#     [2],       # Node 1 has an edge to node 2
#     [0, 3],    # Node 2 has edges to nodes 0 and 3, forming a cycle (0 -> 1 -> 2 -> 0)
#     [4],       # Node 3 has an edge to node 4
#     []         # Node 4 has no edges
# ]

# Graph Representation:
# Node 0 ----> Node 1
#   |            |
#   |            v
#   v          Node 2 ----> Node 3 ----> Node 4
# Node 2 <--------|
#
# Explanation:
# - This graph contains a cycle between nodes 0, 1, and 2.
# - Starting from node 0, we can follow the path 0 -> 1 -> 2 -> 0, forming a cycle.
# - Node 3 and node 4 do not participate in any cycle.
#
# Expected Output:
# The function will detect the cycle in nodes 0 -> 1 -> 2 -> 0 and return True.
