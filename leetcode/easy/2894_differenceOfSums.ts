function differenceOfSums_0(n: number, m: number): number {
    let num1: number = 0;
    let num2: number = 0;

    for (let i: number = 1; i <= n; ++i) {
        if (i % m === 0) {
            num2 += i;
        } else {
            num1 += i;
        }
    }

    return num1 - num2;
};

function differenceOfSums(n: number, m: number): number {
    let res: number = 0;

    for (let i: number = 1; i <= n; ++i) {
        if (i % m === 0) {
            res -= i;
        } else {
            res += i;
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {n: 10, m: 3},
            output: 19,
        },
        {
            input: {n: 5, m: 6},
            output: 15,
        },
        {
            input: {n: 5, m: 1},
            output: -15,
        },
    ];

    params.forEach(({input, output}) => {
        const { n, m } = input;
        const result = differenceOfSums(n, m);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();