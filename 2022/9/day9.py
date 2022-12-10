from math import sqrt, ceil, floor

fileName = "day9_input.txt"
# fileName = "day9_example-input.txt"
# fileName = "day9_example-input2.txt"

with open(fileName, "r") as inputFile:
    inputStr = inputFile.read().strip()


instructions = [
    (line.split()[0], int(line.split()[1])) for line in inputStr.splitlines()
]


def pointsAreAdjacent(point1: tuple[int, int], point2: tuple[int, int]) -> bool:
    x1, y1 = point1
    x2, y2 = point2
    return x1 - 1 <= x2 <= x1 + 1 and y1 - 1 <= y2 <= y1 + 1


def addPoints(point1: tuple[int, int], point2: tuple[int, int]) -> tuple[int, int]:
    return (point1[0] + point2[0], point1[1] + point2[1])


def getNewTailCoords(
    headCoord: tuple[int, int], tailCoord: tuple[int, int]
) -> tuple[int, int]:
    if pointsAreAdjacent(headCoord, tailCoord):
        # print(f"Adjacent, don't need to move -- {headCoord} {tailCoord}")
        return tailCoord
    xDiff = headCoord[0] - tailCoord[0]
    yDiff = headCoord[1] - tailCoord[1]
    dist = sqrt(xDiff * xDiff + yDiff * yDiff)
    unitVecRaw = (xDiff / dist, yDiff / dist)
    unitVec = tuple(ceil(coord) if coord > 0 else floor(coord) for coord in unitVecRaw)
    # print(
    #     f"Head = {headCoord}, Tail = {tailCoord} \t Vector = {unitVec}; Raw Vec = {unitVecRaw}"
    # )
    return addPoints(tailCoord, unitVec)


movements = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def step(
    direc: str, headCoord: tuple[int, int], tailCoord: tuple[int, int]
) -> tuple[tuple[int, int], tuple[int, int]]:
    # print(f"Start step: {headCoord} {tailCoord}")
    mvmt = movements[direc]
    newHead = addPoints(headCoord, mvmt)
    newTail = getNewTailCoords(newHead, tailCoord)
    return (newHead, newTail)


# Part 1
startCoord = (0, 0)
head = (startCoord[0], startCoord[1])
tail = (startCoord[0], startCoord[1])
tailVisitCoords = set([tail])

for direc, amt in instructions:
    # print(f"Moving {direc} {amt}; Head = {head}, Tail = {tail}")
    for _ in range(amt):
        head, tail = step(direc, head, tail)
        tailVisitCoords.add(tail)

# print(tailVisitCoords)
print(f"Part 1: num positions tail visited = {len(tailVisitCoords)}")


# Part 2, longer rope
def stepLonger(direc: str, coordList: list[tuple[int, int]]):
    mvmt = movements[direc]
    coordList[0] = addPoints(coordList[0], mvmt)
    for idx in range(1, len(coordList)):
        coordList[idx] = getNewTailCoords(coordList[idx - 1], coordList[idx])


ropeLength = 10
rope: list[tuple[int, int]] = [startCoord for _ in range(ropeLength)]
endVisitCoords = set([rope[-1]])

for direc, amt in instructions:
    # print(f"Moving {direc} {amt}; Head = {head}, Tail = {tail}")
    for _ in range(amt):
        stepLonger(direc, rope)
        endVisitCoords.add(rope[-1])

# print(endVisitCoords)
print(f"Part 2: num positions rope end visited = {len(endVisitCoords)}")
