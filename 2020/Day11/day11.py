inputFile = open("day11_input.txt", "r")
# inputFile = open("day11_exampleinput.txt", "r")

originalSeatGrid = [list(line) for line in inputFile.read().split("\n")]

empty = "L"
occupied = "#"
floor = "."


def printGrid(grid):
    print("\n")
    for row in grid:
        print(" ".join(row))


def countOccupied(grid):
    count = 0
    for row in grid:
        for char in row:
            if char == occupied:
                count += 1
    return count


def outOfBounds(index, array):
    return index < 0 or len(array) <= index


def outOfGrid(rowNum, colNum, grid):
    return outOfBounds(rowNum, grid) or outOfBounds(colNum, grid[rowNum])


def updateCoordPart1(row, col, grid):
    numAdjOccupied = 0
    seatStart = grid[row][col]
    if seatStart == floor:
        return seatStart

    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if r == 0 and c == 0:
                continue
            adjRow = row + r
            adjCol = col + c
            if outOfGrid(adjRow, adjCol, grid):
                continue
            adjSeat = grid[row + r][col + c]
            if adjSeat == occupied:
                numAdjOccupied += 1

    if seatStart == empty and numAdjOccupied == 0:
        return occupied
    if seatStart == occupied and numAdjOccupied >= 4:
        return empty
    return seatStart


direcMap = {
    "N": [-1, 0],
    "NE": [-1, 1],
    "E": [0, 1],
    "SE": [1, 1],
    "S": [1, 0],
    "SW": [1, -1],
    "W": [0, -1],
    "NW": [-1, -1],
}


def foundOccSeatInLine(rowNum, colNum, grid, moveAmts):
    nextRow = rowNum + moveAmts[0]
    nextCol = colNum + moveAmts[1]
    if outOfGrid(nextRow, nextCol, grid):
        return False
    nextSeat = grid[nextRow][nextCol]
    if nextSeat == occupied:
        return True
    if nextSeat == empty:
        return False
    return foundOccSeatInLine(nextRow, nextCol, grid, moveAmts)


def updateCoordPart2(row, col, grid):
    numVisibleOccupied = 0
    seatStart = grid[row][col]
    if seatStart == floor:
        return seatStart

    for direction in direcMap.keys():
        if foundOccSeatInLine(row, col, grid, direcMap[direction]):
            numVisibleOccupied += 1

    if seatStart == empty and numVisibleOccupied == 0:
        return occupied
    if seatStart == occupied and numVisibleOccupied >= 5:
        return empty
    return seatStart


def updateGrid(grid, updateCoordFunc):
    numChanged = 0
    newGrid = []
    for rowNum in range(len(grid)):
        newGrid.append([])
        for colNum in range(len(grid[rowNum])):
            seat = grid[rowNum][colNum]
            newSeat = updateCoordFunc(rowNum, colNum, grid)
            newGrid[rowNum].append(newSeat)
            if seat != newSeat:
                numChanged += 1
    # printGrid(newGrid)
    # print(numChanged)
    return [numChanged, newGrid]


def adjGridUntilStable(grid, updateCoordFunc):
    changeCount = 1
    adjustedGrid = [row[:] for row in originalSeatGrid]
    while changeCount > 0:
        changeCount, adjustedGrid = updateGrid(adjustedGrid, updateCoordFunc)
    return adjustedGrid


# Part 1
seatGridPt1 = adjGridUntilStable(originalSeatGrid, updateCoordPart1)
finalNumOccupiedPt1 = countOccupied(seatGridPt1)
print("\nPart 1: # seats occupied when stable =", finalNumOccupiedPt1)

# Part 2
seatGridPt2 = adjGridUntilStable(originalSeatGrid, updateCoordPart2)
finalNumOccupiedPt2 = countOccupied(seatGridPt2)
print("Part 2: # seats occupied when stable =", finalNumOccupiedPt2)

inputFile.close()
