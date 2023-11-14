#!/usr/bin/node
const numArgs = process.argv.length - 2;

if (numArgs === 0) {
  console.log('Not a number');
} else {
  const result = parseInt(process.argv[2], 10);
  if (result) {
    console.log('My number:', result);
  } else {
    console.log('Not a number');
  }
}
