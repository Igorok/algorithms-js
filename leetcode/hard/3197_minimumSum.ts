function minimumSum(grid: number[][]): number {
    const memo: number[][][][] = [];
    for (let i: number = 0; i < grid.length; ++i) {
        memo.push([]);

        for (let j: number = 0; j < grid[0].length; ++j) {
            memo[i].push([]);

            for (let k: number = 0; k < grid.length + 1; ++k) {
                memo[i][j].push(new Array(grid[0].length + 1).fill(-1));

                // for (let l: number = 0; l < grid[0].length + 1; ++l) {
                //     memo[i][j][k].push(-1);
                // }
            }
        }
    }


    const getSquare = (start: number[], end: number[]) => {
        const cache: number = memo[start[0]][start[1]][end[0]][end[1]];
        if (cache !== -1) return cache;

        let top: number = end[0];
        let bottom: number = start[0];
        let left: number = end[1];
        let right: number = start[1];

        for (let row: number = start[0]; row < end[0]; ++row) {
            for (let col: number = start[1]; col < end[1]; ++col) {
                if (grid[row][col] === 0) continue;

                top = Math.min(top, row);
                bottom = Math.max(bottom, row);
                left = Math.min(left, col);
                right = Math.max(right, col);
            }
        }

        memo[start[0]][start[1]][end[0]][end[1]] = (bottom - top + 1) * (right - left + 1);

        return (bottom - top + 1) * (right - left + 1);
    };

    let res: number = Number.MAX_SAFE_INTEGER;

    if (grid.length > 2) {
        for (let row: number = 1; row < grid.length - 1; ++row) {
            const s1: number = getSquare([0, 0], [row, grid[0].length]);

            for (let row1: number = row + 1; row1 < grid.length; ++row1) {
                const s2: number = getSquare([row, 0], [row1, grid[0].length]);
                const s3: number = getSquare([row1, 0], [grid.length, grid[0].length]);

                res = Math.min(res, s1 + s2 + s3);
            }
        }
    }

    if (grid[0].length > 2) {
        for (let col: number = 1; col < grid[0].length - 1; ++col) {
            const s1: number = getSquare([0, 0], [grid.length, col]);

            for (let col1: number = col+1; col1 < grid[0].length; ++col1) {
                const s2: number = getSquare([0, col], [grid.length, col1]);
                const s3: number = getSquare([0, col1], [grid.length, grid[0].length]);

                res = Math.min(res, s1 + s2 + s3);
            }
        }
    }

    for (let row: number = 1; row < grid.length; ++row) {
        for (let col: number = 1; col < grid[0].length; ++col) {
            // 1
            let s1: number = getSquare([0, 0], [row, grid[0].length]);
            let s2: number = getSquare([row,0], [grid.length, col]);
            let s3: number = getSquare([row, col], [grid.length, grid[0].length]);
            res = Math.min(res, s1 + s2 + s3);

            // 2
            s1 = getSquare([0, 0], [row, col]);
            s2 = getSquare([0, col], [row, grid[0].length]);
            s3 = getSquare([row, 0], [grid.length, grid[0].length]);
            res = Math.min(res, s1 + s2 + s3);

            // 3
            s1 = getSquare([0, 0], [grid.length, col]);
            s2 = getSquare([0, col], [row, grid[0].length]);
            s3 = getSquare([row, col], [grid.length, grid[0].length]);
            res = Math.min(res, s1 + s2 + s3);

            // 4
            s1 = getSquare([0, 0], [row, col]);
            s2 = getSquare([row, 0], [grid.length, col]);
            s3 = getSquare([0, col], [grid.length, grid[0].length]);
            res = Math.min(res, s1 + s2 + s3);
        }
    }

    return res;
};

/*

729_000_000

[
    [0,0,0,0,1],
    [1,1,1,0,1],
    [0,1,0,0,1]
]





*/

const test = () => {
    const params = [
        {
            input: {
                grid: [
                    [0,0,0],
                    [0,0,0],
                    [0,0,1],
                    [1,1,0]
                ],
            },
            output: 3,
        },



        {
            input: {
                grid: [
                    [1,0,1],
                    [1,1,1]
                ],
            },
            output: 5,
        },
        {
            input: {
                grid: [[1,0,1,0],[0,1,0,1]],
            },
            output: 5,
        },
        {
            input: {
                grid: [
                    [0,0,0,0,1],
                    [1,1,1,0,1],
                    [0,1,0,0,1]
                ],
            },
            output: 7,
        },
        {
            input: {
                grid: [[1],[1],[0],[1]],
            },
            output: 3,
        },
    ];

    params.forEach(({input, output}) => {
        const { grid } = input;

        const result = minimumSum(grid);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();