#!/usr/bin/node
const square = require('./5-square');

module.exports = class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let h = 0; h < this.height; h++) {
        for (let w = 0; w < this.width; w++) {
          process.stdout.write(c);
        }
        process.stdout.write('\n');
      }
    } else {
      super.print();
    }
  }
};
