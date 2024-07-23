function isValidSudoku(board: string[][]): boolean {
    const rows = new Array(9).fill(null).map(() => new Set());
    const columns = new Array(9).fill(null).map(() => new Set());
    const squares = [
        new Array(3).fill(null).map(() => new Set()),
        new Array(3).fill(null).map(() => new Set()),
        new Array(3).fill(null).map(() => new Set()),
    ];

    for (let i: number = 0; i < 9; ++i) {
        for (let j: number = 0; j < 9; ++j) {
            if (board[i][j] === '.') continue;

            let square: Set<any> = squares[Math.floor(i/3)][Math.floor(j/3)];

            if (
                rows[i].has(board[i][j])
                || columns[j].has(board[i][j])
                || square.has(board[i][j])
            ) {
                return false;
            }
            rows[i].add(board[i][j]);
            columns[j].add(board[i][j]);
            square.add(board[i][j]);
        }
    }

    return true;
}




const test = () => {
    const params = [
        {
            input: [["5","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."]
                    ,[".","9","8",".",".",".",".","6","."]
                    ,["8",".",".",".","6",".",".",".","3"]
                    ,["4",".",".","8",".","3",".",".","1"]
                    ,["7",".",".",".","2",".",".",".","6"]
                    ,[".","6",".",".",".",".","2","8","."]
                    ,[".",".",".","4","1","9",".",".","5"]
                    ,[".",".",".",".","8",".",".","7","9"]],
            output: true,
        },
        {
            input: [["8","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."]
                    ,[".","9","8",".",".",".",".","6","."]
                    ,["8",".",".",".","6",".",".",".","3"]
                    ,["4",".",".","8",".","3",".",".","1"]
                    ,["7",".",".",".","2",".",".",".","6"]
                    ,[".","6",".",".",".",".","2","8","."]
                    ,[".",".",".","4","1","9",".",".","5"]
                    ,[".",".",".",".","8",".",".","7","9"]],
            output: false,
        }
    ];

    params.forEach(({input, output}) => {
        const result = isValidSudoku(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );

    });
};

test();
