function countSquares(matrix: number[][]): number {
    let res: number = 0;

    for (let i: number = 0; i < matrix.length; ++i) {
        for (let j: number = 0; j < matrix[0].length; ++j) {
            if (matrix[i][j] === 0) continue;

            const top: number = i > 0 ? matrix[i-1][j] : 0;
            const left: number = j > 0 ? matrix[i][j-1] : 0;
            const diagonal: number = (i > 0 && j > 0) ? matrix[i-1][j-1] : 0;

            matrix[i][j] = Math.min(top, left, diagonal) + 1;
            res += matrix[i][j];
        }
    }

    return res;
};


/*
[0,1,1,1],
[1,1,1,1],
[0,1,1,1]


0,1,1,1 -   3
1,1,2,2 -   1+1+(1+1)+(1+1)=6
0,1,2,3 -   1+(1+1)+(1+1+1)=6
6+6+3=15


[1,0,1],
[1,1,0],
[1,1,0]

[1,0,1], 2
[1,1,0], 2
[1,2,0]   1+2 = 7

*/

const test = () => {
    const params = [
        {
            input: {
                matrix: [
                    [0,1,1,1],
                    [1,1,1,1],
                    [0,1,1,1]
                ],
            },
            output: 15,
        },
        {
            input: {
                matrix: [
                    [1,0,1],
                    [1,1,0],
                    [1,1,0]
                ],
            },
            output: 7,
        },
    ];

    params.forEach(({input, output}) => {
        const { matrix } = input;
        const result = countSquares(matrix);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();