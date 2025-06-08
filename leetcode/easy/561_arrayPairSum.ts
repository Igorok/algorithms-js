function arrayPairSum(nums: number[]): number {
    nums.sort((a, b) => a - b);

    let res: number = 0;

    for (let i: number = 0; i < nums.length; i += 2) {
        res += nums[i];
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                nums: [1,4,3,2]
            },
            output: 4,
        },
        {
            input: {
                nums: [6,2,6,5,1,2]
            },
            output: 9,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums } = input;
        const result = arrayPairSum(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();