#!/usr/bin/node
const result = parseInt(process.argv[2], 10);

if (!isNaN(result)) {
  for (let i = 0; i < result; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
