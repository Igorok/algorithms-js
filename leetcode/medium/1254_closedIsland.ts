function closedIsland(grid: number[][]): number {
    const shifts: number[][] = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    const n: number = grid.length;
    const m: number = grid[0].length;

    let idOfIsland: number = 3;

    const dfs = (row: number, coll: number): void => {
        for (const [sRow, sCol] of shifts) {
            const newRow: number = row + sRow;
            const newCol: number = coll + sCol;

            if (newRow < 0 || newRow >= n || newCol < 0 || newCol >= m) {
                continue;
            }

            if (grid[newRow][newCol] !== 0) {
                continue;
            }

            grid[newRow][newCol] = idOfIsland;

            dfs(newRow, newCol);
        }
    };

    for (let i: number = 0; i < n; ++i) {
        for (let j: number = 0; j < m; ++j) {
            if (grid[i][j] === 0) {
                grid[i][j] = idOfIsland;
                dfs(i, j);
                idOfIsland += 1;
            }
        }
    }

    const marked: Set<number> = new Set();

    for (let i: number = 0; i < n; ++i) {
        if (grid[i][0] !== 1 && !marked.has(grid[i][0])) {
            marked.add(grid[i][0]);
            idOfIsland -= 1;
        }
        if (grid[i][m-1] !== 1 && !marked.has(grid[i][m-1])) {
            marked.add(grid[i][m-1]);
            idOfIsland -= 1;
        }
    }

    for (let i: number = 0; i < m; ++i) {
        if (grid[0][i] !== 1 && !marked.has(grid[0][i])) {
            marked.add(grid[0][i]);
            idOfIsland -= 1
        }
        if (grid[n-1][i] !== 1 && !marked.has(grid[n-1][i])) {
            marked.add(grid[n-1][i]);
            idOfIsland -= 1
        }
    }

    return idOfIsland - 3;
};

const test = () => {
    const params = [
        {
            input: {
                grid: [
                    [1,1,1,1,1,1,1,0],
                    [1,0,0,0,0,1,1,0],
                    [1,0,1,0,1,1,1,0],
                    [1,0,0,0,0,1,0,1],
                    [1,1,1,1,1,1,1,0]
                ],
            },
            output: 2,
        },
        {
            input: {
                grid: [
                    [0,0,1,0,0],
                    [0,1,0,1,0],
                    [0,1,1,1,0]
                ],
            },
            output: 1,
        },
        {
            input: {
                grid: [
                    [1,1,1,1,1,1,1],
                    [1,0,0,0,0,0,1],
                    [1,0,1,1,1,0,1],
                    [1,0,1,0,1,0,1],
                    [1,0,1,1,1,0,1],
                    [1,0,0,0,0,0,1],
                    [1,1,1,1,1,1,1]
                ],
            },
            output: 2,
        },
    ];

    params.forEach(({input, output}) => {
        const { grid } = input;
        const result = closedIsland(grid);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();