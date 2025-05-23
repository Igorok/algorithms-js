function rob(nums: number[]): number {
    let prev: number = 0;
    let prevPrev: number = 0;
    for (let i = 0; i < nums.length; ++i) {
        const curr: number = Math.max(prevPrev + nums[i], prev);
        prevPrev = prev;
        prev = curr;
    }

    return prev;
};

const test = () => {
    const params = [
        {
            input: {
                nums: [2,1]
            },
            output: 2,
        },
        {
            input: {
                nums: [0]
            },
            output: 0,
        },
        {
            input: {
                nums: [1,2,3,1]
            },
            output: 4,
        },
        {
            input: {
                nums: [2,7,9,3,1]
            },
            output: 12,
        },

    ];

    params.forEach(({input, output}) => {
        const { nums } = input;
        const result = rob(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();