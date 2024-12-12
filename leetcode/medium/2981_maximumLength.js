/**
 * @param {string} s
 * @return {number}
 */
var maximumLength = function(s) {
    const cache = {};

    const isThrice = (char, num) => {
        let count = 0;
        let length = 0;

        for (let i = 0; i < num; ++i) {
            if (s[i] === char) {
                length += 1;
            }
        }
        if (length === num) {
            count += 1;
        }

        for (let i = 1; i <= s.length - num; ++i) {
            if (s[i-1] === char) {
                length -= 1;
            }
            if (s[i-1+num] === char) {
                length += 1;
            }
            if (length === num) {
                count += 1;
                if (count === 3) return true;
            }
        }


        return false;
    };



    const binSearch = (char) => {
        if (cache[char]) return cache[char];

        let start = 1;
        let end = s.length - 1;

        let res = -1;
        while (start <= end) {
            const m = Math.round((start + end) / 2);
            if (isThrice(char, m)) {
                res = m;
                start = m + 1;
            } else {
                end = m - 1;
            }
        }

        cache[char] = res;

        return res;
    };

    let res = -1;
    for (const char of s) {
        res = Math.max(res, binSearch(char));
    }

    return res;
};


const test = () => {
    const params = [
        {
            input: "aaaa",
            output: 2,
        },
        {
            input: "abcdef",
            output: -1,
        },
        {
            input: "abcaba",
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const result = maximumLength(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();