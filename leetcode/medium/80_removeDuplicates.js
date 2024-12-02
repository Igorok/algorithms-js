/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    const limit = 2;
    let count = 1;
    let id = 1;
    let tmp = nums[0];
    for (let i = 1; i < nums.length; ++i) {
        if (nums[i] === tmp) {
            if (count >= limit) {
                continue;
            }
            nums[id] = nums[i];
            id += 1;
            count += 1;
        } else {
            tmp = nums[i]
            nums[id] = tmp;
            count = 1;
            id += 1;
        }
    }

    // nums.length = id;
    return nums.slice(0, id);
};

const test = () => {
    const params = [
        {
            input: [1,1,1,2,2,3],
            output: [1,1,2,2,3],
        },

        {
            input: [0,0,1,1,1,1,2,3,3],
            output: [0,0,1,1,2,3,3],
        },
    ];

    params.forEach(({input, output}) => {
        const result = removeDuplicates([...input]);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();