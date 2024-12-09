/**
 * @param {number[]} banned
 * @param {number} n
 * @param {number} maxSum
 * @return {number}
 */
var maxCount = function(banned, n, maxSum) {
    const ban = new Set(banned);

    let sum = 0;
    let count = 0;
    for (let i = 1; i <= n; ++i) {
        if (sum + i > maxSum) {
            break;
        }
        if (!ban.has(i)) {
            sum += i;
            count += 1;
        }
    }
    return count;
};

/*



*/

const test = () => {
    const params = [
        {
            input: [[1,6,5], 5, 6],
            output: 2,
        },
        {
            input: [[1,2,3,4,5,6,7], 8, 1],
            output: 0,
        },
        {
            input: [[11], 7, 50],
            output: 7,
        },
    ];

    params.forEach(({input, output}) => {
        const result = maxCount(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();