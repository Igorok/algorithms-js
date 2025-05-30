function replaceDigits(s: string): string {
    const arr: string[] = s.split('');

    for (let i: number = 1; i < arr.length; i += 2) {
        const code: number = arr[i-1].charCodeAt(0);
        arr[i] = String.fromCharCode(code + parseInt(arr[i]));
    }

    return arr.join('');
};

const test = () => {
    const params = [
        {
            input: { s: "a1c1e1" },
            output: 'abcdef',
        },
        {
            input: { s: "a1b2c3d4e" },
            output: 'abbdcfdhe',
        },
    ];

    params.forEach(({input, output}) => {
        const { s } = input;

        const result = replaceDigits(s);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();