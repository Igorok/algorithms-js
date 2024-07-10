/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    const frequency = Math.floor(nums.length / 2);
    const memo = new Map();
    for (const n of nums) {
        const count = (memo.has(n) ? memo.get(n) : 0) + 1;

        if (count > frequency) return n;

        memo.set(n, count);
    }
};

const test = () => {
    const params = [
        {
            input: [3,2,3],
            output: 3,
        },
        {
            input: [2,2,1,1,1,2,2],
            output: 2,
        },
    ];

    params.forEach(({input, output}) => {
        const result = majorityElement(input);

        console.log(
            result === output ? 'SUCCESS ' : 'ERROR ',
            'input', input,
            'output', output,
            'result', result,
        );

    });
};

test();
