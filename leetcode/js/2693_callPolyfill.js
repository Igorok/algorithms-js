/**
 * @param {Object} context
 * @param {Array} args
 * @return {null|boolean|number|string|Array|Object}
 */
Function.prototype.callPolyfill_0 = function(context, ...args) {
    context[this.name] = this;
    return context[this.name](...args);
};

Function.prototype.callPolyfill = function(context, ...args) {
  const smbl = Symbol(this.name);
  context[smbl] = this;
  const r = context[smbl](...args);
  delete context[smbl];
  return r;
}

const test = () => {
    const params = [
        {
            input: {
                fn: function add(b) {
                    return this.a + b;
                },
                args: [{"a": 5}, 7]
            },
            output: 12,
        },
        {
            input: {
                fn: function tax(price, taxRate) {
                    return `The cost of the ${this.item} is ${price * taxRate}`;
                },
                args: [{"item": "burger"}, 10, 1.1],
            },
            output: 'The cost of the burger is 11',
        },
        {
            input: {
                fn: function keys() { return Object.keys(this); },
                args: [{"x": 1, "y": 2}],
            },
            output: ["x","y"],
        },
    ];

    for (const { input, output } of params) {
        const { fn, args } = input;
        const context = args[0];
        const arg = args.slice(1);
        const r = fn.callPolyfill(context, ...arg);

        if (JSON.stringify(r) === JSON.stringify(output)) {
            console.log('SUCCESS \n');
        } else {
            console.log(
                'ERROR',
                'result', r,
                'output', output,
                '\n',
            );
        }
    }
};
test();