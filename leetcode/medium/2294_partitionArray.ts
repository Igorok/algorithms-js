function partitionArray(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);

    let res: number = 1;
    let start = nums[0] + k;

    for (const num of nums) {
        if (num > start) {
            res += 1;
            start = num + k;
        }
    }

    return res;
};


const test = () => {
    const params = [
        {
            input: {
                nums: [3,6,1,2,5], k: 2,
            },
            output: 2,
        },
        {
            input: {
                nums: [1,2,3], k: 1,
            },
            output: 2,
        },
        {
            input: {
                nums: [2,2,4,5], k: 0,
            },
            output: 3,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums, k } = input;
        const result = partitionArray(nums, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();