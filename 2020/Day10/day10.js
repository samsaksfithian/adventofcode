const fs = require("fs");

async function run() {
  const fileData = await fs.promises.readFile("day10_exampleinput2.txt", "utf-8");
  // const fileData = await fs.promises.readFile("day10_exampleinput.txt", "utf-8");
  // const fileData = await fs.promises.readFile("day10_input.txt", "utf-8");
  const joltageVals = fileData
    .split("\n")
    .map((numStr) => Number(numStr))
    .sort((a, b) => a - b);
  joltageVals.unshift(0);
  joltageVals.push(joltageVals[joltageVals.length - 1] + 3);
  // console.log(joltageVals);

  const arrangements = await recurseFindArrangement(0, joltageVals);
  console.log(`Part 2: # possible arrangements = ${arrangements}`);
}

// NOTE: attempt to see if running it async would make it faster
//    didn't work, needs to use memoization/dynamic programming
async function recurseFindArrangement(startIndex, dataList) {
  if (startIndex === dataList.length - 1) {
    return 1;
  }
  const currVal = dataList[startIndex];
  const recursePromises = [];
  for (let diff = 1; diff <= 3; diff++) {
    const diffIndex = dataList.indexOf(currVal + diff, startIndex);
    if (diffIndex >= 0) {
      recursePromises.push(recurseFindArrangement(diffIndex, dataList));
    }
  }
  return Promise.all(recursePromises).then((subcounts) =>
    subcounts.reduce((acc, num) => acc + num, 0),
  );
}

run();
