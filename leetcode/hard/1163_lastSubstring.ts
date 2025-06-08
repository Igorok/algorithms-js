function lastSubstring(s: string): string {
    let res: string = '';

    for (let i = 0; i < s.length; ++i) {
        const sub: string = s.slice(i, s.length);
        if (sub > res) {
            res = sub;
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                s: "abab",
            },
            output: 'bab',
        },
        {
            input: {
                s: "leetcode",
            },
            output: 'tcode',
        },
    ];

    params.forEach(({input, output}) => {
        const { s } = input;

        const result = lastSubstring(s);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();
