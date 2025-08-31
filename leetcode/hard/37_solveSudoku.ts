/**
 Do not return anything, modify board in-place instead.
 */
function solveSudoku(board: string[][]): void {
    const n: number = board.length;
    const rows: number[][] = new Array(9).fill(0).map(() => new Array(10).fill(0));
    const cols: number[][] = new Array(9).fill(0).map(() => new Array(10).fill(0));
    const squares: number[][] = new Array(9).fill(0).map(() => new Array(10).fill(0));

    const getSquareId = (row: number, col: number): number => {
        const r: number = Math.floor(row / 3);
        const c: number = Math.floor(col / 3);
        return r * 3 + c;
    };

    const getNext = (row: number, col: number): number[] => {
        if (col + 1 < 9) {
            return [row, col + 1];
        }
        return [row + 1, 0]
    }

    for (let row: number = 0; row < n; ++row) {
        for (let col: number = 0; col < n; ++col) {
            if (board[row][col] === '.') {
                continue;
            }
            const num: number = Number(board[row][col]);
            rows[row][num] = 1;
            cols[col][num] = 1;
            squares[getSquareId(row, col)][num] = 1;
        }
    }

    const rec = (row: number, col: number): boolean => {
        if (row === n) {
            return true;
        }

        const nextLoc: number[] = getNext(row, col);

        if (board[row][col] !== '.') {
            return rec(nextLoc[0], nextLoc[1]);
        }

        const sqr = squares[getSquareId(row, col)];

        for (let i: number = 1; i <= 9; ++i) {
            if (rows[row][i] || cols[col][i] || sqr[i]) {
                continue;
            }

            rows[row][i] = 1;
            cols[col][i] = 1;
            sqr[i] = 1;
            board[row][col] = String(i);

            if (rec(nextLoc[0], nextLoc[1])) {
                return true;
            }

            rows[row][i] = 0;
            cols[col][i] = 0;
            sqr[i] = 0;
            board[row][col] = '.';
        }

        return false;
    }

    rec(0, 0);
};

const test = () => {
    const params = [
        {
            input: {
                board: [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
            },
            output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]],
        },
    ];

    params.forEach(({input, output}) => {
        const { board } = input;

        solveSudoku(board);

        console.log(
            JSON.stringify(input) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
        );
    });
};

test();
