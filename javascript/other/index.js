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

console.log("getX", getX);
function getX() {}

// ReferenceError: Cannot access 'getY' before initialization
// console.log("getY", getY);
// const getY = () => {};
