function lengthOfLIS(nums: number[]): number {
    const memo: number[] = [];

    for (const num of nums) {
        if (memo.length === 0) {
            memo.push(num);
            continue;
        }

        if (num > memo.at(-1)) {
            memo.push(num);
            continue;
        }

        let i: number = memo.length - 1;
        while (memo[i] >= num) {
            i -= 1;
        }
        memo[i+1] = num;
    }

    return memo.length;
};

const test = () => {
    const params = [
        {
            input: {
                nums: [10,9,2,5,3,7,101,18],
            },
            output: 4,
        },
        {
            input: {
                nums: [0,1,0,3,2,3],
            },
            output: 4,
        },
        {
            input: {
                nums: [7,7,7,7,7,7,7],
            },
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums } = input;
        const result = lengthOfLIS(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();