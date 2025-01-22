/**
 * @param {number[][]} grid
 * @return {number}
 */
var gridGame_0 = function(grid) {
    const length = grid[0].length;

    let post0 = new Array(length).fill(0);
    let post1 = new Array(length).fill(0);
    post0[length - 1] = grid[0][length - 1];
    post1[length - 1] = grid[1][length - 1];

    for (let i = length - 2; i > -1; --i) {
        post0[i] = grid[0][i] + post0[i + 1];
        post1[i] = grid[1][i] + post1[i + 1];
    }

    let pivot = 0
    for (let i = 0; i < length; ++i) {
        if (i + 1 === length || post1[i] > post0[i + 1]) {
            pivot = i;
            break;
        }
    }

    const rightSum = pivot + 1 === length ? 0 : post0[pivot + 1];
    const leftSum = pivot === 0 ? 0 : post1[0] - post1[pivot];

    return Math.max(rightSum, leftSum);
};

var gridGame = function(grid) {
    const length = grid[0].length;

    let post = new Array(length).fill(0);
    post[length - 1] = grid[0][length - 1];
    for (let i = length - 2; i > -1; --i) {
        post[i] = grid[0][i] + post[i + 1];
    }

    let rightSum = 0;
    let res = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i < length; ++i) {
        const right = (i + 1 === length) ? 0 : post[i + 1];
        const maxRemainder = Math.max(right, rightSum);
        rightSum += grid[1][i];
        res = Math.min(res, maxRemainder);
    }

    return res;
};

/*
7

[20,3,20,17,2,12,15,17,4,15],
[20,10,13,14,15,5,2,3,14,3]

[125,105,102,82,65,63,51,36,19,15,]
[99, 79, 69, 56,42,27,22,20,17,3,]


99+79+69+56+42+27+22+20+14

*/

const test = () => {
    const params = [
        {
            input: [[2,5,4],[1,5,1]],
            output: 4,
        },
        {
            input: [[3,3,1],[8,5,2]],
            output: 4,
        },
        {
            input: [[1,3,1,15],[1,3,3,1]],
            output: 7,
        },
        {
            input: [[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]],
            output: 63,
        },
    ];


    for (const { input, output } of params) {
        const result = gridGame(input);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${JSON.stringify(output)}
            RESULT: ${JSON.stringify(result)}`;

        if (JSON.stringify(result) === JSON.stringify(output)) {
            console.log(
                `SUCCESS: ${message}`,
            );
        } else {
            console.error(`ERROR: ${message}`);
        }
    }
};

test();
