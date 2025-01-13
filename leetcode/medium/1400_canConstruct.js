/**
 * @param {string} s
 * @param {number} k
 * @return {boolean}
 */
var canConstruct = function(s, k) {
    if (s.length < k) {
        return false;
    }

    const countOfChars = new Array(26).fill(0);
    const aCode = 'a'.charCodeAt();
    for (const char of s) {
        const code = char.charCodeAt() - aCode;
        countOfChars[code] += 1;
    }

    let odd = 0;
    for (const count of countOfChars) {
        if (count % 2) {
            odd += 1;
        }
    }

    return k >= odd;
};

/*

annabelle
nleabaeln


*/

const test = () => {
    const params = [
        {
            input: ['annabelle', 2],
            output: true,
        },
        {
            input: ['leetcode', 3],
            output: false,
        },
        {
            input: ['true', 4],
            output: true,
        },
        {
            input: ['eeek', 3],
            output: true,
        },
    ];

    params.forEach(({input, output}) => {
        const result = canConstruct(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();