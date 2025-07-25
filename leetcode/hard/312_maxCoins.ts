function maxCoins_0(nums: number[]): number {
    const memo: Map<string, number> = new Map();

    const dfs = (arr: number[]) => {
        if (!arr.length) {
            return 0;
        }
        const key = arr.join('_');
        if (memo.has(key)) {
            return memo.get(key);
        }

        let res: number = 0;

        for (let i: number = 0; i < arr.length; ++i) {
            const left: number = i > 0 ? arr[i-1] : 1;
            const right: number = i < arr.length - 1 ? arr[i+1] : 1;
            let r: number = arr[i] * left * right;

            const lPart = i === 0 ? [] : arr.slice(0, i);
            const rPart = i === arr.length - 1 ? [] : arr.slice(i+1);
            r += dfs([...lPart, ...rPart]);

            res = Math.max(res, r);
        }

        memo.set(key, res);

        return res;
    }

    return dfs(nums);
};

/*
0
[3,1,5,8]
15
[3,5,8]
15 + 3*5*8=135
[3,8]
135+24=159
[8]
159+8=167
[]

---

[1, 3,1,5,8, 1]
1*8*1
[1, 3,1,5, 8]   [1]
8+ 1*3*8 = 32
[1, 3,1,5, 8]   [1]
32+ 3*5*8 = 32+120 = 152
[1,] [3, 1,5, 8]   [1]
152 + 3*1*5 = 167
[1,] [3, 1, 5], [8]   [1]
167
[1,] [3], [1], [5], [8]   [1]

*/

function maxCoins(nums: number[]): number {
    const arr: number[] = [1, ...nums, 1];
    const memo: number[][] = new Array(arr.length).fill(0).map(() => new Array(arr.length).fill(-1));

    const dfs = (left: number, right: number): number => {
        if (left > right) {
            return 0;
        }

        if (memo[left][right] !== -1) {
            return memo[left][right];
        }

        let res: number = -1;

        for (let i: number = left; i <= right; ++i) {
            let num: number = arr[left-1] * arr[i] * arr[right+1];
            num += dfs(left, i-1);
            num += dfs(i+1, right);

            res = Math.max(res, num);
        }

        memo[left][right] = res;

        return res;
    }

    return dfs(1, arr.length - 2);
};


const test = () => {
    const params = [
        {
            input: {
                nums: [3,1,5,8],
            },
            output: 167,
        },
        {
            input: {
                nums: [1,5],
            },
            output: 10,
        },
        {
            input: {
                nums: [8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2],
            },
            output: 167,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums } = input;

        const result = maxCoins(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();