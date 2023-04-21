#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
    let occur = 0;
    for (const item of list) {
      if (item === searchElement) {
        occur += 1;
      }
    }
    return occur;
  };
