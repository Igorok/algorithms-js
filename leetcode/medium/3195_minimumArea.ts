function minimumArea(grid: number[][]): number {
    let top: number = grid.length;
    let bottom: number = -1;
    let left: number = grid[0].length;
    let right: number = -1;

    for (let row: number = 0; row < grid.length; ++row) {
        for (let col: number = 0; col < grid[0].length; ++col) {
            if (grid[row][col] === 0) continue;

            top = Math.min(top, row);
            bottom = Math.max(bottom, row);
            left = Math.min(left, col);
            right = Math.max(right, col);
        }
    }

    return (right - left + 1) * (bottom - top + 1);
};

const test = () => {
    const params = [
        {
            input: {
                grid: [[0,1,0],[1,0,1]],
            },
            output: 6,
        },
        {
            input: {
                grid: [[1,0],[0,0]]
            },
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const { grid } = input;
        const result = minimumArea(grid);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();