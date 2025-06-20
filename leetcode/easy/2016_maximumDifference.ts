function maximumDifference(nums: number[]): number {
    let min: number = nums[0];
    let res: number = -1;

    for (let i: number = 1; i < nums.length; ++i) {
        if (nums[i] > min) {
            res = Math.max(res, nums[i] - min);
        }

        min = Math.min(min, nums[i]);
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                nums: [7,1,5,4],
            },
            output: 4,
        },
        {
            input: {
                nums: [9,4,3,2],
            },
            output: -1,
        },
        {
            input: {
                nums: [1,5,2,10],
            },
            output: 9,
        },
        {
            input: {
                nums: [7,7,5,4],
            },
            output: -1,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums } = input;
        const result = maximumDifference(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

