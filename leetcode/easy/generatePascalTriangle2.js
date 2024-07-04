/*

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]


[
    [1],
    [1,1],
    [1,2,1],
    [1,3,3,1],
    [1,4,6,4,1],
    [1, 5, 10, 10, 5 ,1]
]


*/

/**
 * @param {number} numRows
 * @return {number[][]}
 */
var getRow = function(numRows) {
    if (numRows == 0) return [1];
    if (numRows == 1) return [1, 1];

    let prev = [1, 1];

    for (let i = 2; i <= numRows; ++i) {
        const line = new Array(prev.length + 1).fill(1);
        const middle = (line.length) / 2;

        for (let j = 1; j < middle; ++j) {
            const val = prev[j - 1] + prev[j];
            line[j] = val;
            line[line.length - 1 - j] = val;
        }

        prev = line;
    }

    return prev;
};

const test = () => {
    const params = [
        {
            input: 3,
            output: [1,3,3,1],
        },
        {
            input: 0,
            output: [1],
        },
        {
            input: 1,
            output: [1,1],
        },
        {
            input: 2,
            output: [1,2,1],
        },
    ];

    params.forEach(({input, output}) => {
        const result = getRow(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', input,
            'output', output,
            'result', result,
        );

    });
};

test();
