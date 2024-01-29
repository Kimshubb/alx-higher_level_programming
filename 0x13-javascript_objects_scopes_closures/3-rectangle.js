#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w > 0 && Number.isinteger(w) && (h > 0 && Number.isinteger(h)) {
      this.width = w;
      this.width = h;
    } else {
    return {}
    }
  }
  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}
