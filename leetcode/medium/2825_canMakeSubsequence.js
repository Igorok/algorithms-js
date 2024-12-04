/**
 * @param {string} str1
 * @param {string} str2
 * @return {boolean}
 */
var canMakeSubsequence = function(str1, str2) {
    const getNextChar = (char) => (char === 'z') ? 'a' : String.fromCharCode(char.charCodeAt() + 1);

    let i = 0;
    for (const char of str2) {
        while (i < str1.length && str1[i] !== char && getNextChar(str1[i]) !== char) {
            i += 1;
        }
        if (i === str1.length) {
            return false;
        } else {
            i += 1;
        }
    }
    return true;
};


const test = () => {
    const params = [
        {
            input: ["abc", "ad"],
            output: true,
        },
        {
            input: ["zc", "ad"],
            output: true,
        },
        {
            input: ["ab", "d"],
            output: false,
        },
        {
            input: ["abcdcdcde", "adef"],
            output: true,
        },
    ];

    params.forEach(({input, output}) => {
        const result = canMakeSubsequence(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();