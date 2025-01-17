/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    const memo = new Set();
    const rec = (_n) => {
        if (memo.has(_n)) {
            return false;
        }
        memo.add(_n);

        let num = _n;
        let sum = 0;
        while (num !== 0) {
            sum += (num % 10)**2;
            num = Math.floor(num / 10);
        }
        if (sum === 1) {
            return true;
        }
        return rec(sum);
    };

    return rec(n);
};

const test = () => {
    const params = [
        {
            input: 19,
            output: true,
        },
        {
            input: 2,
            output: false,
        },
    ];

    params.forEach(({input, output}) => {
        const result = isHappy(input);

        console.log(
            result === output ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();