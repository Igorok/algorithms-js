function permuteUnique(nums: number[]): number[][] {
    const res: number[][] = [];
    const unique: Set<string> = new Set();
    const visited: number[] = new Array(nums.length).fill(0);

    const rec = (acc: number[]): void => {
        if (acc.length === nums.length) {
            const key: string = acc.join('_');
            if (!unique.has(key)) {
                res.push([...acc]);
                unique.add(key);
            }
            return;
        }

        for (let i: number = 0; i < nums.length; ++i) {
            if (visited[i] !== 0) {
                continue;
            }
            visited[i] = 1;
            acc.push(nums[i]);

            rec(acc);

            acc.pop();
            visited[i] = 0;
        }

    };

    rec([]);

    return res;
};

const test = () => {
    const params = [
        {
            input: { nums: [1,1,2] },
            output: [
                [1,1,2],
                [1,2,1],
                [2,1,1]
            ],
        },
        {
            input: { nums: [1,2,3] },
            output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]],
        },
    ];

    params.forEach(({input, output}) => {
        const { nums } = input;
        const result = permuteUnique(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();