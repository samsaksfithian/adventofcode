from math import gcd
from functools import reduce

# inputFile = open("day13_input.txt", "r")
inputFile = open("day13_exampleinput.txt", "r")

timeLine, busLine = inputFile.readlines()

earliestTime = int(timeLine)
busIdNums = [int(idNum) for idNum in busLine.split(",") if idNum != "x"]

# Part 1
def findFirstBus(busIds, initTime):
    currTime = initTime
    foundBus = None
    while not foundBus:
        for busNum in busIds:
            if currTime % busNum == 0:
                foundBus = busNum
                return [busNum, currTime]
        currTime += 1


foundBus, departTime = findFirstBus(busIdNums, earliestTime)
waitTime = departTime - earliestTime
print(
    "\nPart 1: take bus #{} at {} (waiting {} mins) -- product = {}".format(
        foundBus, departTime, waitTime, foundBus * waitTime
    )
)

# Part 2
# def checkTimestamp(time, orderedDeparts):
#     for offset in range(len(orderedDeparts)):
#         bus = orderedDeparts[offset]
#         if bus == "x":
#             continue
#         busNum = int(bus)
#         currBusTime = time + offset
#         if currBusTime % busNum != 0:
#             return False
#     return True


busReqs = busLine.split(",")
# currTime = 0
# while not checkTimestamp(currTime, busReqs):
#     currTime += 1

# importantIndices = [busReqs.index(str(busNum)) for busNum in busIdNums]
idsWithOffsets = [
    int(busReqs[offset]) - offset
    for offset in range(len(busReqs))
    if busReqs[offset] != "x"
]

firstTimestamp = reduce(lambda a, b: a * b // gcd(a, b), idsWithOffsets)
print("Part 2: consecutive timestamp reqs first met at timestamp = ", firstTimestamp)

inputFile.close()
