
function calculateMinimumHP(dungeon: number[][]): number {
    const shifts: number[][] = [[1, 0], [0, 1]];

    const memo: number[][] = new Array(dungeon.length).fill(0).map(() => new Array(dungeon[0].length).fill(-1));

    const dfs = (row: number, col: number) => {
        if (row === dungeon.length - 1 && col === dungeon[0].length - 1) {
            const r: number = dungeon.at(-1).at(-1);
            return r >= 0 ? 0 : r;
        }

        if (memo[row][col] !== -1) {
            return memo[row][col];
        }

        let res: number = Number.MIN_SAFE_INTEGER;


        for (const [sr, sc] of shifts) {
            const newRow: number = row + sr;
            const newCol: number = col + sc;

            if (newRow === dungeon.length || newCol === dungeon[0].length) {
                continue;
            }

            let r: number = dfs(newRow, newCol);
            r += dungeon[row][col];


            res = Math.max(res, r);
        }

        memo[row][col] = res >= 0 ? 0 : res;


        return memo[row][col];
    };


    let res: number = dfs(0, 0);
    return 1 + (res >= 0 ? 0 : -res);
};

const test = () => {
    const params = [
        {
            input: {
                dungeon: [[-3,5]],
            },
            output: 4,
        },
        {
            input: {
                dungeon: [
                    [-2,-3,3],
                    [-5,-10,1],
                    [10,30,-5]
                ],
            },
            output: 7,
        },
        {
            input: {
                dungeon: [[0]],
            },
            output: 1,
        },
        {
            input: {
                dungeon: [
                    [ 3, -20, 30],
                    [-3,   4,  0]
                ],
            },
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const { dungeon } = input;
        const result = calculateMinimumHP(dungeon);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

