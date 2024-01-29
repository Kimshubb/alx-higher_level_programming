#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.width = h;
    }
  }
  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
	let s = '';
	for (let j = 0; j < this.width; j++) {
	  s += 'X';
	}
        console.log(s);
      }
    }
  }
}
module.exports = Rectangle;
