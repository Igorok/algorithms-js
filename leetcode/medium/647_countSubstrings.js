/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
    let res = s.length;

    const checkSubstr = (left, right) => {
        let i = 1;
        while (left > -1 && right + 1 < s.length && s[left-1] === s[right+1]) {
            left -= 1;
            right += 1;
            i += 1;
        }
        res += i;
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

/*

a a a a a
a a
a a a
  a a
  a a a
a a a a a
    a a
    a a a
      a a

*/

const test = () => {
    const params = [
        {
            input: 'abc',
            output: 3,
        },
        {
            input: 'aaa',
            output: 6,
        },
        {
            input: 'aaaaa',
            output: 15,
        },
    ];

    params.forEach(({input, output}) => {
        const result = countSubstrings(input);

        console.log(
            result === output ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();