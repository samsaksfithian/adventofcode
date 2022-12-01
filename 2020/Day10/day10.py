inputFile = open("day10_input.txt", "r")
# inputFile = open("day10_exampleinput.txt", "r")
# inputFile = open("day10_exampleinput2.txt", "r")

joltageVals = [int(line) for line in inputFile.readlines()]
deviceJoltage = max(joltageVals) + 3

joltageVals.sort()
joltageVals = [0] + joltageVals + [deviceJoltage]

# print(joltageVals)

# Part 1
num1JoltDiffs = 0
num3JoltDiffs = 0
for index in range(len(joltageVals) - 1):
    currVal = joltageVals[index]
    nextVal = joltageVals[index + 1]
    diff = nextVal - currVal
    if diff < 1 or 3 < diff:
        num1JoltDiffs = 0
        num3JoltDiffs = 0
        break
    if diff == 1:
        # print(
        #     "diff of 1 @ index {}: currVal = {} and nextVal = {}".format(
        #         index, currVal, nextVal
        #     )
        # )
        num1JoltDiffs += 1
    elif diff == 3:
        num3JoltDiffs += 1

print(
    "\nPart 1: # diffs 1j = {};  # diffs 3j = {}\n  ==>  product = {}".format(
        num1JoltDiffs, num3JoltDiffs, num1JoltDiffs * num3JoltDiffs
    )
)

# Part 2
memoizedCounts = {}


def recurseFindArrangement(startIndex):
    currVal = joltageVals[startIndex]
    if currVal in memoizedCounts.keys():
        return memoizedCounts[currVal]
    if currVal == deviceJoltage:
        return 1
    count = 0
    for diff in range(1, 4):
        try:
            nextIndex = joltageVals.index(currVal + diff, startIndex)
            count += recurseFindArrangement(nextIndex)
        except ValueError:
            # currVal + diff not a number option
            pass

    memoizedCounts[currVal] = count
    return count


arrangements = recurseFindArrangement(0)
print("Part 2: number of possible arrangements = {}".format(arrangements))
# print(memoizedCounts)

inputFile.close()
