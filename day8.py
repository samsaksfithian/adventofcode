inputFile = open("day8_input.txt", "r")
# inputFile = open("day8_exampleinput.txt", "r")

instrTextLines = inputFile.readlines()

instrTupleList = []
for line in instrTextLines:
    op, num = line.split(" ")
    instrTupleList.append([op, int(num)])


def runSteps(printLines=False, indexToFlip=-1):
    accumulator = 0
    instrIndex = 0
    visited = [False] * len(instrTupleList)
    count = 1
    isLoop = False
    while instrIndex < len(instrTupleList):
        if visited[instrIndex]:
            isLoop = True
            break
        op, num = instrTupleList[instrIndex]
        visited[instrIndex] = True
        # Flip for part 2
        flipStr = ""
        if indexToFlip == instrIndex:
            flipStr = "-- flipped"
            if op == "nop":
                op = "jmp"
            elif op == "jmp":
                op = "nop"

        if op == "nop":
            instrIndex += 1
        elif op == "jmp":
            instrIndex += num
        elif op == "acc":
            accumulator += num
            instrIndex += 1

        if printLines:
            print(
                "{} |  {} {:2}   (i = {:2}) {}".format(
                    count, op, num, instrIndex, flipStr
                )
            )
        count += 1

    return [isLoop, accumulator]


print("\nPart 1: accumulated total: {}".format(runSteps()[1]))

# Part 2
for index in range(len(instrTupleList)):
    # print("\ntrying with flipped index {}".format(index))
    stillLoops, accum = runSteps(False, index)
    if not stillLoops:
        print(
            "\nPart 2: found fix (flip: {} @ index {}), accumulator = {}".format(
                instrTupleList[index], index, accum
            )
        )
        break

inputFile.close()
