/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku_0 = function(board) {
    const rows = new Array(9).fill(0).map(() => new Set());
    const colls = new Array(9).fill(0).map(() => new Set());

    for (let i = 0; i < board.length; ++i) {
        for (let j = 0; j < board[0].length; ++j) {
            if (board[i][j] !== '.') {
                rows[i].add(board[i][j]);
                colls[j].add(board[i][j]);
            }
        }
    }

    const getSquare = (y, x) => {
        while ((y % 3) !== 0) y -= 1;
        while ((x % 3) !== 0) x -= 1;
        const square = new Set();

        for (let i = y; i < y + 3; ++i) {
            for (let j = x; j < x + 3; ++j) {
                if (board[i][j] !== '.') {
                    square.add(board[i][j]);
                }
            }
        }

        return square;
    };



    const rec = (y, x) => {
        const nextStep = (y , x) => {
            if (y === 8 && x  === 8) {
                return true;
            }
            if (x == 8) {
                return rec(y + 1, 0);
            }
            return rec(y, x + 1);
        }

        if (board[y][x] !== '.') {
            return nextStep(y, x);
        }

        for (let i = 1; i < 10; ++i) {
            const square = getSquare(y, x);
            const num = String(i);

            if (!square.has(num) && !rows[y].has(num) && !colls[x].has(num)) {
                board[y][x] = num;
                rows[y].add(num);
                colls[x].add(num);

                const res = nextStep(y, x);
                if (res) {
                    return true;
                }

                rows[y].delete(num);
                colls[x].delete(num);
                board[y][x] = '.';
            }
        }

        return false;
    };

    rec(0, 0);

    return board;
};

var solveSudoku_1 = function(board) {
    const rows = new Array(9).fill(0).map(() => new Set());
    const colls = new Array(9).fill(0).map(() => new Set());
    const squares = ['0_0', '0_3', '0_6', '3_0', '3_3', '3_6', '6_0', '6_3', '6_6',].reduce((acc, val) => {
        acc[val] = new Set();
        return acc;
    }, {});

    const getSquare = (y, x) => {
        while ((y % 3) !== 0) y -= 1;
        while ((x % 3) !== 0) x -= 1;
        const key = [y, x].join('_');
        return squares[key];
    };

    for (let i = 0; i < board.length; ++i) {
        for (let j = 0; j < board[0].length; ++j) {
            if (board[i][j] !== '.') {
                rows[i].add(board[i][j]);
                colls[j].add(board[i][j]);
                const square = getSquare(i, j);
                square.add(board[i][j]);
            }
        }
    }

    const rec = (y, x) => {
        const nextStep = (y , x) => {
            if (y === 8 && x  === 8) {
                return true;
            }
            if (x == 8) {
                return rec(y + 1, 0);
            }
            return rec(y, x + 1);
        }

        if (board[y][x] !== '.') {
            return nextStep(y, x);
        }

        const square = getSquare(y, x);
        for (let i = 1; i < 10; ++i) {
            const num = String(i);

            if (!square.has(num) && !rows[y].has(num) && !colls[x].has(num)) {
                board[y][x] = num;
                rows[y].add(num);
                colls[x].add(num);
                square.add(num);

                const res = nextStep(y, x);
                if (res) {
                    return true;
                }

                square.delete(num);
                rows[y].delete(num);
                colls[x].delete(num);
                board[y][x] = '.';
            }
        }

        return false;
    };

    rec(0, 0);

    return board;
};

var solveSudoku = function(board) {
    const rows = new Array(9).fill(0).map(() => new Array(10).fill(0));
    const colls = new Array(9).fill(0).map(() => new Array(10).fill(0));
    const squares = new Array(3).fill(0)
        .map(() => new Array(3).fill(0).map(() => new Array(10).fill(0)));

    const getSquare = (y, x) => {
        const i = Math.floor(y / 3);
        const j = Math.floor(x / 3);
        return squares[i][j];
    };

    for (let i = 0; i < board.length; ++i) {
        for (let j = 0; j < board[0].length; ++j) {
            if (board[i][j] !== '.') {
                const num = board[i][j];
                rows[i][num] = 1;
                colls[j][num] = 1;
                const square = getSquare(i, j);
                square[num] = 1;
            }
        }
    }

    const rec = (y, x) => {
        const nextStep = (y , x) => {
            if (y === 8 && x  === 8) {
                return true;
            }
            if (x == 8) {
                return rec(y + 1, 0);
            }
            return rec(y, x + 1);
        }

        if (board[y][x] !== '.') {
            return nextStep(y, x);
        }

        const square = getSquare(y, x);
        for (let i = 1; i < 10; ++i) {
            const num = String(i);

            if (!square[num] && !rows[y][num] && !colls[x][num]) {
                board[y][x] = num;
                rows[y][num] = 1;
                colls[x][num] = 1;
                square[num] = 1;

                const res = nextStep(y, x);
                if (res) {
                    return true;
                }

                square[num] = 0;
                rows[y][num] = 0;
                colls[x][num] = 0;
                board[y][x] = '.';
            }
        }

        return false;
    };

    rec(0, 0);

    return board;
};


/*


[
["5","1","9","7","4","8","6","3","2"],
["7","8","3","6","5","2","4","1","9"],
["4","2","6","1","3","9","8","7","5"],
["3","5","7","9","8","6","2","4","1"],
["2","6","4","3","1","7","5","9","8"],
["1","9","8","5","2","4","3","6","7"],
["9","7","5","8","6","3","1","2","4"],
["8","3","2","4","9","1","7","5","6"],
["6","4","1","2","7","5","9","8","3"]
] result



[
["3","1","9","7","4","8","6","5","2"],
["7","4","3","6","5","2","1","8","9"],
["6","2","5","1","3","9","8","7","4"],
["5","3","7","9","8","6","2","4","1"],
["2","6","4","3","1","7","5","9","8"],
["1","9","8","5","2","4","3","6","7"],
["9","7","1","8","6","3","4","2","5"],
["8","5","2","4","9","1","7","3","6"],
["4","8","6","2","7","5","9","1","3"]
]

*/

var test = function () {
    var params = [
        {
            input: [
                ["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"],
            ],
            output: [
                ["5","3","4","6","7","8","9","1","2"],
                ["6","7","2","1","9","5","3","4","8"],
                ["1","9","8","3","4","2","5","6","7"],
                ["8","5","9","7","6","1","4","2","3"],
                ["4","2","6","8","5","3","7","9","1"],
                ["7","1","3","9","2","4","8","5","6"],
                ["9","6","1","5","3","7","2","8","4"],
                ["2","8","7","4","1","9","6","3","5"],
                ["3","4","5","2","8","6","1","7","9"],
            ],
        },
        {
            input: [
                [".",".","9","7","4","8",".",".","."],
                ["7",".",".",".",".",".",".",".","."],
                [".","2",".","1",".","9",".",".","."],
                [".",".","7",".",".",".","2","4","."],
                [".","6","4",".","1",".","5","9","."],
                [".","9","8",".",".",".","3",".","."],
                [".",".",".","8",".","3",".","2","."],
                [".",".",".",".",".",".",".",".","6"],
                [".",".",".","2","7","5","9",".","."]
            ],
            output: [
                ["5","1","9","7","4","8","6","3","2"],
                ["7","8","3","6","5","2","4","1","9"],
                ["4","2","6","1","3","9","8","7","5"],
                ["3","5","7","9","8","6","2","4","1"],
                ["2","6","4","3","1","7","5","9","8"],
                ["1","9","8","5","2","4","3","6","7"],
                ["9","7","5","8","6","3","1","2","4"],
                ["8","3","2","4","9","1","7","5","6"],
                ["6","4","1","2","7","5","9","8","3"]
            ],
        },
    ];

    params.forEach(({input, output}) => {
        const result = solveSudoku(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};
test();
