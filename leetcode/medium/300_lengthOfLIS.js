/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    if (!nums?.length) return 0;

    let res = 1;
    const sequence = new Array(nums.length).fill(1);

    for (let i = 0; i < nums.length; ++i) {
        for (let j = i-1; j > -1; --j) {
            if (nums[j] < nums[i]) {
                sequence[i] = Math.max(sequence[i], sequence[j] + 1);
                res = Math.max(res, sequence[i]);
            }
        }
    }

    return res;
};


const test = () => {
    const params = [
        {
            input: [10,9,2,5,3,7,101,18],
            output: 4,
        },
        {
            input: [0,1,0,3,2,3],
            output: 4,
        },
        {
            input: [7,7,7,7,7,7,7],
            output: 1,
        }
    ];

    params.forEach(({input, output}) => {
        const result = lengthOfLIS(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();