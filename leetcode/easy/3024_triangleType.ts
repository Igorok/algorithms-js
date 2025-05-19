function triangleType(nums: number[]): string {
    nums.sort((a, b) => a - b);

    if (nums[0] + nums[1] <= nums[2]) {
        return 'none';
    }
    if (nums[0] === nums[2]) {
        return 'equilateral';
    } else if (nums[0] === nums[1] || nums[1] === nums[2]) {
        return 'isosceles';
    }
    return 'scalene';
};

const test = () => {
    const params = [
        {
            input: { nums: [9,4,9] },
            output: 'isosceles',
        },
        {
            input: { nums: [3,3,3] },
            output: 'equilateral',
        },
        {
            input: { nums: [3,4,5] },
            output: 'scalene',
        },

    ];

    params.forEach(({input, output}) => {
        const { nums } = input;

        const result = triangleType(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();