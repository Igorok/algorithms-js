function findDisappearedNumbers(nums: number[]): number[] {
    const memo: number[] = new Array(nums.length + 1).fill(0);

    for (const n of nums) {
        if (n < memo.length) {
            memo[n] = 1;
        }
    }

    const res: number[] = [];
    for (let i: number = 1; i < memo.length; ++i) {
        if (memo[i] === 0) {
            res.push(i);
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: [4,3,2,7,8,2,3,1],
            output: [5,6],
        },
        {
            input: [1,1],
            output: [2],
        },
    ];

    params.forEach(({input, output}) => {
        const result = findDisappearedNumbers(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();