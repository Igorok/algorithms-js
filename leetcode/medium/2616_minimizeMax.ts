function minimizeMax(nums: number[], p: number): number {
    nums.sort((a, b) => a - b);

    const getPairsCount = (maxDiff: number): number => {
        let res: number = 0;
        let i: number = 0;
        while (i < nums.length-1) {
            if (nums[i+1] - nums[i] <= maxDiff) {
                res += 1;
                i += 2;
                continue;
            }

            i += 1;
        }
        return res;
    }

    let left: number = 0;
    let right: number = nums.at(-1) - nums[0];
    let res: number = Number.MAX_SAFE_INTEGER;

    while (left <= right) {
        const middle: number = Math.floor((left + right) / 2);
        if (getPairsCount(middle) >= p) {
            res = middle;
            right = middle - 1;
        } else {
            left = middle + 1;
        }
    }

    return res;
};

/*

1,3, 4,4, 7,10

1,3
3,4
4,4
4,7,
7,10


*/

const test = () => {
    const params = [
        {
            input: { nums: [10,1,2,7,1,3], p: 2 },
            output: 1,
        },
        {
            input: { nums: [4,2,1,2], p: 1 },
            output: 0,
        },
        {
            input: { nums: [1,3, 4,4, 7,10], p: 3 },
            output: 3,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums, p } = input;
        const result = minimizeMax(nums, p);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();