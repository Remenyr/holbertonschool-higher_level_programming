#!/usr/bin/node

let executions = 0;
exports.logMe = function (item) {
  console.log(executions + ': ' + item);
  executions += 1;
};
