#!/usr/bin/node
const result = parseInt(process.argv[2], 10);

if (!isNaN(result) && result > 0) {
  for (let i = 0; i < result; i++) {
    console.log('X'.repeat(result));
  }
} else {
  console.log('Missing size');
}
