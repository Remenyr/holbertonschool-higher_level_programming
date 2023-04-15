#!/usr/bin/node
if (!parseInt(process.argv.slice(2)[0])) {
    console.log('Missing size');
  }
  
  const size = parseInt(process.argv.slice(2)[0]);
  
  if (size < 0) {
    process.exit(1);
  }
  
  const sign = 'X';
  
  const modSign = sign.repeat(size);
  
  for (let i = 0; i < size; i++) {
    console.log(modSign);
  }
