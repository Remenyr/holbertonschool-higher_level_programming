#!/usr/bin/node
function recursiveFactorial (num) {
    if (num === 1) {
      return 1;
    } else {
      return num * recursiveFactorial(num - 1);
    }
  }
  
  const number = parseInt(process.argv[2]) || 1;
  
  console.log(recursiveFactorial(number));
