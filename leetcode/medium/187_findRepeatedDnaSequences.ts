function findRepeatedDnaSequences(s: string): string[] {
    const res: Set<string> = new Set();
    const memo: Set<string> = new Set();

    for (let i: number = 0; i + 9 < s.length; ++i) {
        const substr: string = s.slice(i, i + 10);

        if (memo.has(substr)) {
            res.add(substr);
        }
        memo.add(substr);
    }

    return [...res];
};

const test = () => {
    const params = [
        {
            input: {
                s: 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT',
            },
            output: ['AAAAACCCCC','CCCCCAAAAA'],
        },

        {
            input: {
                s: 'AAAAAAAAAAAAA',
            },
            output: ['AAAAAAAAAA'],
        },

        {
            input: {
                s: 'CAAAAAAAACAAAAAAAAC',
            },
            output: ['CAAAAAAAAC'],
        },
    ];

    params.forEach(({input, output}) => {
        const { s } = input;
        const result = findRepeatedDnaSequences(s);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();