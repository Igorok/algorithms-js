function minSteps(s: string, t: string): number {
    const aCode: number = 'a'.charCodeAt(0);

    const countS: number[] = new Array(26).fill(0);
    const countT: number[] = new Array(26).fill(0);

    for (let i: number = 0; i < s.length; ++i) {
        const code: number = s.charCodeAt(i) - aCode;
        countS[code] += 1;
    }
    for (let i: number = 0; i < t.length; ++i) {
        const code: number = t.charCodeAt(i) - aCode;
        countT[code] += 1;
    }

    let res: number = 0;

    for (let i: number = 0; i < 26; ++i) {
        res += Math.abs(countS[i] - countT[i]);
    }

    return res;
};

/*

leetcode
coats

*/

const test = () => {
    const params = [
        {
            input: {
                s: "leetcode", t: "coats",
            },
            output: 7,
        },
        {
            input: {
                s: "night", t: "thing",
            },
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const { s, t } = input;
        const result = minSteps(s, t);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();