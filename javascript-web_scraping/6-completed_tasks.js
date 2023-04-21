#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = args[2];

request(url, function (error, response, body) {
  if (!error || response.statusCode === 200) {
    const result = JSON.parse(body);
    const completed = {};

    for (const task of result) {
      if (!(task.userId in completed)) {
        completed[task.userId] = 0;
      }
      if (task.completed === true) {
        completed[task.userId] += 1;
      }
    }

    const copy = completed;
    const ids = Object.keys(copy);
    for (let i = 1; i <= ids.length; i++) {
      if (copy[i] === 0) {
        delete completed[i];
      }
    }
    console.log(completed);
  }
});
