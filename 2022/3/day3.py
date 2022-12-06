from math import floor

# with open("day3_example-input.txt", "r") as inputFile:
with open("day3_input.txt", "r") as inputFile:
    sackList = inputFile.read().splitlines()


def getPriority(char: str) -> int:
    adj = -38 if char.isupper() else -96
    return ord(char) + adj


# Part 1
sackListByComp: list[list[str]] = []
for sack in sackList:
    compSize = floor(len(sack) / 2)
    comp1 = sack[:compSize]
    comp2 = sack[compSize:]
    sackListByComp.append([comp1, comp2])


def findCommonItem(*chunks) -> str:
    chunkSets = [set(chunk) for chunk in chunks]
    commonItems = chunkSets[0].intersection(*chunkSets[1:])
    return [item for item in commonItems][0]


commonItems = [findCommonItem(comp1, comp2) for comp1, comp2 in sackListByComp]
prioritiesOfCommons = [getPriority(common) for common in commonItems]

# print(commonItems, "\n", prioritiesOfCommons)
print(f"Part 1: sum of priorities of common items = {sum(prioritiesOfCommons)}")


# Part 2
elfGroups = [sackList[i : i + 3] for i in range(0, len(sackList), 3)]
commonGroupItems = [findCommonItem(*group) for group in elfGroups]
prioritiesOfGroupCommons = [getPriority(common) for common in commonGroupItems]
print(
    f"Part 2: sum of priorities of group common items = {sum(prioritiesOfGroupCommons)}"
)
