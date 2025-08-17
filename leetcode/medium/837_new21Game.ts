function new21Game_0(n: number, k: number, maxPts: number): number {
    const prob: number = 1 / maxPts;
    const min: number = 10**(-15);

    const memo: Map<string, number> = new Map();

    const dfs = (acc: number, accProb: number, steps: number): number => {
        if (acc > n) return 0;
        if (acc >= k) {
            return acc <= n ? accProb : 0;
        }

         if (steps > 30) {
            return acc <= n ? accProb : 0;
        }

        // if (accProb < min) {
        //     return acc <= n ? accProb : 0;
        // }

        const key = `${acc}_${accProb}`;

        if (memo.has(key)) {
            return memo.get(key);
        }

        let res: number = 0;

        for (let point: number = 1; point <= maxPts; ++point) {
            if (acc + point > n) break;

            let r: number = dfs(acc + point, accProb * prob, steps + 1);
            res += r;
        }

        memo.set(key, res);

        return res;
    }

    return dfs(0, 1, 0);
};


function new21Game_1(n: number, k: number, maxPts: number): number {
    if (k === 0) return 1;

    const memo: number[] = new Array(n+1).fill(0);
    memo[0] = 1;

    for (let num: number = 1; num <= n; ++num) {
        for (let point: number = 1; point <= maxPts; ++point) {
            const prevNum: number = num - point;
            if (prevNum < 0) break;
            if (prevNum >= k) continue;

            memo[num] += memo[prevNum] / maxPts;
        }
    }


    let res: number = 0;
    for (let i: number = k; i < memo.length; ++i) {
        res += memo[i];
    }

    return res;
};


function new21Game(n: number, k: number, maxPts: number): number {
    if (k === 0) return 1;

    const memo: number[] = new Array(n+1).fill(0);
    memo[0] = 1;

    let sum: number = 1;
    for (let num: number = 1; num <= n; ++num) {
        memo[num] = sum / maxPts;
        if (num < k) {
            sum += memo[num];
        }

        if (num - maxPts >= 0 && num - maxPts < k) {
            sum -= memo[num - maxPts];
        }
    }

    let res: number = 0;
    for (let i: number = k; i < memo.length; ++i) {
        res += memo[i];
    }

    return res;
};




const test = () => {
    const params = [
        {
            input: {
                n: 0, k: 0, maxPts: 1
            },
            output: 1,
        },
        {
            input: {
                n: 9811, k: 8776, maxPts: 1096
            },
            output: 0.99696,
        },
        {
            input: {
                n: 421, k: 0, maxPts: 47
            },
            output: 1,
        },
        {
            input: {
                n: 421, k: 400, maxPts: 47
            },
            output: 0.71188,
        },
        {
            input: {
                n: 10, k: 1, maxPts: 10
            },
            output: 1.00000,
        },
        {
            input: {
                n: 6, k: 1, maxPts: 10
            },
            output: 0.60000,
        },
        {
            input: {
                n: 21, k: 17, maxPts: 10
            },
            output: 0.73278,
        },
    ];

    params.forEach(({input, output}) => {
        const { n, k, maxPts } = input;
        const result = new21Game(n, k, maxPts);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();