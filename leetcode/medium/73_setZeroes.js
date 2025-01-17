/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    let firstColumn = 1;
    let firstRow = 1;
    for (let i = 0; i < matrix.length; ++i) {
        for (let j = 0; j < matrix[0].length; ++j) {
            if (matrix[i][j] === 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
                if (j === 0) {
                    firstColumn = 0;
                }
                if (i === 0) {
                    firstRow = 0;
                }
            }
        }
    }

    // row
    for (let i = 1; i < matrix.length; ++i) {
        if (matrix[i][0] === 0) {
            for (let j = 0; j < matrix[0].length; ++j) {
                matrix[i][j] = 0;
            }
        }
    }
    // column
    for (let i = 1; i < matrix[0].length; ++i) {
        if (matrix[0][i] === 0) {
            for (let j = 0; j < matrix.length; ++j) {
                matrix[j][i] = 0;
            }
        }
    }
    // row
    if (firstRow === 0) {
        for (let i = 0; i < matrix[0].length; ++i) {
            matrix[0][i] = 0;
        }
    }
    // column
    if (firstColumn === 0) {
        for (let i = 0; i < matrix.length; ++i) {
            matrix[i][0] = 0;
        }
    }

    return matrix;
};

/*

[0,1,2,0],
[3,4,5,2],
[1,3,1,5]


*/

const test = () => {
    const params = [
        {
            input: [[1,1,1],[1,0,1],[1,1,1]],
            output: [[1,0,1],[0,0,0],[1,0,1]],
        },
        {
            input: [[0,1,2,0],[3,4,5,2],[1,3,1,5]],
            output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]],
        },
    ];

    params.forEach(({input, output}) => {
        const result = setZeroes(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();