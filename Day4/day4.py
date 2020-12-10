inputFile = open("day4_input.txt", "r")

requiredKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

passportStrings = inputFile.read().split("\n\n")

numValid = 0
for passport in passportStrings:
    fields = passport.split()
    fieldKeys = []
    for field in fields:
        fieldKeys.append(field.split(":")[0])
    # print(fieldKeys)
    if all((key in fieldKeys) for key in requiredKeys):
        # print("keys match")
        numValid += 1

print("{} valid out of {} total".format(numValid, len(passportStrings)))

inputFile.close()