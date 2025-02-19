const calculatorMixin = (Base) => class extends Base {
    calc(x, y) {
        return x * y;
    }
 };
const randomizerMixin = (Base) => class extends Base {
    randomize() {
        return Math.random();
    }
};
class Foo {
    constructor (x, y) {
        this.x = x;
        this.y = y;
    }
}
class Bar extends calculatorMixin(randomizerMixin(Foo)) {}

const b = new Bar(3, 4);
console.log('randomize', b.randomize());
console.log('calc', b.calc(b.x, b.y));


