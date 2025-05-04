def revealMinesweeper(board, row, coloumn): 
    if board[row][coloumn] == 'M':
        return board
    
    neighbors = getNeighbors(board, row, coloumn)
    adjacentMinesCount = 0

    # Count adjacent mines
    for neighborRow, neighborColoumn in neighbors:
        if board[neighborRow][neighborColoumn] == 'M':
            adjacentMinesCount += 1

    if adjacentMinesCount > 0: 
        board[row][coloumn] = str(adjacentMinesCount)
    else:
        board[row][coloumn] = '0'
        for neighborRow, neighborColoumn in neighbors:
            if board[neighborRow][neighborColoumn] == 'H':
                revealMinesweeper(board, neighborRow, neighborColoumn)

    # Final return should be outside the loop
    return board
            
    
def getNeighbors(board, row, coloumn):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    neighbors = []
    for directionRow, directionColoumn in directions:
        newRow = row + directionRow
        newColoumn = coloumn + directionColoumn
        if 0 <= newRow < len(board) and 0 <= newColoumn < len(board[0]):
            neighbors.append((newRow, newColoumn))
    return neighbors    