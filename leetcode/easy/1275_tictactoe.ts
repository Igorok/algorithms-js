function tictactoe(moves: number[][]): string {
    const rows: string[][] = new Array(3).fill(0).map(() => []);
    const colls: string[][] = new Array(3).fill(0).map(() => []);
    const topDown: string[] = [];
    const downTop: string[] = [];

    const topDownKeys = new Set(['0_0', '1_1', '2_2']);
    const downTopnKeys = new Set(['2_0', '1_1', '0_2']);

    for (let i: number = 0; i < moves.length; ++i) {
        const char: string = (i & 1) === 0 ? 'A' : 'B';
        const [r, c] = moves[i];

        if (rows[r].length === 0 || rows[r].at(-1) === char) {
            rows[r].push(char);
            if (rows[r].length === 3) {
                return char;
            }
        }

        if (colls[c].length === 0 || colls[c].at(-1) === char) {
            colls[c].push(char);
            if (colls[c].length === 3) {
                return char;
            }
        }

        const key = moves[i].join('_');
        if (topDownKeys.has(key) && (topDown.length === 0 || topDown.at(-1) === char)) {
            topDown.push(char);
            if (topDown.length === 3) {
                return char;
            }
        }

        if (downTopnKeys.has(key) && (downTop.length === 0 || downTop.at(-1) === char)) {
            downTop.push(char);
            if (downTop.length === 3) {
                return char;
            }
        }
    }


    return moves.length === 9 ? 'Draw' : 'Pending';
};

const test = () => {
    const params = [
        {
            input: {
                moves: [[2,2],[1,2],[2,1],[1,1],[2,0]],
            },
            output: 'A',
        },
        {
            input: {
                moves: [[0,0],[2,0],[1,1],[2,1],[2,2]],
            },
            output: 'A',
        },
        {
            input: {
                moves: [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]],
            },
            output: 'B',
        },
        {
            input: {
                moves: [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]],
            },
            output: 'Draw',
        },
    ];

    params.forEach(({input, output}) => {
        const { moves } = input;
        const result = tictactoe(moves);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();