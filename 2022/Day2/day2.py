with open("day2_input.txt", "r") as inputFile:
    stratGuide = [line.split() for line in inputFile.readlines()]

throwOptions = ["rock", "paper", "scissors"]
scoring = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
    "lose": 0,
    "draw": 3,
    "win": 6,
}


def rps(opp: str, you: str) -> str:
    if opp == you:
        return "draw"
    if you == "rock":
        return "win" if opp == "scissors" else "lose"
    if you == "paper":
        return "win" if opp == "rock" else "lose"
    if you == "scissors":
        return "win" if opp == "paper" else "lose"


def scoreRound(opp: str, you: str) -> int:
    selectPoints = scoring[you]
    result = rps(opp, you)
    resultPoints = scoring[result]
    return selectPoints + resultPoints


# Part 1, score by guide with specific throws
mapping1 = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

stratGuideMapped1 = [[mapping1[oppE], mapping1[youE]] for oppE, youE in stratGuide]

score1 = 0
for opp, you in stratGuideMapped1:
    score1 += scoreRound(opp, you)
print(f"Part 1: Total score by guide with what to throw = {score1}")


# Part 2, score by guide with results
def getThrow(opp: str, result: str) -> str:
    if result == "draw":
        return opp
    for throw in throwOptions:
        if rps(opp, throw) == result:
            return throw


mapping2 = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}

stratGuideMapped2 = [
    [mapping2[oppE], getThrow(mapping2[oppE], mapping2[resultE])]
    for oppE, resultE in stratGuide
]


score2 = 0
for opp, you in stratGuideMapped2:
    score2 += scoreRound(opp, you)
print(f"Part 2: Total score by guide with what the result should be = {score2}")
