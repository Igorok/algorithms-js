/**
 * @param {string} s
 * @param {number[]} spaces
 * @return {string}
 */
var addSpaces = function(s, spaces) {
    let res = '';
    let spaceId = 0;

    for (let i = 0; i < s.length; ++i) {
        if (spaceId < spaces.length && i === spaces[spaceId]) {
            res += ' ';
            spaceId += 1;
        }
        res += s[i];
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: ["LeetcodeHelpsMeLearn", [8,13,15]],
            output: 'Leetcode Helps Me Learn',
        },

        {
            input: ["icodeinpython", [1,5,7,9]],
            output: 'i code in py thon',
        },
        {
            input: ["spacing", [0,1,2,3,4,5,6]],
            output: ' s p a c i n g',
        },
    ];

    params.forEach(({input, output}) => {
        const result = addSpaces(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();