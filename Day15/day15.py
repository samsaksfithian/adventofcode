exampleInputs = [
    "0,3,6",  # 2020th = 436
    "1,3,2",  # 2020th = 1
    "2,1,3",  # 2020th = 10
    "1,2,3",  # 2020th = 27
    "2,3,1",  # 2020th = 78
    "3,2,1",  # 2020th = 438
    "3,1,2",  # 2020th = 1836
]
puzzleInput = "11,18,0,20,1,7,16"
runExamples = False


def makeStartNumList(inputList):
    return [int(num) for num in inputList.split(",")]


def findSpokenNumOnTurn(targetTurn, startNums):
    seenMap = {}
    lastNumSpoken = None
    for turnNum in range(targetTurn):
        if turnNum < len(startNums):
            newNumSpoken = startNums[turnNum]
        elif lastNumSpoken in seenMap:
            prevSeenTurn, lastSeenTurn = seenMap[lastNumSpoken]
            if prevSeenTurn < 0:
                newNumSpoken = 0
            else:
                newNumSpoken = lastSeenTurn - prevSeenTurn

        if newNumSpoken in seenMap:
            seenMap[newNumSpoken].pop(0)
            seenMap[newNumSpoken].append(turnNum)
        else:
            seenMap[newNumSpoken] = [-1, turnNum]

        # print(
        #     "Turn {}: last spoken = {}  =>  new spoken = {}\n   {}".format(
        #         turnNum, lastNumSpoken, newNumSpoken, seenMap
        #     )
        # )
        lastNumSpoken = newNumSpoken
    # print(seenMap, lastNumSpoken)
    return lastNumSpoken


startNumsList = makeStartNumList(puzzleInput)
print(startNumsList)

# Part 1
print()
part1TargetTurn = 2020
if runExamples:
    for exInput in exampleInputs:
        exStartNumsList = makeStartNumList(exInput)
        part1ExSpoken = findSpokenNumOnTurn(part1TargetTurn, exStartNumsList)
        print(
            "Part 1 example: number spoken on turn #{} = {}".format(
                part1TargetTurn, part1ExSpoken
            )
        )
else:
    part1Spoken = findSpokenNumOnTurn(part1TargetTurn, startNumsList)
    print("Part 1: number spoken on turn #{} = {}".format(part1TargetTurn, part1Spoken))

# Part 2
print()
part2TargetTurn = 30000000
if runExamples:
    for exInput in exampleInputs:
        exStartNumsList = makeStartNumList(exInput)
        part2ExSpoken = findSpokenNumOnTurn(part2TargetTurn, exStartNumsList)
        print(
            "Part 2 example: number spoken on turn #{} = {}".format(
                part2TargetTurn, part2ExSpoken
            )
        )
else:
    part2Spoken = findSpokenNumOnTurn(part2TargetTurn, startNumsList)
    print("Part 2: number spoken on turn #{} = {}".format(part2TargetTurn, part2Spoken))
