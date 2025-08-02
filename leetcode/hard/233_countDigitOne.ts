function countDigitOne(n: number): number {
    return 0;
};

/*

0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,1,0,0,0,0,0,0,0,0,


0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,1,0,0,0,0,0,0,0,0,
0,1,1,1,1,1,1,1,1,1,

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
                n: 13123213,
            },
            output: 13016474,
        },
    ];

    params.forEach(({input, output}) => {
        const { n } = input;
        const result = numDistinct(s, t);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

