inputFile = open("day2_input.txt", "r")

numValidPt1 = 0
numValidPt2 = 0
linesList = inputFile.readlines()
for line in linesList:
    [numRange, letter, password] = line.split()
    letter = letter[0]
    [firstNum, secondNum] = numRange.split("-")
    firstNum = int(firstNum)
    secondNum = int(secondNum)

    # Part 1, counting occurrences
    letterCount = password.count(letter)
    if firstNum <= letterCount <= secondNum:
        numValidPt1 += 1
        # print(
        #     "valid: {ps} -- {fst}-{scd}x '{lt}'".format(
        #         ps=password, fst=firstNum, scd=secondNum, lt=letter
        #     )
        # )

    # Part 2, checking positions
    firstPosMatch = password[firstNum - 1] == letter
    secondPosMatch = password[secondNum - 1] == letter
    if firstPosMatch != secondPosMatch:
        numValidPt2 += 1
        # print(
        #     "valid: {ps} -- '{lt}' @ {fst} xor {scd} ".format(
        #         ps=password, fst=firstNum, scd=secondNum, lt=letter
        #     )
        # )

total = len(linesList)
print("Part 1: num valid = {val} ({tot} total)".format(val=numValidPt1, tot=total))
print("Part 2: num valid = {val} ({tot} total)".format(val=numValidPt2, tot=total))

inputFile.close()