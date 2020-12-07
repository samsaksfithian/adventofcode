inputFile = open("day7_input.txt", "r")
# inputFile = open("day7_exampleinput.txt", "r")
# inputFile = open("day7_exampleinput2.txt", "r")

bagRules = inputFile.readlines()
myBag = "shiny gold"

containMineQueue = [myBag]
bagContents = {}
bagCounts = {}
for bag in bagRules:
    # Part 1
    bagType, subBagStr = bag.split(" bags contain ")
    bagContents[bagType] = subBagStr
    # Part 2
    subBags = subBagStr.split(", ")
    bagCounts[bagType] = {}
    for sub in subBags:
        count = int(sub[0]) if sub[0] != "n" else 0
        if count != 0:
            subType = sub.split(" bag")[0][2:]
            bagCounts[bagType][subType] = count

# Part 1
for bagType in containMineQueue:
    # print(bagType)
    for bagKey in bagContents.keys():
        if bagType in bagContents[bagKey] and not bagKey in containMineQueue:
            containMineQueue.append(bagKey)

print(
    "Part 1: number of bags that can hold mine (a {} bag) = {}".format(
        myBag, len(containMineQueue) - 1
    )
)

# Part 2
def recurseCount(bagType, bagCountMap):
    bagInfo = bagCountMap[bagType]
    total = 1  # need to count the bag itself
    for subKey in bagInfo.keys():
        total += bagInfo[subKey] * recurseCount(subKey, bagCountMap)
    return total


# print(bagCounts)
mineTotal = recurseCount(myBag, bagCounts)
print("Part 2: my bag must contain {} other bags".format(mineTotal - 1))

inputFile.close()