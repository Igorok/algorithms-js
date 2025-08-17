function removeInvalidParentheses(s: string): string[] {
    const closedSum: number[] = new Array(s.length).fill(0);
    if (s.at(-1) === ')') {
        closedSum[s.length - 1] = 1;
    }
    for (let i = s.length - 2; i > -1; --i) {
        closedSum[i] = closedSum[i+1];
        if (s.at(i) === ')') {
            closedSum[i] += 1;
        }
    }

    let res: string[] = [];

    const dfs = (id: number, open: number, closed: number, acc: string) => {
        if (id === s.length) {
            if (open !== closed) {
                return;
            }
            if (res.length === 0 || res[0].length < acc.length) {
                res = [acc];
            }
            if (res[0].length === acc.length) {
                res.push(acc);
            }
            return;
        }

        if (id !== s.length) {
            const diff: number = open - closed;
            if (diff > closedSum[id]) {
                return;
            }
        }

        if (s[id] !== '(' && s[id] !== ')') {
            return dfs(id + 1, open, closed, acc + s[id]);
        }

        if (s[id] === ')') {
            if (closed + 1 > open) {
                return dfs(id + 1, open, closed, acc);
            }
            dfs(id + 1, open, closed + 1, acc + s[id]);
            dfs(id + 1, open, closed, acc);
        }

        if (s[id] === '(') {
            dfs(id + 1, open + 1, closed, acc + s[id]);
            dfs(id + 1, open, closed, acc);
            return;
        }
    }

    dfs(0, 0, 0, '');


    return [...new Set(res)];
};


/*

s: "()())()",

()())()
)
()
)()--)()--))()--))()--())()
----------------)()---()()
-----()---)()---)()---()()
----------------()----(()--()

*/

const test = () => {
    const params = [
        {
            input: {
                s: ")()(",
            },
            output: ["()"],
        },
        {
            input: {
                s: "()())()",
            },
            output: ["(())()","()()()"],
        },
        {
            input: {
                s: "(a)())()"
            },
            output: ["(a())()","(a)()()"],
        },
        {
            input: {
                s: ")(",
            },
            output: [""],
        },
        {
            input: {
                s: "(((((((((((((((((((((((()",
            },
            output: ["()"],
        },
    ];

    params.forEach(({input, output}) => {
        const { s } = input;
        const result = removeInvalidParentheses(s);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

