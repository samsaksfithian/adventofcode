inputFile = open("day12_input.txt", "r")
# inputFile = open("day12_exampleinput.txt", "r")

navActions = [[line[0], int(line[1:])] for line in inputFile.readlines()]

# print(navActions)


def calcManhattanDistMap(dirMap):
    northSouthDiff = dirMap["N"] - dirMap["S"]
    eastWestDiff = dirMap["E"] - dirMap["W"]
    return abs(northSouthDiff) + abs(eastWestDiff)


# Part 1
def calcDirAfterTurn(startDir, turnDir, degrees):
    orderedDirList = ["N", "E", "S", "W"]
    numDirChanged = int((degrees / 90) * (1 if turnDir == "R" else -1))
    newIndex = int(
        (orderedDirList.index(startDir) + numDirChanged) % len(orderedDirList)
    )
    return orderedDirList[newIndex]


moveMap = {
    "N": 0,
    "S": 0,
    "E": 0,
    "W": 0,
    "facing": "E",
}
for direction, amount in navActions:
    if direction == "R" or direction == "L":
        moveMap["facing"] = calcDirAfterTurn(moveMap["facing"], direction, amount)
        continue
    if direction == "F":
        direction = moveMap["facing"]
    moveMap[direction] += amount
    # print("moving {} in {} direction".format(amount, direction))
    # print(moveMap)

manhatDist1 = calcManhattanDistMap(moveMap)
print("\nPart 1: Manhattan distance =", manhatDist1)

# Part 2
def calcManhattanDistList(coordList):
    # return sum(abs(coord) for coord in coordList)
    return abs(coordList[0]) + abs(coordList[1])


def calcRotatedWaypoint(clockDir, degrees, initialWaypoint):
    initEW, initNS = initialWaypoint
    if degrees == 180:
        return [-1 * initEW, -1 * initNS]
    quadrantSigns = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
    currSigns = [1 if initEW >= 0 else -1, 1 if initNS >= 0 else -1]
    numQuadsChanged = (degrees / 90) * (-1 if clockDir == "R" else 1)
    newQuadIndex = int(
        (quadrantSigns.index(currSigns) + numQuadsChanged) % len(quadrantSigns)
    )
    newSignEW, newSignNS = quadrantSigns[newQuadIndex]
    newWaypoint = [newSignEW * abs(initNS), newSignNS * abs(initEW)]
    # print("{}{} - {} => {}".format(clockDir, degrees, waypoint, newWaypoint))
    return newWaypoint


shipCoords = [0, 0]
waypoint = [10, 1]
for direction, amount in navActions:
    if direction == "L" or direction == "R":
        waypoint = calcRotatedWaypoint(direction, amount, waypoint)
    elif direction == "N":
        waypoint[1] += amount
    elif direction == "S":
        waypoint[1] -= amount
    elif direction == "E":
        waypoint[0] += amount
    elif direction == "W":
        waypoint[0] -= amount
    elif direction == "F":
        shipCoords[0] += amount * waypoint[0]
        shipCoords[1] += amount * waypoint[1]
    # print(shipCoords, waypoint)

print(shipCoords, waypoint)
manhatDist2 = calcManhattanDistList(shipCoords)
print("Part 2: Manhattan distance =", manhatDist2)

inputFile.close()
