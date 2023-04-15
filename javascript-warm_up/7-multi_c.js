#!/usr/bin/node
const str = 'C is fun';

if (!parseInt(process.argv.slice(2)[0])) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < parseInt(process.argv.slice(2)[0]); i++) {
  console.log(str);
}
