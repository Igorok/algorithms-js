/**
 * @param {string} s
 * @return {number}
 */
var countPalindromicSubsequence_0 = function(s) {
    const subsequence = new Set();

    for (let i1 = 0; i1 < s.length - 2; ++i1) {
        for (let i2 = i1 + 1; i2 < s.length - 1; ++i2) {
            const subs = [s[i1], s[i2], s[i1]].join('_');

            if (subsequence.has(subs)) {
                continue;
            }

            for (let i3 = i2+1; i3 < s.length; ++i3) {
                if (s[i3] === s[i1]) {
                    subsequence.add(subs);
                    break;
                }
            }
        }
    }

    return subsequence.size;
};


/*

aaaaaabaaaacaaaadaaae

{
    a: {
        a: false,
        b: false,
        c: false,
        d: false,
        e: false,
    }
}

*/
var countPalindromicSubsequence_1 = function(s) {
    const subsequence = new Set();

    const charsIds = new Array(26).fill(-1);
    const charsCount = new Array(26).fill(0);

    for (let i = 0; i < s.length; ++i) {
        const code = s[i].charCodeAt() - 'a'.charCodeAt();
        if (charsIds[code] !== -1) {
            const oldId = charsIds[code];

            for (let j = 0; j < charsIds.length; ++j) {
                if (charsIds[j] > oldId) {
                    const key = [code, j, code].join();
                    subsequence.add(key)
                }
            }
        }
        charsIds[code] = i;
        charsCount[code] += 1;
        if (charsCount[code] === 3) {
            const key = [code, code, code].join();
            subsequence.add(key)
        }
    }

    return subsequence.size;
};

var countPalindromicSubsequence_2 = function(s) {
    const subsequence = new Set();

    const charsIds = {};
    const charsCount = {};

    for (let i = 0; i < s.length; ++i) {
        const code = s[i];
        if (charsIds[code] !== undefined) {
            const oldId = charsIds[code];

            for (const k in charsIds) {
                if (charsIds[k] > oldId) {
                    const key = [code, k, code].join();
                    subsequence.add(key);
                }
            }
        } else {
            charsCount[code] = 0;
        }
        charsIds[code] = i;

        charsCount[code] += 1;
        if (charsCount[code] === 3) {
            const key = [code, code, code].join();
            subsequence.add(key)
        }
    }

    return subsequence.size;
};


var countPalindromicSubsequence = function(s) {
    let res = 0;

    const left = new Array(26).fill(-1);
    const right = new Array(26).fill(-1);

    for (let i = 0; i < s.length; ++i) {
        const code = s[i].charCodeAt() - 'a'.charCodeAt();
        if (left[code] === -1) {
            left[code] = i;
        }
        right[code] = i;
    }


    for (let i = 0; i < 26; ++i) {
        if (right[i] === -1) continue;

        const subs = new Set();
        for (let j = left[i]+1; j < right[i]; ++j) {
            subs.add(s[j]);
        }
        res += subs.size;
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: 'aabca',
            output: 3,
        },

        {
            input: 'adc',
            output: 0,
        },
        {
            input: 'bbcbaba',
            output: 4,
        },
        {
            input: 'tlpjzdmtwderpkpmgoyrcxttiheassztncqvnfjeyxxp',
            output: 161,
        },
        {
            input: 'babab',
            output: 3,
        },
    ];

    params.forEach(({input, output}) => {
        const result = countPalindromicSubsequence(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();