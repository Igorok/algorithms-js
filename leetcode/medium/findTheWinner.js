/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findTheWinner = function(n, k) {
    const queue = [];
    for (let i = 1; i <= n; ++i) {
        queue.push(i);
    }

    let i = 0;
    while (queue.length) {
        if (queue.length === 1) return queue[0];

        i+= 1;
        const val = queue.shift();

        if (i === k) {
            i = 0;
        } else {
            queue.push(val);
        }
    }

};

const test = () => {
    const params = [
        {
            input: [5, 2],
            output: 3,
        },
        {
            input: [6, 5],
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const result = findTheWinner(...input);

        console.log(
            result === output ? 'SUCCESS ' : 'ERROR ',
            'input', input,
            'output', output,
            'result', result,
        );

    });
};

test();
