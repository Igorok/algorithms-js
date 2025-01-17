/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    const path = [];


    let res = 0;

    const queue = [[0, 0, new Set()]];
    while (queue.length) {
        const [ y, x, visited ] = queue.shift();
        const key = [y, x].join('_');
        if (
            y === -1 ||
            x === -1 ||
            y === obstacleGrid.length ||
            x === obstacleGrid[0].length ||
            visited.has(key) ||
            obstacleGrid[y][x] === 1
        ) {
            continue;
        }

        visited.add(key);

        if (y === obstacleGrid.length - 1 && x === obstacleGrid[0].length - 1) {
            res += 1;

            path.push(Array.from(visited));
            continue;
        }

        const arr = Array.from(visited);
        queue.push([y+1, x, new Set(arr)]);
        queue.push([y, x+1, new Set(arr)]);
    }

    return res;
};

var uniquePathsWithObstacles = function(obstacleGrid) {
    if (obstacleGrid[0][0] === 1 || obstacleGrid[obstacleGrid.length - 1][obstacleGrid[0].length - 1] === 1) {
        return 0;
    }
    const memo = new Array(obstacleGrid.length).fill(0).map(() => new Array(obstacleGrid[0].length).fill(0));
    memo[0][0] = 1;


    for (let i = 0; i < obstacleGrid.length; ++i) {
        for (let j = 0; j < obstacleGrid[0].length; ++j) {
            if ((i === 0 && j === 0) || obstacleGrid[i][j] === 1) {
                continue;
            }

            if (i - 1 > -1) {
                memo[i][j] += memo[i-1][j];
            }
            if (j - 1 > -1) {
                memo[i][j] += memo[i][j-1];
            }
        }
    }

    return memo[memo.length - 1][memo[0].length - 1];
};

const test = () => {
    const params = [
        {
            input: [[0,0,0],[0,1,0],[0,0,0]],
            output: 2,
        },
        {
            input: [[0,1],[0,0]],
            output: 1,
        },
        {
            input: [[0,0],[0,1]],
            output: 0,
        },
        {
            input: [[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]],
            output: 7,
        },
    ];

    for (const { input, output } of params) {
        const result = uniquePathsWithObstacles(input);
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
