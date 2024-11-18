def cycleInGraph(edges):
    # Get the number of nodes in the graph
    numberOfNodes = len(edges)
    
    # Create lists to keep track of visited nodes and nodes currently in the stack
    visited = [False for _ in range(numberOfNodes)]
    currentlyInStack = [False for _ in range(numberOfNodes)]

    # Traverse each node to check for cycles
    for node in range(numberOfNodes):
        if visited[node]:
            print(f"Node {node} already visited, skipping.")
            continue  # Skip if node is already visited

        print(f"Starting DFS from node {node}.")
        # Check if there's a cycle starting from the current node
        containsCycle = isNodeInCycle(node, edges, visited, currentlyInStack)
        if containsCycle:
            print(f"Cycle detected starting from node {node}.")
            return True  # Return True if a cycle is detected

    print("No cycle found in the graph.")
    return False  # No cycle found


def isNodeInCycle(node, edges, visited, currentlyInStack):
    # Mark the current node as visited and add it to the stack
    visited[node] = True
    currentlyInStack[node] = True
    print(f"Visiting node {node}. Current state: visited={visited}, currentlyInStack={currentlyInStack}")

    # Get all the neighbors of the current node
    neighbors = edges[node]
    for neighbor in neighbors:
        print(f"Checking neighbor {neighbor} of node {node}.")
        if not visited[neighbor]:  # If neighbor hasn't been visited, visit it recursively
            print(f"Neighbor {neighbor} not visited, performing DFS.")
            containsCycle = isNodeInCycle(neighbor, edges, visited, currentlyInStack)
            if containsCycle:
                print(f"Cycle detected via neighbor {neighbor} of node {node}.")
                return True  # Return True if a cycle is detected
        elif currentlyInStack[neighbor]:  # If neighbor is in the stack, a cycle is found
            print(f"Cycle detected: neighbor {neighbor} of node {node} is already in the stack.")
            return True

    # Remove the node from the stack after exploring its neighbors
    currentlyInStack[node] = False
    print(f"Backtracking from node {node}. Current state: visited={visited}, currentlyInStack={currentlyInStack}")
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
print("Cycle detected?" ,cycleInGraph(edges))  # Output should be True, as there is a cycle in the graph
