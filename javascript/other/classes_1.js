
function MyClass (data) {
    this.data = data;
    this.log = function () {
        console.log('data', this.data);
    }
}
const a = new MyClass('aaaaaaaaa');
const b = new MyClass('bbb');
a.log();
b.log();
console.log(a.log === b.log); // false

function MyBareClass (data) {
    this.data = data;
}
MyBareClass.prototype.log = function () {
    console.log('data', this.data);
}
const a1 = new MyBareClass('aaaaaaaaa');
const b1 = new MyBareClass('bbb');
a1.log();
b1.log();
console.log(a1.log === b1.log); // true

function Animal (legs, sound) {
    this.sound = sound;
    this.legs = legs;
}
Animal.prototype.speak = function () {
    console.log(this.sound);
};
function Parrot (legs, sound, wigs) {
    this.sound = sound;
    this.legs = legs;
    this.wigs = wigs;
}
Parrot.prototype = Object.create(Animal.prototype);
Parrot.prototype.constructor = Parrot;
Parrot.prototype.fly = function () {
    console.log('I am flying');
};

function Cat (legs, sound) {
    this.sound = sound;
    this.legs = legs;
}
Cat.prototype = Object.create(Animal.prototype);
Cat.prototype.constructor = Cat;
Cat.prototype.climb = function () {
    console.log('I am climbing on the tree');
};

function Dog (legs, sound) {
    this.sound = sound;
    this.legs = legs;
}
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Parrot;
Dog.prototype.guard = function () {
    console.log('I am guarding the house');
};

const parrot = new Parrot(2, 'Kar kar', 2);
parrot.speak();
parrot.fly();

const cat = new Cat(4, 'Myau Myau');
cat.speak();
cat.climb();

const dog = new Dog(4, 'Gav Gav');
dog.speak();
dog.guard();


class Parent {
    #name = 'parent';
    constructor (name) {
        console.log(1, 'this.#name', this.#name);
        this.#name = name;
        console.log(2, 'this.#name', this.#name);
    }
    hello() {
        // console.log(`Hello my name is ${this.#name}`, (#name in this));
        console.log(`Hello my name is ${this.#name}`);
    }
}
const p = new Parent('John');
// console.log('p.#name', p.#name); // p.#name John
p.hello();

class Child extends Parent {
    #name = 'child';
    buy () {
        // console.log('Goodbuy', this.#name, (#name in this));
        console.log('Goodbuy');
    }
}
const c = new Child('Johny');
c.hello();
// console.log('c.#name', c.#name); // c.#name Johny
c.buy();

/////
class MsgError extends Error {
  constructor(m) {
    super(m);
  }
  sayHello() {
    return "hello " + this.message;
  }
}

const msgError = new MsgError('Error!');
console.log(msgError.sayHello());

