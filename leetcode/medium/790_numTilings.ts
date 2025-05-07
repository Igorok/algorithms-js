function numTilings_0(n: number): number {
    const mod: number = 7 + 10e8;

    const memoOdd: number[] = new Array(n+1).fill(0);
    memoOdd[2] = 2;
    memoOdd[3] = 4;
    const memoEven: number[] = new Array(n+1).fill(0);
    memoEven[1] = 1;
    memoEven[2] = 2;
    memoEven[3] = 5;

    for (let i = 4; i <= n; ++i) {
        memoOdd[i] = memoOdd[i-1];
        memoOdd[i] += memoEven[i-1];
        memoOdd[i] %= mod;

        memoEven[i] = memoEven[i-1];
        memoEven[i] %= mod;
        memoEven[i] += memoEven[i-2] % mod;
        memoEven[i] %= mod;
        memoEven[i] += (memoEven[i-3]*2) % mod;
        memoEven[i] %= mod;
        memoEven[i] += memoOdd[i-1];
        memoEven[i] %= mod;
    }



    return memoEven[n];
};

/*
a
*
*
b
**
c
*
**
d
**
*

*/

function numTilings(n: number): number {
    const mod: number = 7 + 10e8;
    const cache: Map<string, number> = new Map();

    const rec = (id: number, condition: string): number => {
        let res: number = 0;
        if (condition === 'a' && id === n) {
            return 1;
        }

        const key = `${id}_${condition}`;
        if (cache.has(key)) {
            return cache.get(key);
        }

        if (condition === 'a' && id < n) {
            // a + a
            res += rec(id + 1, 'a');
            res %= mod;
        }
        if (condition === 'a' && id < n - 1) {
            // a + b
            res += rec(id + 2, 'a');
            res %= mod;
            // a + c
            res += rec(id + 2, 'c');
            res %= mod;
            // a + d
            res += rec(id + 2, 'd');
            res %= mod;
        }

        if (condition === 'c' && id < n) {
            // c + d
            res += rec(id + 1, 'a');
            res %= mod;
            // c + b
            res += rec(id + 1, 'd');
            res %= mod;
        }
        if (condition === 'd' && id < n) {
            // d + c
            res += rec(id + 1, 'a');
            res %= mod;
            // d + b
            res += rec(id + 1, 'c');
            res %= mod;
        }

        cache.set(key, res);

        return res;
    }


    return rec(0, 'a');
};

const test = () => {
    const params = [
        {
            input: { n: 3 },
            output: 5,
        },
        {
            input: { n: 1 },
            output: 1,
        },
        {
            input: { n: 10 },
            output: 1255,
        },
        {
            input: { n: 100 },
            output: 190242381,
        },
    ];

    params.forEach(({input, output}) => {
        const { n } = input;

        const result = numTilings(n);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();
