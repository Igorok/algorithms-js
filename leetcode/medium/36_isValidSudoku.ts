function isValidSudoku(board: string[][]): boolean {
    const rows: Set<string>[] = new Array(9).fill(0).map(() => new Set());
    const cols: Set<string>[] = new Array(9).fill(0).map(() => new Set());
    const squares: Set<string>[] = new Array(9).fill(0).map(() => new Set());

    const getSquareId = (row: number, col: number) => {
        const r: number = Math.floor(row / 3);
        const c: number = Math.floor(col / 3);
        const id: number = r * 3 + c;
        return id;
    };

    for (let row: number = 0; row < board.length; ++row) {
        for (let col: number = 0; col < board[0].length; ++col) {
            if (board[row][col] === '.') {
                continue;
            }

            if (rows[row].has(board[row][col])) {
                return false;
            }
            rows[row].add(board[row][col]);

            if (cols[col].has(board[row][col])) {
                return false;
            }
            cols[col].add(board[row][col]);

            const id: number = getSquareId(row, col);
            if (squares[id].has(board[row][col])) {
                return false;
            }
            squares[id].add(board[row][col]);
        }
    }

    return true;
};

const test = () => {
    const params = [
        {
            input: {
                board:
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
            },
            output: true,
        },
        {
            input: {
                board:
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
            },
            output: false,
        },
    ];

    params.forEach(({input, output}) => {
        const { board } = input;
        const result = isValidSudoku(board);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();