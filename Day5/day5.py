from math import floor, ceil

inputFile = open("day5_input.txt", "r")

linesList = inputFile.readlines()

idsList = []
for line in linesList:
    rowCoords = line[:7]
    colCoords = line[7:]
    minRow = 0
    maxRow = 127
    for charNum in range(7):
        diff = maxRow - minRow
        if rowCoords[charNum] == "F":
            # lower half
            maxRow = floor(diff / 2 + minRow)
        elif rowCoords[charNum] == "B":
            # upper half
            minRow = ceil(diff / 2 + minRow)
        # print(charNum + 1, "-", minRow, maxRow)

    minCol = 0
    maxCol = 7
    for charNum in range(3):
        diff = maxCol - minCol
        if colCoords[charNum] == "L":
            # lower half
            maxCol = floor(diff / 2 + minCol)
        elif colCoords[charNum] == "R":
            # upper half
            minCol = ceil(diff / 2 + minCol)
        # print(charNum + 1, "-", minCol, maxCol)
    seatId = minRow * 8 + minCol
    idsList.append(seatId)

print("max id =", max(idsList))

for seatId in idsList:
    if (not (seatId + 1) in idsList) and (seatId + 2) in idsList:
        print("my seat id =", seatId + 1)

inputFile.close()