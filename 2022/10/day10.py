from math import floor

fileName = "day10_input.txt"
# fileName = "day10_example-input.txt"

with open(fileName, "r") as inputFile:
    inputStr = inputFile.read().strip()

# inputStr = "noop\naddx 3\naddx -5"
instructions = inputStr.splitlines()

regX = 1
cycle = 0
signalStrs = []
screen = [[] for _ in range(6)]


def drawPixel():
    rowNum = floor((cycle - 1) / 40)
    colNum = (cycle - 1) % 40
    pixel = "#" if regX - 1 <= colNum <= regX + 1 else "."
    screen[rowNum].append(pixel)
    # print("\n", cycle, rowNum, colNum)
    # print("Current CRT row:", "".join(screen[rowNum]))
    # print("".join(["#" if regX - 1 <= x <= regX + 1 else "." for x in range(40)]))


def tickCycle():
    global cycle
    cycle += 1
    if (cycle + 20) % 40 == 0:
        # print(cycle, regX)
        signalStrs.append(cycle * regX)
    drawPixel()


# Part 1
for instr in instructions:
    if instr == "noop":
        tickCycle()
        continue
    amt = int(instr.split()[1])
    # print(f"Start cycle {cycle + 1}: begin executing {instr}")
    tickCycle()
    tickCycle()
    regX += amt
    # print(f"End cycle {cycle}: finish executing {instr} (regX now = {regX})")
    # print(
    #     "Sprite position:",
    #     "".join(["#" if regX - 1 <= x <= regX + 1 else "." for x in range(40)]),
    # )

print(f"Part 1: sum of signal strengths = {sum(signalStrs)}")

# Part 2
def printScr(scr: list[list[str]]):
    print("\n".join(["".join(row) for row in scr]))


print("Part 2:")
printScr(screen)
