#!/usr/bin/node

exports.converter = function (base) {
    function toConvert (num) {
      return num.toString(base);
    }
    return toConvert;
  };
