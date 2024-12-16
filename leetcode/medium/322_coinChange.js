/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    if (amount === 0) {
        return 0
    }

    const arr = coins.sort((a, b) => a - b);
    const memo = new Array(amount + 1).fill(Number.MAX_SAFE_INTEGER);
    memo[0] = 0;

    for (let i = 1; i <= amount; ++i) {
        for (const coin of arr) {
            if (coin > i) break;

            memo[i] = Math.min(memo[i], 1 + memo[i - coin]);
        }
    }

    return (memo[amount] === Number.MAX_SAFE_INTEGER) ? -1 : memo[amount];
};

const test = () => {
    const params = [
        {
            input: [[1,2,5], 11],
            output: 3,
        },

        {
            input: [[2], 3],
            output: -1,
        },
        {
            input: [[1], 0],
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const result = coinChange(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();