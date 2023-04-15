#!/usr/bin/node
if ((!process.argv[3]) || (!process.argv[3] && !process.argv[4])) {
    console.log(0);
    process.exit(1);
  }
  
  const findSecond = (arr) => {
    const sortedArr = arr.sort((a, b) => b - a);
    return sortedArr[1];
  };
  
  const argvArr = process.argv.slice(2);
  
  const argvNumeric = argvArr.map(function (value) {
    return parseInt(value);
  });
  
  console.log(findSecond(argvNumeric));
