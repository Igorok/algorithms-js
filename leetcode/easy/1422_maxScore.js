/**
 * @param {string} s
 * @return {number}
 */
var maxScore = function(s) {
    let sum = 0;
    for (let i = 0; i < s.length; ++i) {
        sum += Number(s[i]);
    }

    let res = 0;
    let left = 0;
    for (let i = 0; i < s.length-1; ++i) {
        left += Number(s[i]);
        const zeros = Math.max(i+1 - left, 0);
        const ones = sum - left;
        res = Math.max(res, zeros + ones)
    }

    return res;
};


const test = () => {
    const params = [
        {
            input: '011101',
            output: 5,
        },
        {
            input: '00111',
            output: 5,
        },
        {
            input: '1111',
            output: 3,
        },
        {
            input: '00',
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const result = maxScore(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();