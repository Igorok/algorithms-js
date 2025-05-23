function repeatedSubstringPattern(s: string): boolean {
    if (s.length === 1) return true;

    for (let i = 1; i <= Math.ceil(s.length / 2); ++i) {
        if ((s.length % i) !== 0) {
            continue;
        }
        const sub: string = s.slice(0, i);
        const repeat: number = s.length / i;
        const res: string = sub.repeat(repeat);
        if (res === s) {
            return true;
        }
    }

    return false;
};

const test = () => {
    const params = [
        {
            input: 'abab',
            output: true,
        },
        {
            input: 'aba',
            output: false,
        },
        {
            input: 'abcabcabcabc',
            output: true,
        },
    ];

    params.forEach(({input, output}) => {
        const result = repeatedSubstringPattern(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();