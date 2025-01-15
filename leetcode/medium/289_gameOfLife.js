/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var gameOfLife_0 = function(board) {
    const old = JSON.parse(JSON.stringify(board));

    const getCell = (y, x) => {
        const val = old[y][x];
        let count = 0;
        const startY = Math.max(y - 1, 0);
        const endY = Math.min(y + 2, old.length);
        for (let i = startY; i < endY; ++i) {
            const startX = Math.max(x - 1, 0);
            const endX = Math.min(x + 2, old[0].length);
            for (let j = startX; j < endX; ++j) {
                if (i === y && j === x) {
                    continue;
                }
                count += old[i][j];
            }
        }

        if (val === 1) {
            if (count > 1 && count < 4) return 1;
            return 0;
        } else {
            if (count === 3) return 1;
            return 0;
        }
    }

    for (let i = 0; i < board.length; ++i) {
        for (let j = 0; j < board[0].length; ++j) {
            board[i][j] = getCell(i, j);
        }
    }
};

/*
0 - 0 = 0
0 - 1 = 1
1 - 0 = 2
1 - 1 = 3

[0, 0, 1, 1]
*/
var gameOfLife = function(board) {
    const valMap = [0, 0, 1, 1];
    const getCell = (y, x) => {
        const startX = Math.max(x - 1, 0);
        const endX = Math.min(x + 2, board[0].length);
        const endY = Math.min(y + 2, board.length);
        let count = board[y][x] ? -1 : 0;

        if (y - 1 > -1) {
            for (let j = startX; j < endX; ++j) {
                count += valMap[board[y - 1][j]];
            }
        }
        for (let i = y; i < endY; ++i) {
            for (let j = startX; j < endX; ++j) {
                if (i === y && j === x - 1) {
                    count += valMap[board[i][j]];
                } else {
                    count += board[i][j]
                }
            }
        }

        if (board[y][x] === 1) {
            if (count > 1 && count < 4) return 3;
            return 2;
        } else {
            if (count === 3) return 1;
            return 0;
        }
    }

    for (let i = 0; i < board.length; ++i) {
        for (let j = 0; j < board[0].length; ++j) {
            board[i][j] = getCell(i, j);
        }
    }

    for (let i = 0; i < board.length; ++i) {
        for (let j = 0; j < board[0].length; ++j) {
            board[i][j] = board[i][j] % 2;
        }
    }
};

const test = () => {
    const params = [
        {
            input: [[0,1,0],[0,0,1],[1,1,1],[0,0,0]],
            output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]],
        },
        {
            input: [[1,1],[1,0]],
            output: [[1,1],[1,1]],
        },
    ];

    for (const { input, output } of params) {
        const param = JSON.parse(JSON.stringify(input));
        gameOfLife(param);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${JSON.stringify(output)}
            RESULT: ${JSON.stringify(param)}
            `;

        if (JSON.stringify(param) === JSON.stringify(output)) {
            console.log(
                'SUCCESS: \n', message,
            );
        } else {
            console.error('ERROR: \n', message);
        }
    }
};

test();
