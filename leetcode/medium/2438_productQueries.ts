function productQueries_0(n: number, queries: number[][]): number[] {
    const mod: number = 7 + 10**9;

    const powers: number[] = [];
    let i: number = 0;
    while (n > 0) {
        if (n & 1) {
            powers.push(2 ** i);
        }
        n = n >> 1;
        i += 1;
    }

    const res: number[] = [];

    for (const [s, e] of queries) {
        let r: number = 1;
        for (let i: number = s; i <= e; ++i) {
            r = (r * powers[i]) % mod;
        }
        res.push(r);
    }

    return res;
};

function productQueries(n: number, queries: number[][]): number[] {
    const mod: number = 7 + 10**9;

    const powers: number[] = [];
    let i: number = 0;
    while (n > 0) {
        if (n & 1) {
            powers.push(2 ** i);
        }
        n = n >> 1;
        i += 1;
    }

    const answers: number[][] = new Array(powers.length).fill(0).map(() => new Array(powers.length).fill(0));
    for (let i: number = 0; i < powers.length; ++i) {
        answers[i][i] = powers[i];

        for (let j: number = i+1; j < powers.length; ++j) {
            const m: number = (answers[i][j-1] * powers[j]) % mod;
            answers[i][j] = m;
        }
    }

    const res: number[] = [];

    for (const [s, e] of queries) {
        res.push(answers[s][e]);
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                n: 15, queries: [[0,1],[2,2],[0,3]]
            },
            output: [2,4,64],
        },
        {
            input: {
                n: 2, queries: [[0,0]]
            },
            output: [2],
        },
    ];

    params.forEach(({input, output}) => {
        const { n, queries } = input;
        const result = productQueries(n, queries);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();