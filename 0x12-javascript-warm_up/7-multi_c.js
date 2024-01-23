#!/usr/bin/node
const arg1 = process.argv[2];
const count = parseInt(arg1);

if (!isNaN(count)) {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
