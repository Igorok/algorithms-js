function onesMinusZeros(grid: number[][]): number[][] {
    const rowDiff: number[] = new Array(grid.length).fill(0);
    const colDiff: number[] = new Array(grid[0].length).fill(0);

    for (let i: number = 0; i < grid.length; ++i) {
        for (let j: number = 0; j < grid[0].length; ++j) {
            const val: number = grid[i][j] === 1 ? 1 : -1;
            rowDiff[i] += val;
            colDiff[j] += val;
        }
    }

    const res: number[][] = new Array(grid.length).fill(0).map(() => new Array(grid[0].length).fill(0));

    for (let i: number = 0; i < grid.length; ++i) {
        for (let j: number = 0; j < grid[0].length; ++j) {
            res[i][j] = rowDiff[i] + colDiff[j];
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                grid: [[0,1,1],[1,0,1],[0,0,1]],
            },
            output: [[0,0,4],[0,0,4],[-2,-2,2]],
        },
        {
            input: {
                grid: [[1,1,1],[1,1,1]],
            },
            output: [[5,5,5],[5,5,5]],
        },
    ];

    params.forEach(({ input, output }) => {
        const { grid } = input;
        const result = onesMinusZeros(grid);

        console.log(
            JSON.stringify(result) === JSON.stringify(output)
                ? "SUCCESS "
                : "ERROR ",
            "input",
            JSON.stringify(input),
            "output",
            output,
            "result",
            result,
        );
    });
};

test();
