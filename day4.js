const fs = require("fs");

const requirements = {
  byr: (yearStr, strict = false) => {
    if (!yearStr) return false;
    if (!strict) return true;
    const yearNum = parseInt(yearStr);
    if (yearStr.length === 4 && yearNum && 1920 <= yearNum && yearNum <= 2002) {
      return true;
    }
    return false;
  },
  iyr: (yearStr, strict = false) => {
    if (!yearStr) return false;
    if (!strict) return true;
    const yearNum = parseInt(yearStr);
    if (yearStr.length === 4 && yearNum && 2010 <= yearNum && yearNum <= 2020) {
      return true;
    }
    return false;
  },
  eyr: (yearStr, strict = false) => {
    if (!yearStr) return false;
    if (!strict) return true;
    const yearNum = parseInt(yearStr);
    if (yearStr.length === 4 && yearNum && 2020 <= yearNum && yearNum <= 2030) {
      return true;
    }
    return false;
  },
  hgt: (heightStr, strict = false) => {
    if (!heightStr) return false;
    if (!strict) return true;
    const units = heightStr.slice(-2);
    const num = parseInt(heightStr.slice(0, -2));
    if (
      (units === "cm" && num && 150 <= num && num <= 193) ||
      (units === "in" && num && 59 <= num && num <= 76)
    ) {
      return true;
    }
    return false;
  },
  hcl: (hexStr, strict = false) => {
    if (!hexStr) return false;
    if (!strict) return true;
    if (/^#[0-9a-f]{6}$/.test(hexStr)) {
      return true;
    }
    return false;
  },
  ecl: (color, strict = false) => {
    if (!color) return false;
    if (!strict) return true;
    const options = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"];
    if (options.includes(color)) {
      return true;
    }
    return false;
  },
  pid: (idStr, strict = false) => {
    if (!idStr) return false;
    if (!strict) return true;
    if (idStr.length === 9 && parseInt(idStr)) {
      return true;
    }
    return false;
  },
  cid: () => true,
};

async function run() {
  const fileData = await fs.promises.readFile("day4_input.txt", "utf-8");
  const passportStrings = fileData.split("\n\n");
  const passportDataList = passportStrings.map((passStr) =>
    passStr.split(/\s+/).reduce((accum, element) => {
      const [key, value] = element.split(":");
      return {
        ...accum,
        [key]: value,
      };
    }, {}),
  );
  // console.log(passportDataList);

  let numValid = 0;
  let numValidStrict = 0;
  passportDataList.forEach((passData) => {
    const validPass = Object.keys(requirements).every((reqKey) =>
      requirements[reqKey](passData[reqKey]),
    );
    if (validPass) {
      numValid++;
    }
    const validPassStrict = Object.keys(requirements).every((reqKey) =>
      requirements[reqKey](passData[reqKey], true),
    );
    if (validPassStrict) {
      numValidStrict++;
    }
  });

  console.log(`Part 1: ${numValid} out of ${passportDataList.length} total`);
  console.log(`Part 2: ${numValidStrict} out of ${passportDataList.length} total`);
}

run();
