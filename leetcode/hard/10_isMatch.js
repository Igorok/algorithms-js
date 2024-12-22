/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    let res = false;
    const cache = {};
    const rec = (i, j) => {
        if (res) return res;
        if (cache[i+'_'+j] !== undefined) {
            return cache[i+'_'+j];
        }

        if (i < s.length && j < p.length) {
            if (s[i] === p[j] || p[j] === '.') {
                if (j+1 < p.length && p[j+1] === '*') {
                    cache[i+'_'+j] = (rec(i+1, j) || rec(i+1, j+2) || rec(i, j+2));
                    return cache[i+'_'+j];
                }

                cache[i+'_'+j] = rec(i+1, j+1);
                return cache[i+'_'+j];
            }
            if (j + 1 < p.length && p[j+1] === '*') {
                cache[i+'_'+j] = rec(i, j+2);
                return cache[i+'_'+j];
            }
        }

        if (i === s.length) {
            if (j === p.length) {
                res = true;
                cache[i+'_'+j] = true;
                return cache[i+'_'+j];
            }
            if (p[j] === '*') {
                cache[i+'_'+j] = rec(i, j+1);
                return cache[i+'_'+j];
            }
            if(j + 1 < p.length && p[j+1] === '*') {
                cache[i+'_'+j] = rec(i, j+2);
                return cache[i+'_'+j];
            }
        }

        cache[i+'_'+j] = false;
        return cache[i+'_'+j];
    };

    rec(0, 0);

    return res;
};

const test = () => {
    const params = [
        {
            input: ["aa", "a"],
            output: false,
        },
        {
            input: ["aa", "a*"],
            output: true,
        },
        {
            input: ["ab", ".*"],
            output: true,
        },
        {
            input: ["abcdefg", ".*"],
            output: true,
        },
        {
            input: ["aab", "c*a*b"],
            output: true,
        },
        {
            input: ["aaaaa", ".*.*.*.*.*"],
            output: true,
        },
        {
            input: ["aaa", "a*a"],
            output: true,
        },
        {
            input: ["aaaaa", "b*c*a"],
            output: false,
        },
        {
            input: ["a", "ab*"],
            output: true,
        },
        {
            input: ["aaa", "ab*a*c*a"],
            output: true,
        },
        {
            input: ["bbbba", ".*a*a"],
            output: true,
        },
        {
            input: ["aaaaaaaaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*"],
            output: false,
        },
    ];

    params.forEach(({input, output}) => {
        const result = isMatch(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();