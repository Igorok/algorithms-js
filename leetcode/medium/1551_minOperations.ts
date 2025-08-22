function minOperations(n: number): number {
    const arr: number[] = new Array(n).fill(0);
    for (let i: number = 0; i < n; ++i) {
        arr[i] = (2 * i) + 1;
    }

    let res: number = 0;
    for (let i: number = 0; i < Math.floor(n/2); ++i) {
        res += (arr[n-1-i] - arr[i]) / 2;
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                n: 3,
            },
            output: 2,
        },
        {
            input: {
                n: 4,
            },
            output: 4,
        },
        {
            input: {
                n: 6,
            },
            output: 9,
        },
    ];

    params.forEach(({input, output}) => {
        const { n } = input;
        const result = minOperations(n);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();