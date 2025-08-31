function sortMatrix(grid: number[][]): number[][] {
    const n: number = grid.length;

    const update = (row: number, col: number, asc: boolean): void => {
        let arr: number[] = [];

        let i: number = 0;
        while (row + i < n && col + i < n) {
            arr.push(grid[row + i][col + i]);
            i += 1;
        }

        arr = asc
            ? arr.sort((a, b) => a - b)
            : arr.sort((a, b) => b - a);

        i = 0
        while (row + i < n && col + i < n) {
            grid[row + i][col + i] = arr[i];
            i += 1;
        }
    }

    for (let row: number = 0; row < n; ++row) {
        update(row, 0, false);
    }
    for (let col: number = 1; col < n; ++col) {
        update(0, col, true);
    }

    return grid;
};

/*

result

[
[ 8, 2, 3 ],
[ 9, 6, 7 ],
[ 4, 5, 1, undefined ]
]

*/

const test = () => {
    const params = [
        {
            input: {
                grid: [[1,7,3],[9,8,2],[4,5,6]],
            },
            output: [[8,2,3],[9,6,7],[4,5,1]],
        },
        {
            input: {
                grid: [[0,1],[1,2]],
            },
            output: [[2,1],[1,0]],
        },
        {
            input: {
                grid: [[1]],
            },
            output: [[1]],
        },
    ];

    params.forEach(({input, output}) => {
        const { grid } = input;
        const result = sortMatrix(grid);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();