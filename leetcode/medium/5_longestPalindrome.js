/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    let res = s[0];

    const checkSubstr = (left, right) => {
        while (left > -1 && right + 1 < s.length && s[left-1] === s[right+1]) {
            left -= 1;
            right += 1;
        }
        const substr = s.slice(left, right + 1);
        if (substr.length > res.length) {
            res = substr;
        }
    }

    for (let i = 1; i < s.length; ++i) {
        if (i + 1 < s.length && s[i-1] === s[i+1]) {
            checkSubstr(i - 1, i + 1);
        }
        if (s[i-1] === s[i]) {
            checkSubstr(i - 1, i);
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: 'babad',
            output: 'bab',
        },
        {
            input: 'cbbd',
            output: 'bb',
        },
        {
            input: 'bb',
            output: 'bb',
        },
        {
            input: 'bbb',
            output: 'bbb',
        },
        {
            input: 'aaaa',
            output: 'aaaa',
        },
    ];

    params.forEach(({input, output}) => {
        const result = longestPalindrome(input);

        console.log(
            result === output ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();