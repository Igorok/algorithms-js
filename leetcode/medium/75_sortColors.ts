/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
    const count: number[] = new Array(3).fill(0);
    for (const num of nums) {
        count[num] += 1;
    }

    for (let i: number = 0; i < nums.length; ++i) {
        for (let j: number = 0; j < 3; ++j) {
            if (count[j] !== 0) {
                nums[i] = j;
                count[j] -= 1;
                break;
            }
        }
    }
};

const test = () => {
    const params = [
        {
            input: {nums: [2,0,2,1,1,0]},
            output: [0,0,1,1,2,2],
        },
        {
            input: {nums: [2,0,1]},
            output: [0,1,2],
        },
    ];

    params.forEach(({input, output}) => {
        const {nums} = input;
        const result = sortColors(nums);

        console.log(
            JSON.stringify(nums) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', nums,
        );
    });
};

test();