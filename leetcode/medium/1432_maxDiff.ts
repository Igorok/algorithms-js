function maxDiff(num: number): number {
    const str: string[] = String(num).split('');
    const min: string[] = [...str];
    const max: string[] = [...str];

    let minChar: string = '';
    let minRepl: string = '';
    let maxChar: string = '';

    for (let i: number = 0; i < str.length; ++i) {
        if (minChar === '') {
            if (i === 0 && str[i] > '1') {
                minChar = str[i];
                minRepl = '1';
            }
            if (i > 0 && str[i] > '0' && str[i] !== str[0]) {
                minChar = str[i];
                minRepl = '0';
            }
        }

        if (minChar === str[i]) {
            min[i] = minRepl;
        }

        if (maxChar === '' && str[i] < '9') {
            maxChar = str[i];
        }

        if (str[i] === maxChar) {
            max[i] = '9';
        }
    }

    const minNum: number = Number(min.join(''));
    const maxNum: number = Number(max.join(''));

    return maxNum - minNum;
};

const test = () => {
    const params = [
        {
            input: {
                num: 555
            },
            output: 888,
        },
        {
            input: {
                num: 9
            },
            output: 8,
        },
    ];

    params.forEach(({input, output}) => {
        const { num } = input;
        const result = maxDiff(num);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

