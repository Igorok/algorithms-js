function maxDifference(s: string): number {
    const count: Map<string, number> = new Map();

    for (const char of s) {
        const cnt: number= (count.get(char) || 0) + 1;
        count.set(char, cnt);
    }

    let odd: number = Number.MIN_SAFE_INTEGER;
    let even: number = Number.MAX_SAFE_INTEGER;
    count.forEach((val: number) => {
        if (val % 2) {
            odd = Math.max(odd, val);
        } else {
            even = Math.min(even, val);
        }
    });

    return odd - even;
};


const test = () => {
    const params = [
        {
            input: { s: "aaaaabbc" },
            output: 3,
        },
        {
            input: { s: "abcabcab" },
            output: 1,
        },
        {
            input: { s: "tzt" },
            output: -1,
        },
    ];

    params.forEach(({input, output}) => {
        const { s } = input;
        const result = maxDifference(s);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

