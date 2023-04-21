#!/usr/bin/node
const args = process.argv;
const request = require('request');
const url = args[2];

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const parseResponse = JSON.parse(body);
    let movies = 0;
    for (const films of parseResponse.results) {
      for (const characters of films.characters) {
        if (characters.includes('18')) {
          movies += 1;
        }
      }
    }
    console.log(movies);
  }
});
