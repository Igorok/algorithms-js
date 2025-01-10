/**
 * @param {string} s
 * @param {number[][]} shifts
 * @return {string}
 */
var shiftingLetters_0 = function(s, shifts) {
    const chars = [];
    for (let i = 0; i < s.length; ++i) {
        const code = s[i].charCodeAt();
        chars.push(code);
    }
    const aCode = 'a'.charCodeAt();
    const zCode = 'z'.charCodeAt();

    for (const [start, end, increace] of shifts) {
        const val = increace ? 1 : -1;
        for (let i = start; i <= end; ++i) {
            chars[i] += val;
            if (chars[i] < aCode) {
                chars[i] = zCode;
            }
            if (chars[i] > zCode) {
                chars[i] = aCode;
            }
        }
    }

    return chars.map((code) => String.fromCharCode(code)).join('');
};

var shiftingLetters = function(s, shifts) {
    const diffArray = new Array(s.length + 1).fill(0);

    for (const [start, end, increace] of shifts) {
        const right = increace ? 1 : -1;
        const left = increace ? -1 : 1;
        diffArray[start] += left;
        diffArray[end + 1] += right;
    }

    const aCode = 'a'.charCodeAt();
    const chars = new Array(s.length).fill(0);
    let diff = 0;
    for (let i = s.length - 1; i > -1; --i) {
        diff += diffArray[i + 1];
        const code = s[i].charCodeAt() - aCode;
        const char = aCode + (26 + code + (diff % 26)) % 26;
        chars[i] = String.fromCharCode(char);
    }
    return chars.join('');
};


const test = () => {
    const params = [
        {
            input: ['abc', [[0,1,0],[1,2,1],[0,2,1]]],
            output: 'ace',
        },
        {
            input: ['dztz', [[0,0,0],[1,1,1]]],
            output: 'catz',
        },
        {
            input: ['zzz', [[0,2,1],[0,2,1]]],
            output: 'bbb',
        },
        {
            input: ['aaa', [[0,2,0]]],
            output: 'zzz',
        },
    ];

    params.forEach(({input, output}) => {
        const result = shiftingLetters(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();