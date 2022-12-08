fileName = "day7_input.txt"
# fileName = "day7_example-input.txt"

with open(fileName, "r") as inputFile:
    inputStr = inputFile.read().strip()

rootDirKeys = []
dirs = {}
path = []
for line in inputStr.split("\n"):
    chunks = line.split()
    currDirKey = "/".join(path)
    if chunks[0] == "$":
        # process command
        if chunks[1] != "cd":
            continue
        if chunks[2] == "..":
            path.pop()
        else:
            dirName = chunks[2]
            path.append(dirName)
            newDirKey = "/".join(path)
            if newDirKey not in dirs:
                dirs[newDirKey] = {
                    "type": "dir",
                    "name": dirName,
                    "path": newDirKey,
                    "contents": [],
                }
            if not len(path) > 1:
                rootDirKeys.append(newDirKey)
    elif chunks[0] == "dir":
        # make/add new dir
        dirName = chunks[1]
        newDirKey = currDirKey + "/" + dirName
        if newDirKey not in dirs:
            dirs[newDirKey] = {
                "type": "dir",
                "name": dirName,
                "path": newDirKey,
                "contents": [],
            }
        dirs[currDirKey]["contents"].append(dirs[newDirKey])
    else:
        # read/save file info
        fileInfo = {
            "type": "file",
            "name": chunks[1],
            "path": currDirKey + "/" + chunks[1],
            "size": int(chunks[0]),
        }
        dirs[currDirKey]["contents"].append(fileInfo)


def printItem(item: dict, depth: int = 0):
    outStr = f"{depth * 2 * ' '}- {item['name']} ({item['type']})"
    if item["type"] == "file":
        outStr = outStr[:-1] + f", size={item['size']})"
    print(outStr)
    if item["type"] == "dir":
        for subItem in item["contents"]:
            printItem(subItem, depth + 1)


def getItemSize(item: dict, sizeRecord: dict[str, int]) -> int:
    path = item["path"]
    if path in sizeRecord:
        return sizeRecord[path]
    if item["type"] == "file":
        size = item["size"]
    else:
        contentsSize = 0
        for subItem in item["contents"]:
            contentsSize = contentsSize + getItemSize(subItem, sizeRecord)
        size = contentsSize
    sizeRecord[path] = size
    return size


# for rootKey in rootDirKeys:
#     printItem(dirs[rootKey])

# Part 1, find files under size limit
itemSizes = {}
for item in dirs.values():
    getItemSize(item, itemSizes)
dirSizes = [itemSizes[dirPath] for dirPath in dirs]

sizeLimit = 100000
dirSizesInLimit = [size for size in dirSizes if size <= sizeLimit]
print(f"Part 1: sum of dir sizes under limit = {sum(dirSizesInLimit)}")


#  Part 2, find smallest directory to make enough free space
totalSpace = 70000000
spaceNeeded = 30000000
rootSize = itemSizes["/"]
currFreeSpace = totalSpace - rootSize
spaceToDelete = spaceNeeded - currFreeSpace

bigEnoughDirs: list[tuple[str, int]] = [
    (dirPath, itemSizes[dirPath])
    for dirPath in dirs
    if itemSizes[dirPath] >= spaceToDelete
]
smallestDeleteDirPath, smallestDeleteDirSize = min(bigEnoughDirs, key=lambda x: x[1])
print(
    f"Part 2: size of smallest dir to free up space ({smallestDeleteDirPath}) = {smallestDeleteDirSize}"
)
