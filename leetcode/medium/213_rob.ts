function rob(nums: number[]): number {
    if (nums.length === 1) return nums[0];
    const cache: Map<string, number> = new Map();
    let res: number = 0;

    const getSum = (id: number, isFirst: boolean): number => {
        if (id === nums.length - 1 && isFirst) {
            return 0;
        }
        if (id >= nums.length) {
            return 0;
        }

        const key = `${id}_${isFirst}`;
        if (cache.has(key)) {
            return cache.get(key);
        }

        let r1: number = nums[id] + getSum(id + 2, isFirst);
        let r2: number = getSum(id + 1, isFirst);

        const r: number = Math.max(r1, r2);
        cache.set(key, r);

        return r;
    };

    for (let i = 0; i < nums.length; ++i) {
        const r: number = getSum(i, i === 0);
        res = Math.max(res, r);
    }

    return res;
};

/*

1 2 3 4 5 6 7
1+3+5 = 9
2+4+6 = 12
2+5+7 = 14
3+5+7 = 15


*/

const test = () => {
    const params = [
        {
            input: {
                nums: [1,2]
            },
            output: 2,
        },
        {
            input: {
                nums: [1]
            },
            output: 1,
        },
        {
            input: {
                nums: [2,3,2]
            },
            output: 3,
        },
        {
            input: {
                nums: [1,2,3,1]
            },
            output: 4,
        },
        {
            input: {
                nums: [1,2,3]
            },
            output: 3,
        },
        {
            input: {
                nums: [1,2,3,4,5,6,7,]
            },
            output: 15,
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