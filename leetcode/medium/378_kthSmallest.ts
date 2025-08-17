function kthSmallest_0(matrix: number[][], k: number): number {
    const arr: number[] = matrix.reduce((acc, row) => acc.concat(row), []);
    arr.sort((a, b) => a - b);
    return arr[k-1];
};

function kthSmallest(matrix: number[][], k: number): number {
    let count: number = 0;
    let row: number = 0;
    let col: number = 0;

    while (count < k) {
        if (count + 1 === k) {
            return matrix[row][col];
        }
    }

    return -1;
};

/*

1, 2, 3, 10,
2, 3, 4, 11
5, 6, 7, 12
10,11,12,13

*/

const test = () => {
    const params = [
        {
            input: {
                matrix: [
                    [1, 5,  9],
                    [10,11,13],
                    [12,13,15]
                ],
                k : 8,
            },
            output: 13,
        },
        {
            input: {
                matrix: [[-5]], k: 1
            },
            output: -5,
        },
    ];

    params.forEach(({input, output}) => {
        const { matrix, k } = input;
        const result = kthSmallest(matrix, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

