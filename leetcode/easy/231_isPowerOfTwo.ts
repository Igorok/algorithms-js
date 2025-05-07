function isPowerOfTwo_0(n: number): boolean {
    if (n <= 0) return false;

    while (n > 0) {
        if (n === 1) {
            return true;
        }
        if ((n % 2) === 1) {
            return false;
        }
        n = Math.floor(n / 2);
    }

    return true;
};

function isPowerOfTwo(n: number): boolean {
    if (n <= 0) return false;
    const lastBit: number = n & (-n);
    return lastBit === n;
};

const test = () => {
    const params = [
        {
            input: { n: -16 },
            output: false,
        },
        {
            input: { n: 1 },
            output: true,
        },
        {
            input: { n: 16 },
            output: true,
        },
        {
            input: { n: 3 },
            output: false,
        },
    ];

    params.forEach(({input, output}) => {
        const { n } = input;

        const result = isPowerOfTwo(n);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();