fileName = "day6_input.txt"

example1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
example2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
example3 = "nppdvjthqldpwncqszvftbrmjlhg"
example4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
example5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

with open(fileName, "r") as inputFile:
    bufferInput = inputFile.read()


def findMarker(buffer: str, markerSize: int) -> tuple[int, str]:
    marker = ""
    for idx, char in enumerate(buffer):
        marker = marker + char
        if char in marker[:-1]:
            marker = marker[marker.index(char) + 1 :]
            # print("char found, resetting marker")
        # print(marker)
        if len(marker) >= markerSize:
            return [idx + 1, marker]


# Part 1, find start-of-packet marker
# print(
#     findMarker(example1, 4),
#     findMarker(example2, 4),
#     findMarker(example3, 4),
#     findMarker(example4, 4),
#     findMarker(example5, 4),
# )

numChars1, sOPMarker = findMarker(bufferInput, 4)
print(f"Part 1: num chars before start-of-packet marker = {numChars1}")


# Part 2, find start-of-message marker
# print(
#     findMarker(example1, 14),
#     findMarker(example2, 14),
#     findMarker(example3, 14),
#     findMarker(example4, 14),
#     findMarker(example5, 14),
# )
numChars2, sOMMarker = findMarker(bufferInput, 14)
print(f"Part 2: num chars before start-of-message marker = {numChars2}")
