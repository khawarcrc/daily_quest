# """
#     PROBLEM STATEMENT:
#     ------------------
#     Write a function that takes a 2D array (matrix) and returns a 1D array
#     of its elements in zigzag order.

#     Zigzag order means:
#     - Start at top-left corner (0,0)
#     - Move DOWN first
#     - Then move diagonally:
#         ↗ (up-right)
#         ↙ (down-left)
#     - Keep switching directions when hitting boundaries
#     - Continue until all elements are visited

#     -----------------------------------------------------

#     EXECUTION THEORY:
#     ------------------
#     We simulate movement inside the matrix using:

#     1. Two pointers:
#         - row → current row index
#         - col → current column index

#     2. Direction flag:
#         - goingDown = True  → moving down-left (↙)
#         - goingDown = False → moving up-right (↗)

#     -----------------------------------------------------

#     MOVEMENT RULES:

#     If goingDown (↙):
#         - Normal move:
#             row += 1
#             col -= 1

#         - Boundary cases:
#             if at LEFT wall (col == 0)
#             OR at BOTTOM wall (row == height):
#                 → switch direction (goingDown = False)

#                 if at bottom:
#                     move RIGHT (col += 1)
#                 else:
#                     move DOWN (row += 1)

#     -----------------------------------------------------

#     If going UP (↗):
#         - Normal move:
#             row -= 1
#             col += 1

#         - Boundary cases:
#             if at TOP wall (row == 0)
#             OR at RIGHT wall (col == width):
#                 → switch direction (goingDown = True)

#                 if at right wall:
#                     move DOWN (row += 1)
#                 else:
#                     move RIGHT (col += 1)

#     -----------------------------------------------------

#     LOOP CONDITION:
#         Continue until indices go out of bounds

#     -----------------------------------------------------

#     TIME COMPLEXITY:
#         O(n * m) → we visit every element once

#     SPACE COMPLEXITY:
#         O(n * m) → storing result

#     -----------------------------------------------------

#     DUMMY EXAMPLE:

#     Input:
#         [
#             [1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]
#         ]

#     Output:
#         [1, 4, 2, 3, 5, 7, 8, 6, 9]

#     -----------------------------------------------------

#     DRY RUN FLOW (MENTAL MODEL):

#         (0,0) → 1
#         ↓
#         (1,0) → 4
#         ↗
#         (0,1) → 2
#         →
#         (0,2) → 3
#         ↙
#         (1,1) → 5
#         (2,0) → 7
#         →
#         (2,1) → 8
#         ↗
#         (1,2) → 6
#         ↓
#         (2,2) → 9

#     Pattern:
#         DOWN → ↗ → RIGHT → ↙ → repeat...

#     -----------------------------------------------------
#     """

def zigzagTraverse(array):
    
    height = len(array) - 1
    width = len(array[0]) - 1

    row, col = 0, 0
    goingDown = True
    result = []

    while not isOutOfBounds(row, col, height, width):
        result.append(array[row][col])

        if goingDown:
            if col == 0 or row == height:
                goingDown = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                goingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1

    return result


def isOutOfBounds(row, col, height, width):
    # Returns True if indices go outside matrix boundaries
    return row < 0 or row > height or col < 0 or col > width



array = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
print("Zigzag Traversal Output:", zigzagTraverse(array))  # Output: [1, 4, 2, 3, 5, 7, 8, 6, 9]
