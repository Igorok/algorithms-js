function orderlyQueue(s: string, k: number): string {
    if (k > 1) {
        return s.split('').sort().join('');
    }

    const memo: Set<string> = new Set();
    let min: string = s;

    for (let i: number = 0; i < s.length; ++i) {
        const char: string = s[0];
        s = s.slice(1) + char;
        if (s < min) {
            min = s;
        }
    }

    return min;
};

/*

caaba-cabaa-cbaaa-caaab-aaabc

*/


const test = () => {
    const params = [
        {
            input: {
                s: "xmvzi", k: 2,
            },
            output: 'imvxz',
        },
        {
            input: {
                s: "gxzv", k: 4
            },
            output: 'gvxz',
        },
        {
            input: {
                s: "cba", k: 1
            },
            output: 'acb',
        },
        {
            input: {
                s: "baaca", k: 3
            },
            output: 'aaabc',
        },
        {
            input: {
                s: "caaba", k: 2
            },
            output: 'aaabc',
        },
        {
            input: {
                s: "caaba", k: 4
            },
            output: 'aaabc',
        },
    ];

    params.forEach(({input, output}) => {
        const { s, k } = input;
        const result = orderlyQueue(s, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

