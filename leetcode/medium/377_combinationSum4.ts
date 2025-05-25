function combinationSum4_0(nums: number[], target: number): number {
    const memo: Set<string> = new Set();

    const checkTarget = (acc: number[], sum: number): void => {
        if (sum > target) {
            return;
        }
        if (sum === target) {
            memo.add(acc.join('_'));
            return;
        }

        for (const num of nums) {
            acc.push(num);
            sum += num;

            checkTarget(acc, sum);

            acc.pop();
            sum -= num;
        }

    };

    checkTarget([], 0);

    return memo.size;
};


function combinationSum4(nums: number[], target: number): number {
    const memo: Map<number, number> = new Map();

    const getComb = (val: number): number => {
        if (val < 0) {
            return 0;
        }
        if (val === 0) {
            return 1;
        }
        if (memo.has(val)) {
            return memo.get(val);
        }

        let res: number = 0;
        for (const num of nums) {
            const r: number = getComb(val - num);
            res += r;
        }

        memo.set(val, res);

        return res;
    };

    return getComb(target);
};


const test = () => {
    const params = [
        {
            input: { nums: [4,2,1], target: 32 },
            output: 39882198,
        },
        {
            input: { nums: [1,2,3], target: 4 },
            output: 7,
        },
        {
            input: { nums: [9], target: 3 },
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums, target } = input;
        const result = combinationSum4(nums, target);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();