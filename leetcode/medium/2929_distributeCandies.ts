function distributeCandies(n: number, limit: number): number {
    let res: number = 0;

    for (let i: number = 0; i <= Math.min(limit, n); ++i) {
        const rem: number = n - i;
        if (rem > limit * 2) {
            continue;
        }

        const maxCount: number = Math.min(limit, rem);
        const minCount: number = Math.max(0, rem - limit);

        const r: number = maxCount - minCount + 1;
        res += r;
    }

    return res;
};

/*

n: 5, limit: 2

1, min(5-1, 2), max(0, 5-1-2)
2, min(5-2, 2), max(0, 5-2-2)



*/


const test = () => {
    const params = [
        {
            input: { n: 9, limit: 3 },
            output: 1,
        },
        {
            input: { n: 5, limit: 2 },
            output: 3,
        },
        {
            input: { n: 3, limit: 3 },
            output: 10,
        },
    ];

    params.forEach(({input, output}) => {
        const { n, limit } = input;

        const result = distributeCandies(n, limit);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();