function numEquivDominoPairs(dominoes: number[][]): number {
    const countOfDominoes: Map<string, number[]> = new Map();

    let res: number = 0;
    for (const [top, bottom] of dominoes) {
        const key: string = `${Math.min(top, bottom)}_${Math.max(top, bottom)}`;
        const count: number[] = countOfDominoes.get(key) || [0, 0];

        if (count[0] === 0) {
            count[0] = 1;
        } else {
            count[1] += count[0];
            res += count[0];

            count[0] += 1;

        }

        countOfDominoes.set(key, count);
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: { dominoes: [[1,2],[1,2],[1,1],[1,2],[2,2]] },
            output: 3,
        },
        {
            input: { dominoes: [[1,2],[2,1],[3,4],[5,6]] },
            output: 1,
        },

    ];

    params.forEach(({input, output}) => {
        const { dominoes } = input;

        const result = numEquivDominoPairs(dominoes);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();