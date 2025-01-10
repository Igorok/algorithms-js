
var RandomizedSet = function() {
    this.map = new Map();
    this.arr = [];
};

/**
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function(val) {
    if (this.map.has(val)) {
        return false;
    }

    this.arr.push(val);
    this.map.set(val, this.arr.length - 1);

    return true;
};

/**
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function(val) {
    if (!this.map.has(val)) {
        return false;
    }

    const tmp = this.arr.pop();

    if (tmp !== val) {
        const id = this.map.get(val);
        this.arr[id] = tmp;
        this.map.set(tmp, id);
    }

    this.map.delete(val);

    return true;
};

/**
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function() {
    const id = Math.floor(Math.random() * this.arr.length);
    return this.arr[id];
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */



const test = () => {
    const params = [
        {
            input: [
                ["insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],
                [[1], [2], [2], [], [1], [2], []]
            ],
            output: [true, false, true, 2, true, false, 2],
        },
    ];

    params.forEach(({input, output}) => {
        const randomizedSet = new RandomizedSet();
        for (let i = 0; i < input[0].length; ++i) {
            const fn = input[0][i];
            const param = input[1][i]?.[0];
            const out = output[i];

            const result = randomizedSet[fn](param);
            console.log(
                JSON.stringify(result) === JSON.stringify(out) ? 'SUCCESS ' : 'ERROR ',
                'input', JSON.stringify(input[0][i]),
                'output', out,
                'result', result,
            );
        }
    });
};

test();