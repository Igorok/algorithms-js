/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    const getNumEnd = (id) => {
        let e = id + 1;
        while (e < s.length && s[e].match(/\d/)) {
            e += 1;
        }
        return e;
    };

    const rec = (id) => {
        let res = 0;
        const operators = [];

        const applyNum = (num) => {
            if (!operators.length) {
                res += num;
                return;
            }
            const op = operators.pop();
            if (op === '-') {
                res -= num;
            } else {
                res += num;
            }
        };

        let i = id;
        while (i < s.length) {
            if (s[i] === ' ') {
                i += 1;
                continue;
            }
            if (s[i] === '(') {
                const [num, e] = rec(i + 1);
                applyNum(num);
                i = e;
                continue;
            }
            if ('+-'.includes(s[i])) {
                operators.push(s[i]);
                i += 1;
                continue;
            }
            if (s[i].match(/\d/)) {
                const e = getNumEnd(i);
                const num = Number(s.slice(i, e));
                applyNum(num);
                i = e;
                continue;
            }

            if (s[i] === ')') {
                return [res, i + 1];
            }
        }

        return [res, i];
    }

    const res = rec(0);

    return res[0];
};

const test = () => {
    const params = [
        {
            input: "1 + 1",
            output: 2,
        },
        {
            input: " 2-1 + 2 ",
            output: 3,
        },
        {
            input: "(1+(4+5+2)-3)+(6+8)",
            output: 23,
        },
    ];

    for (const { input, output } of params) {
        const result = calculate(input);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${JSON.stringify(output)}
            RESULT: ${JSON.stringify(result)}`;

        if (JSON.stringify(result) === JSON.stringify(output)) {
            console.log(
                `SUCCESS: ${message}`,
            );
        } else {
            console.error(`ERROR: ${message}`);
        }
    }
};

test();
