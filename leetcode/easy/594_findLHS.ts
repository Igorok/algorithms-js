function findLHS(nums: number[]): number {
    let res: number = 0;
    let countOfNums: Map<number, number> = new Map();

    for (const num of nums) {
        const count: number = (countOfNums.get(num) || 0) + 1;
        countOfNums.set(num, count);

        if (countOfNums.has(num - 1)) {
            const countMin: number = countOfNums.get(num - 1) || 0;
            res = Math.max(res, count+countMin);
        }
        if (countOfNums.has(num + 1)) {
            const countMax: number = countOfNums.get(num + 1) || 0;
            res = Math.max(res, count+countMax);
        }
    }

    return res;
};

const test = () => {
    const params = [
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