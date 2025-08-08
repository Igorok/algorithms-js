function longestIncreasingPath(matrix: number[][]): number {
    const shifts: number[][] = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    const memo: number[][] = new Array(matrix.length).fill(0).map(() => new Array(matrix[0].length).fill(-1));

    const dfs = (row: number, col: number) => {
        if (memo[row][col] !== -1) {
            return memo[row][col];
        }

        let res: number = 0;

        for (const [sr, sc] of shifts) {
            const newRow = sr + row;
            const newCol = sc + col;

            if (newRow < 0 || newRow === matrix.length || newCol < 0 || newCol === matrix[0].length) {
                continue;
            }
            if (matrix[newRow][newCol] <= matrix[row][col]) {
                continue;
            }

            const r: number = dfs(newRow, newCol);
            res = Math.max(res, r);
        }

        memo[row][col] = res + 1;

        return memo[row][col];
    };

    let res: number = 0;
    for (let row: number = 0; row < matrix.length; ++row) {
        for (let col: number = 0; col < matrix[0].length; ++col) {
            const r: number = dfs(row, col);
            res = Math.max(res, r);
        }
    }


    return res;
};

const test = () => {
    const params = [
        {
            input: {
                matrix: [[0],[1],[5],[5]],
            },
            output: 3,
        },
        {
            input: {
                matrix: [[9,9,4],[6,6,8],[2,1,1]],
            },
            output: 4,
        },
        {
            input: {
                matrix: [[3,4,5],[3,2,6],[2,2,1]],
            },
            output: 4,
        },
        {
            input: {
                matrix: [[1]],
            },
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const { matrix } = input;

        const result = longestIncreasingPath(matrix);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();