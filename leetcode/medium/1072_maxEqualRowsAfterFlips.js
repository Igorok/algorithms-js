/**
 * @param {number[][]} matrix
 * @return {number}
 */
var maxEqualRowsAfterFlips = function(matrix) {
    const rowsCount = new Map();
    let res = 0;
    for (const row of matrix) {
        const rowKey = row[0] ? row.join('_') : row.map(v => v ? 0 : 1).join('_');
        const count = (rowsCount.get(rowKey) || 0) + 1;
        rowsCount.set(rowKey, count);
        res = Math.max(res, count);
    }
    return res;
};

/*



*/

const test = () => {
    const params = [
        {
            input: [[0,1],[1,1]],
            output: 1,
        },
        {
            input: [[0,1],[1,0]],
            output: 2,
        },
        {
            input: [[0,0,0],[0,0,1],[1,1,0]],
            output: 2,
        },
    ];

    for (const { input, output } of params) {
        const result = maxEqualRowsAfterFlips(input);
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
