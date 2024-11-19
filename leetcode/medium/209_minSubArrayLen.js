/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let start = 0;
    let end = 0;

    let sum = nums[0];
    let res = nums.length + 1;
    while (end !== nums.length) {

        while (sum >= target) {
            if (end - start === 0) {
                return 1;
            }

            res = Math.min(res, (end - start + 1));
            sum -= nums[start];
            start += 1;
        }

        end += 1;
        if (end < nums.length) {
            sum += nums[end];
        }
    }

    return res === nums.length + 1 ? 0 : res;
};

const test = () => {
    const params = [
        {
            input: [7, [2,3,1,2,4,3]],
            output: 2,
        },

        {
            input: [4, [1,4,4]],
            output: 1,
        },
        {
            input: [11, [1,1,1,1,1,1,1,1]],
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const result = minSubArrayLen(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();