#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const args = process.argv;
const url = args[2];

request(url, function (error, response, body) {
  if (!error || response.statusCode === 200) {
    const result = JSON.stringify(body);
    fs.writeFile(args[3], JSON.parse(result), 'utf-8', err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
