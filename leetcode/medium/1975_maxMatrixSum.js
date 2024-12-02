/**
 * @param {number[][]} matrix
 * @return {number}
 */
var maxMatrixSum_1 = function(matrix) {
    const l = matrix.length;

    const multiply = (i, j) => {
        const locs = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        const visited = new Set();

        const dfs = (i, j) => {
            visited.add(`${i}_${j}`);

            const val = matrix[i][j];
            let nei = undefined;
            for (const loc of locs) {
                const y = i + loc[0];
                const x = j + loc[1];

                if (visited.has(`${y}_${x}`) || y < 0 || y === l || x < 0 || x === l) continue;

                if (matrix[y][x] < 0 || Math.abs(val) >= matrix[y][x]) {
                    if (!nei || matrix[y][x] < matrix[nei[0]][nei[1]]) {
                        nei = [y, x, matrix[y][x]];
                    }
                }
            }

            if (nei) {
                matrix[i][j] = -matrix[i][j];
                matrix[nei[0]][nei[1]] = -matrix[nei[0]][nei[1]];
                if (matrix[nei[0]][nei[1]] < 0)
                    dfs(nei[0], nei[1]);
            }
        };

        dfs(i, j);
    };

    for (let i = 0; i < l; ++i) {
        for (let j = 0; j < l; ++j) {
            if (matrix[i][j] < 0) multiply(i, j);
        }
    }

    console.log(JSON.stringify(matrix));

    let res = 0;
    for (let i = 0; i < l; ++i) {
        for (let j = 0; j < l; ++j) {
            res += matrix[i][j];
        }
    }

    return res;
};

var maxMatrixSum = function(matrix) {
    let negativeCount = 0;
    let minMod = 10e6;
    let sum = 0;

    for (let i = 0; i < matrix.length; ++i) {
        for (let j = 0; j < matrix.length; ++j) {
            sum += Math.abs(matrix[i][j]);
            if (matrix[i][j] < 0) {
                negativeCount += 1;
            }
            minMod = Math.min(minMod, Math.abs(matrix[i][j]));
        }
    }

    if ((negativeCount % 2) === 0 || minMod === 0) {
        return sum;
    }

    return sum - 2 * minMod;
};


/*

[ -9,  9,  9, -9]
[-10, 10,  7,  5]
[  4, -8, -9,  6]
[ 10,  2, -6,  1]

[  9,  9,  9, -9]
[ 10, 10,  7,  5]
[  4, -8, -9,  6]
[ 10,  2, -6,  1]

[  9,  9,  9,  9]
[ 10, 10,  7, -5]
[  4, -8, -9,  6]
[ 10,  2, -6,  1]

[  9,  9,  9,  9]
[ 10, 10,  7, -5]
[  4,  8,  9,  6]
[ 10,  2, -6,  1]

[  9,  9,  9,  9]
[ 10, 10,  7, -5]
[  4,  8,  9,  6]
[ 10,  2,  6, -1]


*/



const test = () => {
    const params = [
        {
            input: [[1,-1],[-1,1]],
            output: 4,
        },
        {
            input: [[1,2,3],[-1,-2,-3],[1,2,3]],
            output: 16,
        },
        {
            input: [[-1,0,-1],[-2,1,3],[3,2,2]],
            output: 15,
        },
        {
            input: [[1,0,-1],[-2,1,3],[3,2,2]],
            output: 15,
        },
        {
            input: [[-9,9,9,-9],[-10,10,7,5],[4,-8,-9,6],[10,2,-6,1]],
            output: 114,
        },


    ];

    params.forEach(({input, output}) => {
        const result = maxMatrixSum(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();