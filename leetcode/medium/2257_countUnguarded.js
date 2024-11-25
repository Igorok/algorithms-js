/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} guards
 * @param {number[][]} walls
 * @return {number}
 */
var countUnguarded = function(m, n, guards, walls) {
    let unguarded = n * m - walls.length - guards.length;

    const field = new Array(m).fill(0).map(() => new Array(n).fill(0));

    for (const [i, j] of walls) {
        field[i][j] = 1;
    }

    for (const [y, x] of guards) {
        field[y][x] = 2;
    }

    for (const [y, x] of guards) {
        // move right
        for (let i = x + 1; i < n; ++i) {
            if ([1,2].includes(field[y][i])) break;
            if (field[y][i] == 0) {
                field[y][i] = 3;
                unguarded -= 1;
            }
        }
        // move left
        for (let i = x - 1; i > -1; --i) {
            if ([1,2].includes(field[y][i])) break;
            if (field[y][i] == 0) {
                field[y][i] = 3;
                unguarded -= 1;
            }
        }
        // move top
        for (let i = y - 1; i > -1; --i) {
            if ([1,2].includes(field[i][x])) break;
            if (field[i][x] == 0) {
                field[i][x] = 3;
                unguarded -= 1;
            }
        }
        // move bottom
        for (let i = y + 1; i < m; ++i) {
            if ([1,2].includes(field[i][x])) break;
            if (field[i][x] == 0) {
                field[i][x] = 3;
                unguarded -= 1;
            }
        }
    }

    console.log('field', JSON.stringify(field));

    return unguarded;
};

/*

m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]

g w 0 0 0 0
0 g 0 0 w 0
0 0 w g 0 0
0 0 0 0 0 0
0 0 0 0 0 0


[
    [2,1,0,0,0,0],
    [2,2,2,2,1,0],
    [2,2,1,2,2,2],
    [2,2,0,2,0,0]
]

 [2,7,[[1,5],[1,1],[1,6],[0,2]],    [[0,6],[0,3],[0,5]]]


[
    [3,3,2,1,0,1,1],
    [3,2,3,3,3,2,2]
]

*/

const test = () => {
    const params = [
        {
            input: [4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]]],
            output: 7,
        },
        {
            input: [3, 3, [[1,1]], [[0,1],[1,0],[2,1],[1,2]]],
            output: 4,
        },
        {
            input: [2, 7, [[1,5],[1,1],[1,6],[0,2]], [[0,6],[0,3],[0,5]]],
            output: 1,
        },
    ];

    for (const { input, output } of params) {
        const result = countUnguarded(...input);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${output}
            RESULT: ${result}
            `;

        if (JSON.stringify(result) === JSON.stringify(output)) {
            console.log(
                'SUCCESS: \n', message,
            );
        } else {
            console.error('ERROR: \n', message);
        }
    }
};

test();
