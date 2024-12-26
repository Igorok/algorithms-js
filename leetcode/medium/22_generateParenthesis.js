/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    const res = [];

    const rec = (open, close, str) => {
        if (open > 0) {
            rec(open - 1, close, str + '(');
        }
        if (close > 0 && close > open) {
            rec(open, close - 1, str + ')');
        }
        if (!open && !close) {
            res.push(str);
        }
    };

    rec(n, n, '');

    return res;
};


const test = () => {
    const params = [
        {
            input: 3,
            output: ['((()))','(()())','(())()','()(())','()()()'],
        },
        {
            input: 1,
            output: ['()'],
        },
    ];

    params.forEach(({input, output}) => {
        const result = generateParenthesis(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();