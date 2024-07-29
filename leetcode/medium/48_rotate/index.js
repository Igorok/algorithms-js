/**
 Do not return anything, modify matrix in-place instead.
*/
function rotate(matrix) {
    let start = 0;
    let end = matrix.length - 1;
    while (start < end) {
        for (let i = 0; i < (end - start); ++i) {
            let left = start;
            let right = end;
            let top = start;
            let bottom = end;

            const tmp = matrix[top][left + i];

            matrix[top][left + i] = matrix[bottom - i][left];
            matrix[bottom - i][left] = matrix[bottom][right - i];
            matrix[bottom][right - i] = matrix[top + i][right];
            matrix[top + i][right] = tmp;
        }

        start += 1;
        end -= 1;
    }
};

/*
[
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]

[
    [15,13,2,5],
    [14,3,4,1],
    [12,6,8,9],
    [16,7,10,11]
]

[
    [15,13,2,5],
    [14,6,3,1],
    [12,8,4,9],
    [16,7,10,11]]
*/

const test = () => {
    const params = [
        {
            input: [[1,2,3],[4,5,6],[7,8,9]],
            output: [[7,4,1],[8,5,2],[9,6,3]],
        },
        {
            input: [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
            output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]],
        },
    ];

    params.forEach(({ input, output }) => {
        const i = JSON.parse(JSON.stringify(input));

        rotate(i);

        console.log(
            JSON.stringify(i) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(i),
        );
    });
};
test();
