/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
    if (!s) return 0;

    let res = 0;
    const stack = [];
    const valid = [];

    for (let i = 0; i < s.length; ++i) {
        if (s[i] === '(') {
            stack.push(i);
        } else {
            if (!stack.length) {
                continue;
            }
            const id = stack.pop();
            res = Math.max(res, (i - id + 1));

            while (valid.length && valid.at(-1)[1] > id) {
                valid.pop();
            }

            if (valid.length && valid.at(-1)[1] === id - 1) {
                const left = valid.pop();
                valid.push([left[0], i]);

                res = Math.max(res, (i - left[0] + 1));
            } else {
                valid.push([id, i]);
            }
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: "(()",
            output: 2,
        },
        {
            input: ")()())",
            output: 4,
        },
        {
            input: "",
            output: 0,
        },
        {
            input: ")()()(((((((()(()())",
            output: 8,
        },
        {
            input: "((()))())",
            output: 8,
        },
    ];

    params.forEach(({input, output}) => {
        const result = longestValidParentheses(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();