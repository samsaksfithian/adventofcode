inputFile = open("day16_input.txt", "r")
# inputFile = open("day16_exampleinput.txt", "r")
# inputFile = open("day16_exampleinput2.txt", "r")

ruleStrs, mineStr, nearbyStrs = [
    line.split("\n") for line in inputFile.read().split("\n\n")
]
mineStr = mineStr[1]
nearbyStrs.pop(0)


def parseTicket(ticketStr):
    return [int(numStr) for numStr in ticketStr.split(",")]


def parseRule(ruleStr):
    field, rangeOptionStrs = ruleStr.split(": ")
    ranges = []
    for rangeStr in rangeOptionStrs.split(" or "):
        ranges.append([int(num) for num in rangeStr.split("-")])
    return [field, ranges]


myTicket = parseTicket(mineStr)
nearbyTickets = [parseTicket(ticketStr) for ticketStr in nearbyStrs]
rulesList = [parseRule(rule) for rule in ruleStrs]

# print("My ticket:", myTicket)
# print("Nearby tickets:\n  ", nearbyTickets)
# print("Rules:\n  ", rulesList)

# Part 1
def isPossibleValid(value, rangeOptions):
    for rangeMin, rangeMax in rangeOptions:
        if rangeMin <= value <= rangeMax:
            return True
    return False


allRanges = [rangeTup for (_, ranges) in rulesList for rangeTup in ranges]
scanErrors = [
    value
    for ticketNums in nearbyTickets
    for value in ticketNums
    if not isPossibleValid(value, allRanges)
]

# print(allRanges)
# print(scanErrors)

print("\nPart 1: ticket error rate =", sum(scanErrors))

# Part 2
validTickets = [
    ticket
    for ticket in nearbyTickets
    if all([isPossibleValid(value, allRanges) for value in ticket])
]
validTickets.append(myTicket)
# print(validTickets)

orderedFieldNames = [""] * len(myTicket)


def validFieldNumAllTickets(index, ranges, ticketList):
    for ticket in ticketList:
        if not isPossibleValid(ticket[index], ranges):
            return False
    return True


# FIXME: has duplicates/overwrites positions/doesn't fill all positions
# loop through each rule
# for each rule loop through each possible index in tickets
# for each index check every ticket value at that index
# if one isn't valid, go to the next index
# if all are valid, set ordered field name at the index to the rulename
for fieldName, ranges in rulesList:
    for index in range(len(orderedFieldNames)):
        if orderedFieldNames[index] != "":
            continue
        if validFieldNumAllTickets(index, ranges, validTickets):
            orderedFieldNames[index] = fieldName
            print(index, fieldName)
            break

print(orderedFieldNames)

product = 1
departNums = []
for index in range(len(myTicket)):
    if "departure" in orderedFieldNames[index]:
        product *= myTicket[index]
        departNums.append(myTicket[index])

print(product, departNums)

inputFile.close()
