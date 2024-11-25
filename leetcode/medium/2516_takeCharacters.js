/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var takeCharacters_1 = function(s, k) {
    const letterCount = new Map();
    for (const char of s) {
        const count = (letterCount.get(char) || 0) + 1;
        letterCount.set(char, count);
    }

    for (const char of ['a', 'b', 'c']) {
        const count = letterCount.get(char) || 0;
        if (count < k) return -1;
    }

    let left = right = Math.floor(s.length / 2);

    let res = -1;
    return res;
};

var takeCharacters_2 = function(s, k) {
    const letterCount = new Array(3).fill(0);
    const letterIds = { a: 0, b: 1, c: 2 };
    let start = 0;
    let end = s.length - 1;

    while (start < end) {
        letterCount[letterIds[s[start]]] += 1;
        letterCount[letterIds[s[end]]] += 1;

        if (letterCount.every((count) => (count >= k))) break;

        start += 1;
        end -= 1;
    }

    if (start === end) {
        end += 1;
        letterCount[letterIds[s[start]]] += 1;
    }

    if (!letterCount.every((count) => (count >= k))) return -1;
    if (start + 1 === end && s.length === 3 * k) {
        return 3*k;
    }

    let reduce = true;
    while (reduce) {
        const pStart = start;
        const pEnd = end;


        if (letterCount[letterIds[s[start]]] - 1 >= k) {
            letterCount[letterIds[s[start]]] -= 1;
            start -= 1;
        }
        if (letterCount[letterIds[s[end]]] - 1 >= k) {
            letterCount[letterIds[s[end]]] -= 1;
            end += 1;
        }

        if (pStart === start && pEnd === end) {
            reduce = false;
        }
    }

    if (start + 1 === end && s.length > 3 * k) {
        let _start = 0;
        let _end = s.length - 1;

        const leftCount = [...letterCount];
        const rightCount = [...letterCount];

        while (leftCount[letterIds[s[_start + 1]]] - 1 >= k) {
            _start += 1;
        }

        while (rightCount[letterIds[s[_end - 1]]] - 1 >= k) {
            _end -= 1;
        }

        const diff = Math.max(
            _start + 1,
            s.length - _end - 1,
        );

        return s.length - diff;
    }


    return s.length - (end - start - 1);
};
var takeCharacters = function(s, k) {
    if (k === 0) return 0;

    const letterCount = [0, 0, 0];
    const letterIds = { a: 0, b: 1, c: 2 };

    for (const char of s) letterCount[letterIds[char]] += 1;

    if (letterCount.some((count) => (count < k))) return -1;

    let res = s.length;
    let l = 0;
    for (let i = 0; i < s.length; ++i) {
        letterCount[letterIds[s[i]]] -= 1;

        while (Math.min(...letterCount) < k) {
            letterCount[letterIds[s[l]]] += 1;
            l += 1;
        }

        res = Math.min(
            res,
            s.length - (i - l + 1),
        );
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: ['aabaaaacaabc', 2],
            output: 8,
        },
        {
            input: ['a', 1],
            output: -1,
        },
        {
            input: ['aacbbcaa', 2],
            output: 6,
        },
        {
            input: ['abc', 1],
            output: 3,
        },
        {
            input: ['bcca', 1],
            output: 3,
        },
        {
            input: ['cbbac', 1],
            output: 3,
        },
    ];

    for (const { input, output } of params) {
        const result = takeCharacters(...input);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${output}
            RESULT: ${result}
            `;

        if (JSON.stringify(result) === JSON.stringify(output)) {
            console.log(
                'SUCCESS: \n', message,
            );
        } else {
            console.error('ERROR: \n', message);
        }
    }
};

test();
