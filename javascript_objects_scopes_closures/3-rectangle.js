#!/usr/bin/node

module.exports = class Rectangle {
    constructor (w, h) {
      if (Number.isInteger(w, h) && h > 0 && w > 0) {
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      for (let h = 0; h < this.height; h++) {
        for (let w = 0; w < this.width; w++) {
          process.stdout.write('X');
        }
        process.stdout.write('\n');
      }
    }
  };
