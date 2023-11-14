#!/usr/bin/node
const argName = process.argv[2];

if (argName) {
  console.log(argName);
} else {
  console.log('No argument');
}
