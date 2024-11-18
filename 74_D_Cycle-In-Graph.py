# Problem Statement:
# ------------------
# Write a function that detects whether a directed graph contains a cycle. 
# The graph is represented as an adjacency list, where each index represents a node, 
# and the values at each index represent the nodes it points to (edges).
# A cycle is a path in the graph that starts and ends at the same node.

# Code Execution Theory:
# -----------------------
# - We use a color-coding method to track the state of each node during a depth-first search (DFS).
#   WHITE (0) -> Node is unvisited.
#   GREY (1) -> Node is being visited (currently in the recursion stack).
#   BLACK (2) -> Node has been completely visited.
# - As we traverse the graph:
#   1. If we encounter a node that is GREY, it means we've returned to a node currently in the stack, indicating a cycle.
#   2. If a node is BLACK, it's already processed, and we skip it.
#   3. At the end of visiting all neighbors of a node, we mark it BLACK.
# - If any traversal detects a cycle, the function returns True. Otherwise, it returns False.

# Code:
# -----
WHITE, GREY, BLACK = 0, 1, 2  # Constants to represent node states


def cycleInGraph(edges):
    """
    Determines if a directed graph contains a cycle.

    Args:
    - edges: List of lists where edges[i] contains nodes that the i-th node points to.

    Returns:
    - True if the graph contains a cycle, False otherwise.
    """
    # Number of nodes in the graph
    numberOfNodes = len(edges)
    # Initialize all nodes as WHITE (unvisited)
    colors = [WHITE for _ in range(numberOfNodes)]

    # Traverse each node in the graph
    for node in range(numberOfNodes):
        # Skip already visited nodes
        if colors[node] != WHITE:
            continue

        # Perform DFS to detect a cycle
        containsCycle = traverseAndColorNodes(node, edges, colors)
        if containsCycle:
            return True  # Cycle detected

    return False  # No cycle detected


def traverseAndColorNodes(node, edges, colors):
    """
    Helper function to perform DFS and color nodes.

    Args:
    - node: The current node being visited.
    - edges: The adjacency list of the graph.
    - colors: List representing the state of each node.

    Returns:
    - True if a cycle is detected, False otherwise.
    """
    # Mark the node as being visited (GREY)
    colors[node] = GREY

    # Get all neighbors of the current node
    neighbors = edges[node]
    for neighbor in neighbors:
        neighborColor = colors[neighbor]

        # If the neighbor is GREY, a cycle is detected
        if neighborColor == GREY:
            return True

        # If the neighbor is BLACK, skip it
        if neighborColor == BLACK:
            continue

        # Recur on the neighbor
        containsCycle = traverseAndColorNodes(neighbor, edges, colors)
        if containsCycle:
            return True

    # Mark the node as completely visited (BLACK)
    colors[node] = BLACK
    return False


# Dummy Data:
# ---------
# Graph represented as an adjacency list:
# Node 0 points to node 1
# Node 1 points to node 2
# Node 2 points to node 0 (Cycle exists)
# Node 3 points to node 4
edges = [
    [1],     # Node 0 points to 1
    [2],     # Node 1 points to 2
    [0],     # Node 2 points to 0 (creates a cycle)
    [4],     # Node 3 points to 4
    []       # Node 4 points to no one
]

# Detect if the graph has a cycle
print(cycleInGraph(edges))  # Expected Output: True (cycle exists)
