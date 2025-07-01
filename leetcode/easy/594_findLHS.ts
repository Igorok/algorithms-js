function findLHS(nums: number[]): number {
    let res: number = 0;
    const count: Map<number, number> = new Map();

    for (let i: number = 0; i < nums.length; ++i) {
        const countEqual = (count.get(nums[i]) || 0) + 1;
        count.set(nums[i], countEqual);
        const countLess = count.get(nums[i] - 1) || 0;
        if (countLess > 0) {
            res = Math.max(res, countEqual + countLess);
        }
        const countLarge = count.get(nums[i] + 1) || 0;
        if (countLarge > 0) {
            res = Math.max(res, countEqual + countLarge);
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: { nums: [1,2,2,1] },
            output: 4,
        },
        {
            input: { nums: [1,3,2,2,5,2,3,7] },
            output: 5,
        },
        {
            input: { nums: [1,2,3,4] },
            output: 2,
        },
        {
            input: { nums: [1,1,1,1] },
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums } = input;

        const result = findLHS(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();