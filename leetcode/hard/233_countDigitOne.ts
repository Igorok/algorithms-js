function countDigitOne(n: number): number {
    return 0;
};

/*

   - [10, 13] - 10, 11, 12, 13 = 5
13 - [0, 9] - 0,1,2,3,4,5,6,7,8,9 = 1

    - [100, 111]
111 - [0-99] - [10-19] -[0-9]
             - [20-29] -[0-9]
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

