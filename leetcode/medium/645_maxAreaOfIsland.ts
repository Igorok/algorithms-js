function maxAreaOfIsland(grid: number[][]): number {
    const shifts: number[][] = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    const n: number = grid.length;
    const m: number = grid[0].length;

    const dfs = (row: number, coll: number): number => {
        let res: number = 1;

        for (const [sRow, sColl] of shifts) {
            const newRow: number = row + sRow;
            const newColl: number = coll + sColl;

            if (newRow === -1 || newRow === n || newColl === -1 || newColl === m) {
                continue;
            }

            if (grid[newRow][newColl] !== 1) {
                continue;
            }

            grid[newRow][newColl] = 2;
            res += dfs(newRow, newColl);
        }

        return res;
    };

    let res: number = 0;
    for (let i: number = 0; i < n; ++i) {
        for (let j: number = 0; j < m; ++j) {
            if (grid[i][j] !== 1) {
                continue;
            }
            grid[i][j] = 2;
            const r: number = dfs(i, j);
            res = Math.max(res, r);
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]],
            output: 6,
        },
        {
            input: [[0,0,0,0,0,0,0,0]],
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const result = maxAreaOfIsland(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

