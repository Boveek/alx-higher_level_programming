#!/usr/bin/node
const numArgs = process.argv.length - 2;

if (numArgs === 0) {
  console.log('undefined is undefined');
} else if (numArgs === 1) {
  console.log(process.argv[2] + ' is undefined');
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
