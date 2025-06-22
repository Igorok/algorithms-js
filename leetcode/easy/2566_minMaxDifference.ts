function minMaxDifference(num: number): number {
    const str: string[] = String(num).split('');
    const min: string[] = [...str];
    const max: string[] = [...str];

    const minChar: string = min[0];
    let maxChar: string = '';


    for (let i: number = 0; i < str.length; ++i) {
        if (str[i] === minChar) {
            min[i] = '0';
        }
        if (maxChar === '' && str[i] < '9') {
            maxChar = str[i];
        }
        if (maxChar !== '' && str[i] === maxChar) {
            max[i] = '9';
        }
    }

    return Number(max.join('')) - Number(min.join(''));
};


/*

9876
9976 - 876

*/

const test = () => {
    const params = [
        {
            input: {
                num: 11891,
            },
            output: 99009,
        },
        {
            input: {
                num: 90,
            },
            output: 99,
        },
        {
            input: {
                num: 9876,
            },
            output: 9100,
        },
    ];

    params.forEach(({input, output}) => {
        const { num } = input;
        const result = minMaxDifference(num);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

