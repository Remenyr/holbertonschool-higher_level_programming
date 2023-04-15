#!/usr/bin/node
if (parseInt(process.argv.slice(2)[0])) {
    console.log(`My number: ${parseInt(process.argv.slice(2)[0])}`);
  } else {
    console.log('Not a number');
  }
  