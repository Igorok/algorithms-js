/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    let res = '';
    const charsMap = new Map();
    const windowMap = new Map();

    for (const char of t) {
        const count = (charsMap.get(char) || 0) + 1;
        charsMap.set(char, count);
    }

    const isOk = () => {
        for (const key of charsMap.keys()) {
            if (!windowMap.has(key) || charsMap.get(key) > windowMap.get(key)) {
                return false;
            }
        }
        return true;
    }

    let left = 0;
    for (let right = 0; right < s.length; ++right) {
        const rightChar = s[right];
        if (!charsMap.has(rightChar)) {
            continue;
        }
        const count = (windowMap.get(rightChar) || 0) + 1;
        windowMap.set(rightChar, count);

        if (count >= charsMap.get(rightChar) && isOk()) {
            if (!res.length) {
                res = s.slice(left, right + 1);
            }

            while (left <= right) {
                if ((right - left + 1) < res.length) {
                    res = s.slice(left, right + 1);
                }
                const leftChar = s[left];
                if (!charsMap.has(leftChar)) {
                    left += 1;
                    continue;
                }

                const leftCount = windowMap.get(leftChar) - 1;
                windowMap.set(leftChar, leftCount);
                left += 1;
                if (leftCount < charsMap.get(leftChar)) {
                    break;
                }
            }
        }
    }


    return res;
};

const test = () => {
    const params = [
        {
            input: ['ADOBECODEBANC', 'ABC'],
            output: 'BANC',
        },
        {
            input: ['a', 'a'],
            output: 'a',
        },
        {
            input: ['a', 'aa'],
            output: '',
        },
        {
            input: ['ab', 'b'],
            output: 'b',
        },
    ];

    params.forEach(({input, output}) => {
        const result = minWindow(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();