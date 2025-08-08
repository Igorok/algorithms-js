function countPyramids(grid: number[][]): number {
    for (let i: number = 0; i < grid.length; ++i) {
        let id: number = 2;

        for (let j: number = 0; j < grid[0].length; ++j) {
            if (grid[i][j] === 1 && j > 0 && grid[i][j-1] === 0) {
                id += 1;
            }

            if (grid[i][j] === 1) {
                grid[i][j] = id;
            }
        }
    }

    const dfsBottom = (row: number, left: number, right: number): number => {
        if (
            row === grid.length ||
            left < 0 || right === grid[0].length ||
            grid[row][left] === 0 || grid[row][left] !== grid[row][right]
        ) {
            return 0;
        }

        return 1 + dfsBottom(row + 1, left-1, right+1);
    }

    const dfsUp = (row: number, left: number, right: number) => {
        if (
            row < 0 ||
            left < 0 || right === grid[0].length ||
            grid[row][left] === 0 || grid[row][left] !== grid[row][right]
        ) {
            return 0;
        }

        return 1 + dfsUp(row - 1, left-1, right+1);
    }

    let res: number = 0;

    for (let i: number = 0; i < grid.length; ++i) {
        for (let j: number = 0; j < grid[0].length; ++j) {
            if (grid[i][j] === 0) {
                continue;
            }
            const b: number = dfsBottom(i, j, j);
            const u: number = dfsUp(i, j, j);

            res += b - 1;
            res += u - 1;
        }
    }

    return res;
};

/*

[
[0,1,1,0],
[1,1,1,1]
],

*/

const test = () => {
    const params = [
        {
            input: {
                grid: [[0,1,1,0],[1,1,1,1]],
            },
            output: 2,
        },
        {
            input: {
                grid: [[1,1,1],[1,1,1]],
            },
            output: 2,
        },
        {
            input: {
                grid: [[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,0,0,1]],
            },
            output: 13,
        },
    ];

    params.forEach(({input, output}) => {
        const { grid } = input;
        const result = countPyramids(grid);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();