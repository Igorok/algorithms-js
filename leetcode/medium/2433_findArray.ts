function findArray(pref: number[]): number[] {
    const res: number[] = new Array(pref.length).fill(0);
    res[0] = pref[0];

    for (let i: number = 1; i < pref.length; ++i) {
        res[i] = pref[i-1] ^ pref[i];
    }
    return res;
};

const test = () => {
    const params = [
        {
            input: {
                pref: [5,2,0,3,1]
            },
            output: [5,7,2,3,2],
        },
        {
            input: {
                pref: [13]
            },
            output: [13],
        },
    ];

    params.forEach(({input, output}) => {
        const { pref } = input;

        const result = findArray(pref);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();