function countMaxOrSubsets(nums: number[]): number {
    let res: number = 0;
    let maxVal: number = nums.reduce((acc: number, num: number) => acc | num, 0);

    const dfs = (id: number, acc: number) => {
        if (id === nums.length) {
            if (acc === maxVal) {
                res += 1;
            }
            return;
        }

        dfs(id+1, acc);
        dfs(id+1, acc | nums[id]);
    };
    dfs(0, 0);

    return res;
};


const test = () => {
    const params = [
        {
            input: {
                nums: [3,1],
            },
            output: 2,
        },
        {
            input: {
                nums: [2,2,2],
            },
            output: 7,
        },
        {
            input: {
                nums: [3,2,1,5],
            },
            output: 6,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums } = input;
        const result = countMaxOrSubsets(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();