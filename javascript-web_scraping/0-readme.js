#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

fs.readFile(args[2], 'utf8', (error, data) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(data);
});
