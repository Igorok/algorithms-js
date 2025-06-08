function lexicalOrder(n: number): number[] {
    const res: number[] = [];

    const rec = (num: number): void => {
        if (num > n) {
            return;
        }
        const start: number = num < 10 ? 1 : 0;
        for (let i: number = start; i < 10; i++) {
            const val: number = num + i;
            if (val > n) {
                break;
            }

            res.push(val);
            rec(val * 10);
        }
    };

    rec(0);

    return res;
};

/*

[1, ]
1   10, 100, 1000




*/

const test = () => {
    const params = [
        {
            input: { n: 13 },
            output: [1,10,11,12,13,2,3,4,5,6,7,8,9],
        },
        {
            input: { n: 2 },
            output: [1,2],
        },
    ];

    params.forEach(({input, output}) => {
        const { n } = input;
        const result = lexicalOrder(n);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();