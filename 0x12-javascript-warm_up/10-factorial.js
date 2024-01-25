#!/usr/bin/node
function factorial(n) {
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const arg = parseInt(process.argv[2]);
if (Number.isNaN(arg)) {
  console.log('Factorial of NaN is 1');
} else {
  console.log(factorial(arg));
}
