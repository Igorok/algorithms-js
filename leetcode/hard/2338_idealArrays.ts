function idealArrays_0(n: number, maxValue: number): number {
    const mod: number = 7 + 10e8;

    const cache: Map<string, number> = new Map();
    const rec = (iteration: number, prev: number): number => {
        if (iteration === n) return 1;
        if (prev > maxValue) return 0;

        const key: string = `${iteration}_${prev}`;
        if (cache.has(key)) {
            return cache.get(key);
        }

        let acc: number = 0;
        for (let i: number = prev; i <= maxValue; i+=prev) {
            acc += rec(iteration + 1, i);
            acc %= mod;
        }

        cache.set(key, acc);

        return acc;
    }

    return rec(0, 1);
};

function idealArrays(n: number, maxValue: number): number {
    const mod: number = 7 + 10e8;
    const count: number[][] = new Array(15).fill(0).map(() => new Array(10005).fill(0));
    const prefixSum: number[][] = new Array(15).fill(0).map(() => new Array(10005).fill(0));
    const options: number[] = new Array(15).fill(0);

    const countUniqueSequences = (curr: number, id: number, memo: number[]) => {
        options[id] += 1;
        for (let i: number = 2; curr * i <= maxValue; ++i) {
            countUniqueSequences(curr * i, id + 1, [...memo, curr*i]);
        }
    };

    for (let i: number = 1; i < count[0].length; ++i) {
        count[1][i] = 1;
        prefixSum[1][i] = i;
    }

    for (let i: number = 2; i <= 14; ++i) {
        for (let j = i; j <= 10000; ++j) {
            count[i][j] = prefixSum[i-1][j-1];
            prefixSum[i][j] = (count[i][j] + prefixSum[i][j-1]) % mod;
        }
    }

    for (let i = 1; i <= maxValue; ++i) {
        countUniqueSequences(i, 1, [i]);
    }

    let res: bigint = 0n;

    for (let i: number = 1; i <= 14; ++i) {
        const comb: bigint = BigInt(count[i][n]);
        const opts: bigint = BigInt(options[i]);
        const ways = (comb * opts) % BigInt(mod);
        res += ways;
        res %= BigInt(mod)
    }

    return Number(res);
};

/*

n: 5, maxValue: 3,

1, 1, 1, 1, 1
1, 1, 1, 1, 2
1, 1, 1, 2, 2
1, 1, 2, 2, 2
1, 2, 2, 2, 2
2, 2, 2, 2, 2
1, 1, 1, 1, 3
1, 1, 1, 3, 3
1, 1, 3, 3, 3
1, 3, 3, 3, 3
3, 3, 3, 3, 3

---

1 1 1

1 1 2
1 2 2

1 2 4

1 1 2 4
1 2 2 4
1 2 4 4

i = uniq numbers
j = length

  0 1 2 3 4
0 0 0 0 0 0
1 0 1 1 1 1
2 0 0 1 2 3
3 0 0 0 1 3
4 0 0 0 0 1


Why does a prefix sum work?
1 1 1 1
uniq 1
length 4, count always 1
uniq2
length 4, so we can replace 3 items by a second number
uniq3
length 4, so we can replace 3 previous numbers by a third element


---

2 <= n <= 10**4
1 <= maxValue <= 10**4

10**4 = 10000;
2**13 = 8192;
2**14 = 16384;





 */

const test = () => {
    const params = [
        {
            input: {
                n: 2, maxValue: 5,
            },
            output: 10,
        },
        {
            input: {
                n: 5, maxValue: 3,
            },
            output: 11,
        },
        {
            input: {
                n: 5878, maxValue: 2900,
            },
            output: 11,
        },
    ];

    params.forEach(({input, output}) => {
        const { n, maxValue } = input;

        const result = idealArrays(n, maxValue);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();
