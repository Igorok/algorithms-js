/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
    let isNegativeRow: boolean = false;
    let isNegativeColumn: boolean = false;

    for (let i: number = 0; i < matrix.length; ++i) {
        for (let j: number = 0; j < matrix[0].length; ++j) {
            if (matrix[i][j] === 0) {
                matrix[0][j] = 0;
                matrix[i][0] = 0;

                if (i === 0) {
                    isNegativeRow = true;
                }
                if (j === 0) {
                    isNegativeColumn = true;
                }
            }
        }
    }

    for (let i: number = 1; i < matrix.length; ++i) {
        for (let j: number = 1; j < matrix[0].length; ++j) {
            if (matrix[0][j] === 0) {
                matrix[i][j] = 0;
            }
            if (matrix[i][0] === 0) {
                matrix[i][j] = 0;
            }
        }
    }

    if (isNegativeColumn) {
        for (let i: number = 0; i < matrix.length; ++i) {
            matrix[i][0] = 0;
        }
    }
    if (isNegativeRow) {
        for (let i: number = 0; i < matrix[0].length; ++i) {
            matrix[0][i] = 0;
        }
    }

};

const test = () => {
    const params = [
        {
            input: [[0,1,2,0],[3,4,5,2],[1,3,1,5]],
            output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]],
        },
        {
            input: [[1,1,1],[1,0,1],[1,1,1]],
            output: [[1,0,1],[0,0,0],[1,0,1]],
        },
    ];

    params.forEach(({input, output}) => {
        setZeroes(input);

        console.log(
            JSON.stringify(input) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(input),
        );
    });
};

test();