/**
 * @param {number[][]} isWater
 * @return {number[][]}
 */
var highestPeak = function(isWater) {
    const res = new Array(isWater.length).fill(0).map(() => new Array(isWater[0].length).fill(-1));
    const offset = [[1, 0], [-1, 0], [0 , 1], [0, -1]];
    const queue = [];

    for (let i = 0; i < isWater.length; ++i) {
        for (let j = 0; j < isWater[0].length; ++j) {
            if (isWater[i][j] === 1) {
                res[i][j] = 0;
                queue.push([i, j, 0]);
            }
        }
    }

    while (queue.length) {
        const [i, j, val] = queue.shift();

        for (const [addY, addX] of offset) {
            const y = i + addY;
            const x = j + addX;

            if (y < 0 || x < 0 || y === res.length || x === res[0].length || res[y][x] !== -1) {
                continue;
            }

            res[y][x] = val + 1;
            queue.push([y, x, val + 1]);
        }
    }

    return res;
};

/*

[0,0,1],
[1,0,0],
[0,0,0]


[1,1,0],
[0,1,1],
[1,2,2]

1 1 0
0 1 1
1 1 2
1 0 1

*/

const test = () => {
    const params = [
        {
            input: [[0,1],[0,0]],
            output: [[1,0],[2,1]],
        },
        {
            input: [[0,0,1],[1,0,0],[0,0,0]],
            output: [[1,1,0],[0,1,1],[1,2,2]],
        },
    ];

    for (const { input, output } of params) {
        const result = highestPeak(input);
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
