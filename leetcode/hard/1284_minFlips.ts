function minFlips(mat: number[][]): number {
    const memo: Map<string, number> = new Map();

    const flip = (row: number, col: number) => {
        const values: number[] = [1, 0];
        const shifts: number[][] = [[-1, 0], [1, 0], [0, -1], [0, 1]];

        const val: number = mat[row][col];
        mat[row][col] = values[val];

        for (const [sr, sc] of shifts) {
            const newRow: number = row + sr;
            const newCol: number = col + sc;

            if (newRow < 0 || newRow === mat.length || newCol < 0 || newCol === mat[0].length) {
                continue;
            }

            const val: number = mat[newRow][newCol];
            mat[newRow][newCol] = values[val];
        }
    };

    const getSum = () => {
        let sum: number = 0;
        for (let row: number = 0; row < mat.length; ++row) {
            for (let col: number = 0; col < mat[0].length; ++col) {
                sum += mat[row][col];
            }
        }
        return sum;
    }

    const dfs = (step: number) => {
        let sum: number = getSum();
        if (sum === 0) {
            return 0;
        }

        const key: string = mat.map((row) => row.join('_')).join('_');
        const val: number|undefined = memo.get(key);
        if (val !== undefined) {
            return val;
        }

        memo.set(key, -1);

        let res: number = Number.MAX_SAFE_INTEGER;

        for (let row: number = 0; row < mat.length; ++row) {
            for (let col: number = 0; col < mat[0].length; ++ col) {
                flip(row, col);

                const r: number = dfs(step + 1);
                if (r !== -1) {
                    res = Math.min(res, r+1);
                }

                flip(row, col);
            }
        }

        res = (res === Number.MAX_SAFE_INTEGER) ? -1 : res;

        memo.set(key, res);

        return res;
    };

    return dfs(0);
};

const test = () => {
    const params = [
        {
            input: {
                mat: [[0,0],[0,1]],
            },
            output: 3,
        },
        {
            input: {
                mat: [[0]],
            },
            output: 0,
        },
        {
            input: {
                mat: [[1,0,0],[1,0,0]],
            },
            output: -1,
        },
    ];

    params.forEach(({input, output}) => {
        const { mat } = input;

        const result = minFlips(mat);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();