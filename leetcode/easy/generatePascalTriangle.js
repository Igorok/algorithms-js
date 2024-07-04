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
var generate = function(numRows) {
    if (!numRows) return [];
    if (numRows == 1) return [[1]];
    if (numRows == 2) return [[1], [1, 1]];

    const triangle = [[1], [1, 1]];

    for (let i = 2; i < numRows; ++i) {
        const line = new Array(triangle[i - 1].length + 1).fill(1);
        const middle = (line.length) / 2;

        for (let j = 1; j < middle; ++j) {
            const val = triangle[i - 1][j - 1] + triangle[i - 1][j];
            line[j] = val;
            line[line.length - 1 - j] = val;
        }

        triangle.push(line);
    }

    return triangle;
};

const test = () => {
    const params = [
        {
            input: 5,
            output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]],
        },
        {
            input: 1,
            output: [[1]],
        },
    ];

    params.forEach(({input, output}) => {
        const result = generate(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', input,
            'output', output,
            'result', result,
        );

    });
};

test();
