with open("day1_input.txt", "r") as inputFile:
    elfPacks = [
        [int(cal) for cal in elf.splitlines()] for elf in inputFile.read().split("\n\n")
    ]

elfCalTotals = [sum(pack) for pack in elfPacks]

# Part 1, find with most
elfWithMost = -1
maxCals = 0
for idx, packSum in enumerate(elfCalTotals):
    if packSum > maxCals:
        maxCals = packSum
        elfWithMost = idx
print(f"Part 1: Elf #{elfWithMost + 1} has most total ({maxCals})")

# Part 2, find top 3
sortedCalTotals = elfCalTotals[:]
sortedCalTotals.sort(reverse=True)

numNeeded = 3
topTotals = sortedCalTotals[:numNeeded]
print(
    f"Part 2: Top {numNeeded} elves are carrying {', '.join(map(str, topTotals))} cals, Total = {sum(topTotals)}"
)
