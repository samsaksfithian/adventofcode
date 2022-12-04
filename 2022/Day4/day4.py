# with open("day4_example-input.txt", "r") as inputFile:
with open("day4_input.txt", "r") as inputFile:
    pairList = [line.split(",") for line in inputFile.read().splitlines()]

parsedPairs = [
    [[int(num) for num in elf.split("-")] for elf in pair] for pair in pairList
]

# Part 1
count = 0
for elfA, elfB in parsedPairs:
    if (elfA[0] <= elfB[0] and elfB[1] <= elfA[1]) or (
        elfB[0] <= elfA[0] and elfA[1] <= elfB[1]
    ):
        count += 1

print(f"Part 1: number of pairs where one contains the other = {count}")

# Part 2
overlapCount = 0
for elfA, elfB in parsedPairs:
    if (
        elfA[0] <= elfB[0] <= elfA[1]
        or elfA[0] <= elfB[1] <= elfA[1]
        or elfB[0] <= elfA[0] <= elfB[1]
        or elfB[0] <= elfA[0] <= elfB[1]
    ):
        overlapCount += 1

print(f"Part 2: number of pairs there is overlap = {overlapCount}")
