function numEnclaves(grid: number[][]): number {
    const shifts: number[][] = [[-1, 0], [1, 0], [0, -1], [0, 1]];

    const n: number = grid.length;
    const m: number = grid[0].length;
    let total: number = 0;
    let idIsland: number = 2;
    const sumByIsland: Map<number, number> = new Map();

    const dfs = (row: number, coll: number): number => {
        let sum: number = 1;
        grid[row][coll] = idIsland;

        for (const [sR, sC] of shifts) {
            const newR: number = row + sR;
            const newC: number = coll + sC;

            if (newR === -1 || newR === n || newC === -1 || newC === m || grid[newR][newC] !== 1) {
                continue;
            }

            sum += dfs(newR, newC);
        }

        return sum;
    };

    for (let i: number = 0; i < n; ++i) {
        for (let j: number = 0; j < m; ++j) {
            if (grid[i][j] === 1) {
                const sum: number = dfs(i, j);
                sumByIsland.set(idIsland, sum);
                total += sum;
                idIsland += 1;
            }
        }
    }

    const used: Set<number> = new Set();
    for (let i: number = 0; i < n; ++i) {
        if (grid[i][0] !== 0 && !used.has(grid[i][0])) {
            used.add(grid[i][0]);
            total -= (sumByIsland.get(grid[i][0]) || 0);
        }
        if (grid[i][m-1] !== 0 && !used.has(grid[i][m-1])) {
            used.add(grid[i][m-1]);
            total -= (sumByIsland.get(grid[i][m-1]) || 0);
        }
    }

    for (let i: number = 0; i < m; ++i) {
        if (grid[0][i] !== 0 && !used.has(grid[0][i])) {
            used.add(grid[0][i]);
            total -= (sumByIsland.get(grid[0][i]) || 0)
        }
        if (grid[n-1][i] !== 0 && !used.has(grid[n-1][i])) {
            used.add(grid[n-1][i]);
            total -= (sumByIsland.get(grid[n-1][i]) || 0)
        }
    }


    return total;
};

const test = () => {
    const params = [
        {
            input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]],
            output: 3,
        },
        {
            input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]],
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const result = numEnclaves(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();
