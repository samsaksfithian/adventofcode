inputFile = open("day3_input.txt", "r")

linesList = inputFile.read().splitlines()
width = len(linesList[0])

# Strategies/paths:
# Right 1, down 1.
# Right 3, down 1.
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
paths = [
    {"name": "r1d1", "treeCount": 0, "xCoord": 0, "right": 1, "down": 1},
    {"name": "r3d1", "treeCount": 0, "xCoord": 0, "right": 3, "down": 1},
    {"name": "r5d1", "treeCount": 0, "xCoord": 0, "right": 5, "down": 1},
    {"name": "r7d1", "treeCount": 0, "xCoord": 0, "right": 7, "down": 1},
    {"name": "r1d2", "treeCount": 0, "xCoord": 0, "right": 1, "down": 2},
]

prMin = 0
prMax = len(linesList)
prMax = -1
stratToPrint = "r1d2"

labelsTens = "      "
labelsOnes = "      "
for num in range(0, width):
    labelsOnes += str(num)[-1]
    labelsTens += str(num)[0] if num > 9 else " "
labelNums = "{}\n{}".format(labelsTens, labelsOnes)
if prMax >= 0 and stratToPrint in [path["name"] for path in paths]:
    print(labelNums)

lineNum = 0
for line in linesList:
    for path in paths:
        xCoord = path["xCoord"]
        if lineNum % path["down"] != 0:
            visitedLine = line
        elif line[xCoord] == "#":
            path["treeCount"] += 1
            visitedLine = line[:xCoord] + "X" + line[(xCoord + 1) :]
        else:
            visitedLine = line[:xCoord] + "O" + line[(xCoord + 1) :]

        if prMin <= lineNum <= prMax and stratToPrint == path["name"]:
            print("{: >3}:  {}  x = {: >2}".format(lineNum, visitedLine, xCoord))

        if lineNum % path["down"] == 0:
            xCoord += path["right"]
            if xCoord >= width:
                xCoord -= width
            path["xCoord"] = xCoord

    lineNum += 1

treeProduct = 1
print("")
for path in paths:
    print("num trees hit on path {} = {}".format(path["name"], path["treeCount"]))
    treeProduct *= path["treeCount"]

print("total product of trees hit = {}".format(treeProduct))

inputFile.close()
