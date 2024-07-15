function isValidSudoku(board) {
    var rows = new Array(9).fill(null).map(function () { return new Set(); });
    var columns = new Array(9).fill(null).map(function () { return new Set(); });
    var squares = [
        new Array(3).fill(null).map(function () { return new Set(); }),
        new Array(3).fill(null).map(function () { return new Set(); }),
        new Array(3).fill(null).map(function () { return new Set(); }),
    ];
    for (var i = 0; i < 9; ++i) {
        for (var j = 0; j < 9; ++j) {
            if (board[i][j] === '.')
                continue;
            var square = squares[Math.floor(i / 3)][Math.floor(j / 3)];
            if (rows[i].has(board[i][j])
                || columns[j].has(board[i][j])
                || square.has(board[i][j])) {
                return false;
            }
            rows[i].add(board[i][j]);
            columns[j].add(board[i][j]);
            square.add(board[i][j]);
        }
    }
    return true;
}
var test = function () {
    var params = [
        {
            input: [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
            output: true,
        },
        {
            input: [["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
            output: false,
        }
    ];
    params.forEach(function (_a) {
        var input = _a.input, output = _a.output;
        var result = isValidSudoku(input);
        console.log(JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ', 'input', JSON.stringify(input), 'output', output, 'result', result);
    });
};
test();
