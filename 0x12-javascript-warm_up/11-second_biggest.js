#!/usr/bin/node
const args = process.argv.slice[2];
const numbers = args.map(Number);
const sortedNumbers = numbers.sort((a, b) => b - a);

if (sortedNumber.length < 2) {
  console.log(0);
} else {
  console.log(sortedNumbers[1]);
}
