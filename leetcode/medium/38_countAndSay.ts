const getRLE = (str: string): string => {
    let chars: string[] = [];

    let start: number = 0;
    let current: string = str[0];

    for (let i: number = 1; i < str.length; ++i) {
        if (str[i] !== current) {
            chars.push(String(i - start));
            chars.push(current);
            current = str[i];
            start = i;
        }
    }

    chars.push(String(str.length - start));
    chars.push(current);

    return chars.join('');
};

function countAndSay(n: number): string {
    let str: string = '1';
    for (let i: number = 1; i < n; ++i) {
        str = getRLE(str);
    }

    return str;
};

const test = () => {
    const params = [
        {
            input: 4,
            output: '1211',
        },
        {
            input: 1,
            output: '1',
        },
    ];

    params.forEach(({input, output}) => {
        const result = countAndSay(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();