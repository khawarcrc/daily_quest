# Problem Statement:
# Write a function that takes in a two-dimensional array (matrix) of potentially varying sizes.
# Each element in the matrix represents a node in a graph and is either a 0 or a 1. 
# A "river" is a group of 1s connected horizontally or vertically (not diagonally).
# The function should return an array of the sizes of all rivers represented in the input matrix.

# Execution Theory:
# 1. Traverse each cell in the matrix. If it's a 1 and hasn't been visited, begin counting the size of the river.
# 2. Use depth-first search to explore all connected cells with value 1, marking each cell visited as part of the river.
# 3. Each time a new river is found, store its size and add it to the sizes list.
# 4. Return the list of river sizes at the end of traversal.

def riverSizes(matrix):
    sizes = []  # Store the sizes of each river
    visited = [[False for _ in row] for row in matrix]  # Track visited nodes
    
    # Traverse each cell in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Skip if the node is already visited
            if visited[i][j]:
                continue
            # Calculate river size if a new river is found
            traverseNode(i, j, matrix, visited, sizes)
    return sizes

def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0  # Initialize river size counter
    nodesToExplore = [[i, j]]  # Stack to explore nodes for current river depth first serach with stack
    
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()  # Get the current node
        i, j = currentNode
        
        # Skip if already visited
        if visited[i][j]:
            continue
        visited[i][j] = True  # Mark node as visited
        
        # Skip if current node is 0 (not part of a river)
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1  # Increment the size of the current river
        
        # Get unvisited neighbors and add them to the stack
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
    
    # Append the river size if a river was found
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)

def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []  # List to store unvisited neighbors
    
    # Check each possible direction (up, down, left, right)
    if i > 0 and not visited[i - 1][j]:  # Up
        unvisitedNeighbors.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:  # Down
        unvisitedNeighbors.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:  # Left
        unvisitedNeighbors.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:  # Right
        unvisitedNeighbors.append([i, j + 1])
        
    return unvisitedNeighbors

# Dummy data for testing
matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

# Example usage
print(riverSizes(matrix))  # Expected output: Sizes of rivers, e.g., [2, 1, 5, 2]



# Sample Matrix:
# matrix = [
#     [1, 0, 0, 1, 0],
#     [1, 0, 1, 0, 0],
#     [0, 0, 1, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 1, 1, 0]
# ]

# Execution Example:

# 1. Start with an empty list `sizes` to store sizes of rivers.
#    Create a `visited` matrix of the same dimensions as `matrix` with all values set to False.

# 2. Begin iterating over each cell in `matrix` using indices `i` (row) and `j` (column).
#    - Start with `i = 0` and `j = 0`.

# 3. At `matrix[0][0]`, the value is 1 and `visited[0][0]` is False:
#    - This indicates the start of a new river.
#    - Call `traverseNode(0, 0, matrix, visited, sizes)` to explore this river.

# 4. Inside `traverseNode` with `i = 0` and `j = 0`:
#    - Initialize `currentRiverSize = 0`.
#    - Start with `nodesToExplore = [[0, 0]]` (list of nodes to visit in this river).
    
# 5. Pop `[0, 0]` from `nodesToExplore` and mark `visited[0][0] = True`.
#    - Since `matrix[0][0] = 1`, this is part of the river, so increment `currentRiverSize` to 1.

# 6. Find unvisited neighbors of `[0, 0]`:
#    - `getUnvisitedNeighbors(0, 0, matrix, visited)` returns `[[1, 0]]`.
#    - Add `[1, 0]` to `nodesToExplore`.

# 7. Pop `[1, 0]` from `nodesToExplore` and mark `visited[1][0] = True`.
#    - Since `matrix[1][0] = 1`, increment `currentRiverSize` to 2.

# 8. Find unvisited neighbors of `[1, 0]`:
#    - `getUnvisitedNeighbors(1, 0, matrix, visited)` returns `[[0, 0], [3, 0]]` (skip `[0, 0]` as it's visited).
#    - Add `[3, 0]` to `nodesToExplore`.

# 9. Pop `[3, 0]` from `nodesToExplore`, mark `visited[3][0] = True`.
#    - Since `matrix[3][0] = 1`, increment `currentRiverSize` to 3.

# 10. Find unvisited neighbors of `[3, 0]`:
#     - `getUnvisitedNeighbors(3, 0, matrix, visited)` returns `[[4, 0]]`.
#     - Add `[4, 0]` to `nodesToExplore`.

# 11. Pop `[4, 0]` from `nodesToExplore`, mark `visited[4][0] = True`.
#     - Since `matrix[4][0] = 1`, increment `currentRiverSize` to 4.

# 12. Find unvisited neighbors of `[4, 0]`:
#     - `getUnvisitedNeighbors(4, 0, matrix, visited)` returns no new unvisited neighbors.

# 13. `nodesToExplore` is now empty, so add `currentRiverSize` (4) to `sizes`.

# 14. Return to the main loop in `riverSizes`, now at `i = 0`, `j = 1`:
#     - `matrix[0][1] = 0`, so skip as it’s not part of a river.

# 15. Continue to `matrix[0][3] = 1` and `visited[0][3] = False`:
#     - Start a new traversal with `traverseNode(0, 3, matrix, visited, sizes)`.

# 16. Repeat similar steps for each unvisited "1" in the matrix until all cells are processed.

# Final Output:
# After completing the matrix traversal, `sizes` will contain the sizes of all rivers in the matrix.
# Example: `sizes = [4, 1, 2, 2, 2]` representing sizes of each river found.
