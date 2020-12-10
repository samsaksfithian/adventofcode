from itertools import combinations

inputFile = open("day9_input.txt", "r")
preambleSize = 25
# inputFile = open("day9_exampleinput.txt", "r")
# preambleSize = 5

numList = [int(numStr) for numStr in inputFile.readlines()]

# Part 1
preambleNums = numList[:preambleSize]
firstInvalid = None
for index in range(preambleSize, len(numList)):
    checkNum = numList[index]
    foundSum = False
    for pair in combinations(preambleNums, 2):
        if checkNum == sum(pair):
            foundSum = True
            break
    if not foundSum:
        # print("invalid num: {}".format(checkNum))
        firstInvalid = checkNum
        break
    preambleNums.pop(0)
    preambleNums.append(numList[index])

print("Part 1: first invalid number = {}".format(firstInvalid))

# Part 2
def findContigSum(targetSum, startIndex):
    contigRange = []
    found = False
    for index in range(startIndex, len(numList)):
        contigRange.append(numList[index])
        if sum(contigRange) == targetSum and index != startIndex:
            found = True
            break
        if sum(contigRange) > targetSum:
            break
    return [found, contigRange]


weakness = None
for startIndex in range(len(numList)):
    found, contigRange = findContigSum(firstInvalid, startIndex)
    if found:
        weakness = min(contigRange) + max(contigRange)
        break

print("Part 2: encryption weakness = {}".format(weakness))

inputFile.close()
