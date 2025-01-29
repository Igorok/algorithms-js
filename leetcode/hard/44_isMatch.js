/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    const cache = new Map();

    const _isMatch = (y, x) => {
        if (cache.has([s.length, p.length].join('_')))
            return cache.get([s.length, p.length].join('_'));

        const key = [y, x].join('_');

        if (cache.has(key))
            return cache.get(key);

        if (x == p.length && y == s.length) {
            cache.set(key, true);
            return true;
        }

        if (x == p.length && y < s.length) {
            cache.set(key, false);
            return false;
        }

        if (x < p.length && y == s.length) {
            for (i = x; i < p.length; ++i) {
                if (p[i] != '*') {
                    cache.set([y, i].join('_'), false);
                    cache.set(key, false);
                    return false;
                }
            }
            cache.set([p.length, s.length].join('_'), true);
            cache.set(key, true);
            return true;
        }

        if (s[y] == p[x] || p[x] == '?') {
            const r = _isMatch(y + 1, x + 1);
            cache.set(key, r)
            return r;
        }

        if (p[x] == '*') {
            let i = y
            while (i <= s.length) {
                const r = _isMatch(i, x + 1);
                if (r == true) {
                    cache.set(key, true);
                    return true;
                }
                i += 1
            }
            cache.set(key, false);
            return false;
        }

        cache.set(key, false);
        return false
    };

    return _isMatch(0, 0);
};


const test = () => {
    const params = [
        {
            'input': [
                "aababbbbaaabaabaabbbbbaabbaabaaaabaaabbbaaaaabbbaaaabaaababbbbbbabbbabaababbbaaaaaaabaaaabbbaabbbaaabaaaababbababbaabaaaaabaaababbaababbabbbbabaabababbabbabbababbbbaaaabbbaabbaabbaabababbbbaaaabbabaaabbab",
                "*bbb*b*****a*abaab****a****b***a*ab*bb***b**bb*b*aab*aaa*a*b*bbbb*a*a*****ba**bb*b*****b*a*bb*******aa"
            ],
            'output': false,
        },
        {
            'input': [
                "bbbbaababbbbaabaaabbbbbbabbabbaaabaabbbaaaaaababababbbbbaabbaababbbbbabbababbaabaaabbbababaabbabbbaabbbabbbaabbabbbabbbbabbaabbbbbbaabababbaaaababbbaaabbbbaaabbbbabaabaaababbabbbabaaabbbbbbbbaabaabbabb",
                "b*ab*b****b*a**b**b****abbba**a*baa****b*ab****bbabaaaab***ab****aba***a******aa*ba*bba****aa******b*b**",
            ],
            'output': false,
        },

        {
            'input': ["adceb", "*a*b"],
            'output': true,
        },
        {
            'input': ["aa", "a"],
            'output': false,
        },
        {
            'input': ["aa", "*"],
            'output': true,
        },
        {
            'input': ["cb", "?a"],
            'output': false,
        },
        {
            'input': ["aa", "a?"],
            'output': true,
        },
        {
            'input': ["cb", "??"],
            'output': true,
        },
        {
            'input': ["caaaaaab", "c*b"],
            'output': true,
        },
        {
            'input': ["cb", "c*b"],
            'output': true,
        },
        {
            'input': ["cbbbbbbb", "c*b"],
            'output': true,
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