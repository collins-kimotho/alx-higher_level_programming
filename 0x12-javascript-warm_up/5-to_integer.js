#!/usr/bin/node
const firstArg = process.argv[2];

// Attempt to convert the first argument to an integer
const parsedInt = parseInt(firstArg);

if (!isNaN(parsedInt)) {
  console.log(`My number: ${parsedInt}`);
} else {
  console.log('Not a number');
}
