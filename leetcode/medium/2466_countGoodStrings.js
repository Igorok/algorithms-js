/**
 * @param {number} low
 * @param {number} high
 * @param {number} zero
 * @param {number} one
 * @return {number}
 */
var countGoodStrings = function(low, high, zero, one) {
    const mod = 7 + 10e8;
    const cache = new Array(high+1).fill(-1);
    const rec = (id) => {
        if (id > high) {
            return 0;
        }

        if (cache[id] !== -1) {
            return cache[id];
        }

        if (id === high) {
            return 1;
        }

        let res = 0;
        if (id >= low) {
            res += 1;
        }

        res += rec(id + zero)
        res += rec(id + one);
        res %= mod;

        cache[id] = res;

        return res;
    };

    return rec(0);
};

const test = () => {
    const params = [
        {
            input: [3, 3, 1, 1],
            output: 8,
        },
        {
            input: [2, 3, 1, 2],
            output: 5,
        },
        {
            input: [200, 200, 10, 1],
            output: 764262396,
        },
    ];

    params.forEach(({input, output}) => {
        const result = countGoodStrings(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();