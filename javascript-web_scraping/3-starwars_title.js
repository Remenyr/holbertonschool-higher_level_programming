#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/' + args[2];

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const result = JSON.parse(body);
    console.log(result.title);
  }
});
