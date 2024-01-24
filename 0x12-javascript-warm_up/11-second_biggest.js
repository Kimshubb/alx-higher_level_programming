#!/usr/bin/node
const findSecondLargest = (args) => {
  const numbers = args.map(Number);
  if (numbers.length <= 1) {
    return 0;
  }
  numbers.sort((a, b) => b - a);
  return numbers[1];
};
const args = process.argv.slice[2];
console.log(findSecondLargest(args));
