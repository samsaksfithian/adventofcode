from copy import deepcopy

fileName = "day5_input.txt"
# fileName = "day5_example-input.txt"

with open(fileName, "r") as inputFile:
    cratesRaw, movesRaw = inputFile.read().split("\n\n")

# Parse crates input
cratesRawLines = cratesRaw.splitlines()
crateRowStrs, numCols = cratesRawLines[:-1], len(cratesRawLines[-1].split())

startColumns = [[] for _ in range(numCols)]
crateRows = [
    [rowStr[i : i + 3] for i in range(0, len(rowStr), 4)] for rowStr in crateRowStrs
]

for row in reversed(crateRows):
    for idx, crate in enumerate(row):
        crateCont = crate[1].strip()
        if crateCont:
            startColumns[idx].append(crateCont)


def printCrates(cols: list[list[str]]):
    for idx, col in enumerate(cols):
        horizCol = " ".join([f"[{crate}]" for crate in col])
        print(f"{idx + 1}: {horizCol}")


# printCrates(startColumns)

# Parse instructions input
moves = [
    [int(word) for word in line.split() if word.isdigit()]
    for line in movesRaw.splitlines()
]
# print(moves)


# Part 1, execute moves moving one at a time
def executeMove9000(columns: list[list[str]], count: int, fromNum: int, toNum: int):
    srcCol = columns[fromNum - 1]
    destCol = columns[toNum - 1]
    for _ in range(count):
        destCol.append(srcCol.pop())


p1Cols = deepcopy(startColumns)
for move in moves:
    executeMove9000(p1Cols, *move)
    # print("\n")
    # printCrates(p1Cols)

topCrates1 = [col[-1] for col in p1Cols]
print(f'Part 1: top crates after all moves => {"".join(topCrates1)}')


# Part 2, execute moves moving multiple at a time
def executeMove9001(columns: list[list[str]], count: int, fromNum: int, toNum: int):
    srcCol = columns[fromNum - 1]
    destCol = columns[toNum - 1]
    destCol.extend(srcCol[-1 * count :])
    del srcCol[-1 * count : :]


p2Cols = deepcopy(startColumns)
for move in moves:
    executeMove9001(p2Cols, *move)
    # print("\n")
    # printCrates(p2Cols)

topCrates2 = [col[-1] for col in p2Cols]
print(f'Part 2: top crates after all moves => {"".join(topCrates2)}')
