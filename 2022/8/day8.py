from math import prod

fileName = "day8_input.txt"
# fileName = "day8_example-input.txt"

with open(fileName, "r") as inputFile:
    inputStr = inputFile.read().strip()

treeGrid = [[int(tree) for tree in line] for line in inputStr.split("\n")]
width = len(treeGrid[0])
height = len(treeGrid)


def printGrid(grid: list[list]):
    for row in grid:
        print("".join([str(cell) for cell in row]))


# Part 1, num visible from edges

# NOTE: this is super inefficent and pretty brute-force
def checkVisibility(grid: list[list[int]], colIdx: int, rowIdx: int) -> bool:
    # visible if on edge
    if not (0 < colIdx < len(grid[0]) - 1) or not (0 < rowIdx < len(grid) - 1):
        return True

    row = grid[rowIdx]
    col = [grid[r][colIdx] for r in range(len(grid))]
    treeHeight = grid[rowIdx][colIdx]
    directions = (row[:colIdx], row[colIdx + 1 :], col[:rowIdx], col[rowIdx + 1 :])
    for direcList in directions:
        if all(cell < treeHeight for cell in direcList):
            return True
    return False


numVisible = 0
visibilityGrid = [["." for _ in range(width)] for _ in range(height)]
for ri in range(height):
    for ci in range(width):
        if checkVisibility(treeGrid, ci, ri):
            numVisible += 1
            visibilityGrid[ri][ci] = "v"

# visibilityGrid = [
#     ["v" if checkVisibility(treeGrid, ci, ri) else "." for ci in range(width)]
#     for ri in range(height)
# ]
# printGrid(visibilityGrid)
print(f"Part 1: num trees visible = {numVisible}")

# Part 2, scenic score
def countVisibleTreesInDir(currHeight: int, treeList: list[int]) -> int:
    numVisible = 0
    for tree in treeList:
        numVisible += 1
        if tree >= currHeight:
            break
    return numVisible


def getScenicScore(grid: list[list[int]], colIdx: int, rowIdx: int) -> int:
    row = grid[rowIdx]
    col = [grid[r][colIdx] for r in range(len(grid))]
    treeHeight = grid[rowIdx][colIdx]
    directions = (
        reversed(row[:colIdx]),
        row[colIdx + 1 :],
        reversed(col[:rowIdx]),
        col[rowIdx + 1 :],
    )
    return prod(
        [countVisibleTreesInDir(treeHeight, treeList) for treeList in directions]
    )


maxScore = 0
maxCoords = (-1, -1)
scoreGrid = [[0 for _ in range(width)] for _ in range(height)]
for ri in range(height):
    for ci in range(width):
        score = getScenicScore(treeGrid, ci, ri)
        scoreGrid[ri][ci] = score
        if score > maxScore:
            maxScore = score
            maxCoords = (ri, ci)

print(f"Part 2: max scenic score = {maxScore} at {maxCoords}")
