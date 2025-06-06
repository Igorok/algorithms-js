function shortestBridge(grid: number[][]): number {
    const n: number = grid.length;
    const m: number = grid[0].length;

    const shifts: number[][] = [[-1, 0], [1, 0], [0, -1], [0, 1]];

    const queue: number[][] = [];

    const markIsland = (r: number, c: number) => {
        for (const [shiftR, shiftC] of shifts) {
            const newR: number = r + shiftR;
            const newC: number = c + shiftC;

            if (newR === -1 || newR === n || newC === -1 || newC === m) {
                continue;
            }

            if (grid[newR][newC] === 0) {
                queue.push([newR, newC, 1]);
            }

            if (grid[newR][newC] === 1) {
                grid[newR][newC] = 2;
                markIsland(newR, newC);
            }
        }
    };

    for (let i: number = 0; i < n; ++i) {
        let found: boolean = false;

        for (let j: number = 0; j < m; ++j) {
            if (grid[i][j] === 1) {
                grid[i][j] = 2;
                markIsland(i, j);
                found = true;
                break;
            }
        }

        if (found) {
            break;
        }
    }

    while (queue.length) {
        const [r, c, length] = queue.shift();
        if (grid[r][c] === 1) {
            return length - 1;
        }

        if (grid[r][c] === 2 || grid[r][c] === 3) {
            continue;
        }

        grid[r][c] = 3;

        for (const [shiftR, shiftC] of shifts) {
            const newR: number = r + shiftR;
            const newC: number = c + shiftC;

            if (newR === -1 || newR === n || newC === -1 || newC === m || grid[newR][newC] === 2 || grid[newR][newC] === 3) {
                continue;
            }

            queue.push([newR, newC, length + 1]);
        }
    }

    return 0;
};

/*

[
[0,1],
[1,0]
]

[
[3,1,3],
[0,3,3],
[0,3,1]
]

*/

const test = () => {
    const params = [
        {
            input: {
                grid: [[0,1],[1,0]]
            },
            output: 1,
        },
        {
            input: {
                grid: [[0,1,0],[0,0,0],[0,0,1]]
            },
            output: 2,
        },
        {
            input: {
                grid: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
            },
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const { grid } = input;
        const result = shortestBridge(grid);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();