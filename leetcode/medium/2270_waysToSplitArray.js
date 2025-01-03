/**
 * @param {number[]} nums
 * @return {number}
 */
var waysToSplitArray = function(nums) {
    const postfix = new Array(nums.length).fill(0);
    postfix[postfix.length - 1] = nums.at(-1);
    for (let i = nums.length - 2; i > -1; --i) {
        postfix[i] = nums[i] + postfix[i + 1];
    }

    let res = 0;
    let acc = 0;
    for (let i = 0; i < nums.length - 1; ++i) {
        acc += nums[i];
        if (acc >= postfix[i+1]) {
            res += 1;
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: [10,4,-8,7],
            output: 2,
        },
        {
            input: [2,3,1,0],
            output: 2,
        },
    ];

    params.forEach(({input, output}) => {
        const result = waysToSplitArray(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();