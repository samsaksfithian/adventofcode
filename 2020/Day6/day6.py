inputFile = open("day6_input.txt", "r")
# inputFile = open("day6_exampleinput.txt", "r")

groupsList = inputFile.read().split("\n\n")

totalsPart1 = []
totalsPart2 = []
for group in groupsList:
    groupQs = {}
    people = group.split()
    for person in people:
        for qChar in person:
            prevCount = groupQs[qChar] if qChar in groupQs.keys() else 0
            groupQs[qChar] = prevCount + 1

    totalsPart1.append(len(groupQs.keys()))
    groupTotal = 0
    for key in groupQs:
        if groupQs[key] == len(people):
            groupTotal += 1
    totalsPart2.append(groupTotal)

print("part 1 total = {}".format(sum(totalsPart1)))
print("part 2 total = {}".format(sum(totalsPart2)))

inputFile.close()