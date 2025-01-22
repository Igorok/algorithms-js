/**
 * @param {number} n
 * @return {string[]}
 */
var validStrings = function(n) {
    if (!n) return [];

    const res = [];

    const rec = (str) => {
        if (str.length === n) {
            res.push(str);
            return;
        }

        rec(str + '1');
        if (str.at(-1) === '1') {
            rec(str + '0');
        }
    }

    rec('1');
    rec('0');

    return res;
};

const test = () => {
    const params = [
        {
            input: 3,
            output: ["010","011","101","110","111"],
        },
        {
            input: 1,
            output: ["0","1"],
        },
    ];

    for (const { input, output } of params) {
        const result = validStrings(input);
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
