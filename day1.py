from itertools import combinations

inputFile = open("day1_input.txt", "r")

goalSum = 2020

numList = []
for numStr in inputFile.read().split():
    numList.append(int(numStr))

# Part 1, pairs
for pair in combinations(numList, 2):
    if sum(pair) == goalSum:
        print(pair, "=", pair[0] * pair[1])

# Part 2, triples
for triple in combinations(numList, 3):
    if sum(triple) == goalSum:
        print(triple, "=", triple[0] * triple[1] * triple[2])

inputFile.close()