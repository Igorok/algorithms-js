function calculateMinimumHP(dungeon: number[][]): number {
    const shifts: number[][] = [[1, 0], [0, 1]];
    const memo: Map<string, number> = new Map();

    const dfs = (r: number, c: number, curr: number, acc: number) => {
        if (r === dungeon.length - 1 && c === dungeon[0].length - 1) {
            return acc;
        }

        let res: number = Number.MAX_SAFE_INTEGER;

        for (const [sr, sc] of shifts) {
            const nr: number = r + sr;
            const nc: number = c + sc;

            if (nr === dungeon.length || nc === dungeon[0].length) {
                continue;
            }


            let na: number = acc;
            if (curr + dungeon[nr][nc] < 0) {
                na += -(curr + dungeon[nr][nc]);
            }
        }


        const diff: number = curr + dungeon[r][c];

        if (curr + dungeon[r][c] <= 0) {
            acc += diff;
            curr = 0;
        }

        return 0;
    }

    const acc: number = dungeon[0][0] >= 0 ? 0 : -dungeon[0][0]
    const r: number = dfs(0, 0, 0, acc);

    return r+1;
};

const test = () => {
    const params = [
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

