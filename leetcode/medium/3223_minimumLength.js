/**
 * @param {string} s
 * @return {number}
 */
var minimumLength = function(s) {
    const charsCount = new Array(26).fill(0);

    const aCode = 'a'.charCodeAt();
    for (const char of s) {
        const code = char.charCodeAt() - aCode;
        charsCount[code] += 1;
    }

    let res = 0;
    for (const num of charsCount) {
        if (num < 3) {
            res += num;
        } else if (num % 2) {
            res += 1;
        } else {
            res += 2
        }
    }

    return res;
};

/*
1111
*/

const test = () => {
    const params = [
        {
            input: 'abaacbcbb',
            output: 5,
        },
        {
            input: 'aa',
            output: 2,
        },
    ];

    params.forEach(({input, output}) => {
        const result = minimumLength(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();