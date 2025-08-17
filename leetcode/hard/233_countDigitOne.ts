function countDigitOne(n: number): number {
    const str: string = String(n);
    const memo: Map<string, number> = new Map();

    const dfs = (id: number, limited: boolean, acc: number) => {
        if (id === str.length) {
            return acc;
        }

        const key = `${id}_${limited}_${acc}`;
        if (memo.has(key)) {
            return memo.get(key);
        }

        const max: number = limited ? Number(str[id]) : 9;

        let res: number = 0;

        for (let i: number = 0; i <= max; ++i) {
            const l: boolean = (i == max) && limited;
            const a: number = i === 1 ? acc + 1 : acc;
            res += dfs(id + 1, l, a);
        }

        memo.set(key, res);

        return res;
    };


    return dfs(0, true, 0);
};

/*
9252736
13016474


*/
const test = () => {
    const params = [
        {
            input: {
                n: 13
            },
            output: 6,
        },
        {
            input: {
                n: 0,
            },
            output: 0,
        },
        {
            input: {
                n: 111,
            },
            output: 36,
        },
        {
            input: {
                n: 500,
            },
            output: 200,
        },
        {
            input: {
                n: 13123213,
            },
            output: 13016474,
        },
    ];

    params.forEach(({input, output}) => {
        const { n } = input;
        const result = countDigitOne(n);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

