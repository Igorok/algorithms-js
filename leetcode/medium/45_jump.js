/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    if (nums.length === 1) return 0;

    const findSteps = (id, count) => {
        if (id + nums[id] >= nums.length - 1) {
            return count;
        }

        let nextId = id;
        for (let i = id; i <= (id + nums[id]); ++i) {
            if (i + nums[i] > nextId + nums[nextId]) {
                nextId = i;
            }
            if (nextId + nums[nextId] >= nums.length - 1) {
                break;
            }
        }
        return findSteps(nextId, count + 1);
    };

    return findSteps(0, 1);



};


const test = () => {
    const params = [
        {
            input: [2,3,1,1,4],
            output: 2,
        },
        {
            input: [2,3,0,1,4],
            output: 2,
        },
        {
            input: [0],
            output: 0,
        },
        {
            input: [1,1,1,1],
            output: 3,
        },
    ];

    params.forEach(({input, output}) => {
        const result = jump(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();