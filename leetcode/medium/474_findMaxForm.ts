function findMaxForm(strs: string[], m: number, n: number): number {
    const countOfChars: number[][] = new Array(strs.length).fill(0).map(() => [0, 0]);

    for (let i: number = 0; i < strs.length; ++i) {
        const str: string = strs[i];
        for (const char of str) {
            countOfChars[i][parseInt(char)] += 1;
        }
    }

    const cache: Map<string, number> = new Map();
    const rec = (id: number, c0: number, c1: number): number => {
        const key: string = `${id}_${c0}_${c1}`;

        if (id >= strs.length) {
            return 0;
        }
        if (cache.has(key)) {
            return cache.get(key);
        }

        let r1: number = 0;
        if (c0 + countOfChars[id][0] <= m && c1 + countOfChars[id][1] <= n) {
            r1 = 1 + rec(id + 1, c0 + countOfChars[id][0], c1 + countOfChars[id][1]);
        }

        const r2: number = rec(id + 1, c0, c1);

        const res: number = Math.max(r1, r2);

        cache.set(key, res);

        return res;
    };


    return rec(0, 0, 0);
};

const test = () => {
    const params = [
        {
            input: { strs: ["10","0001","111001","1","0"], m: 5, n: 3 },
            output: 4,
        },
        {
            input: { strs: ["10","0","1"], m: 1, n: 1 },
            output: 2,
        },
    ];

    params.forEach(({input, output}) => {
        const { strs, m, n } = input;
        const result = findMaxForm(strs, m, n);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();