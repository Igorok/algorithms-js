// var behavior
// let, const ReferenceError: x is not defined
if (true) {
  var x = 1;
}
console.log("x", x);

// hoisting
// let, const ReferenceError: Cannot access 'y' before initialization
// Temporal dead zone (TDZ)
console.log("y", y);
var y = 2;

console.log("getX", getX, getX());
function getX() {
  return "I'm getX";
}

// ReferenceError: Cannot access 'getY' before initialization
// console.log("getY", getY);
// const getY = () => {};


// loop labels
(() => {
  let x1 = 0;
  let y1 = 0;
  while1: while (true) {
    x1 += 100;

    while2: while (true) {
      if (x1 >= 300) break while1;
      y1 += 1;
      if (y1 > 0 && (y1 % 10) === 0) break while2;
    }
  }

  console.log({ x1, y1 });
})();

/*

console.log(undefined)
test = 1
test = 2
test = 5
console.log(test)
++test

*/
run();

async function run() {
  console.log(test);
  test = 1;

  while (++test < 10) {
    await new Promise((resolve) =>
      setTimeout(() => {
        console.log(test);
        resolve();
      }, 100)
    );
  }
}

var test = 5;