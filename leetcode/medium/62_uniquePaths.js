/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths_1 = function(m, n) {
    let res = 0;

    const dfs = (y, x) => {
        if (y === m || x === n) return;
        if (y === m - 1 && x === n - 1) {
            res += 1;
            return;
        }

        dfs(y + 1, x);
        dfs(y, x + 1);
    };

    dfs(0, 0);

    return res;
};

/*

0 0
0 0
0 0

1 0
1 0
1 1

1 0
1 1
0 1

1 1
0 1
0 1

-

0 0
0 0
0 0


1 1
1 2
1 3


*/

var uniquePaths = function(m, n) {
    const visited = new Array(m).fill(0).map(() => new Array(n).fill(1));

    for (let i = 1; i < m; ++i) {
        for (let j = 1; j < n; ++j) {
            const top = visited[i-1][j];
            const left = visited[i][j - 1];
            visited[i][j] = top + left;
        }
    }

    return visited[m-1][n-1];
};

const test = () => {
    const params = [
        {
            input: [3,7],
            output: 28,
        },
        {
            input: [3,2],
            output: 3,
        },
        {
            input: [23,12],
            output: 193536720,
        },
    ];

    for (const { input, output } of params) {
        const result = uniquePaths(...input);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${output}
            RESULT: ${result}
            `;

        if (result === output) {
            console.log(
                'SUCCESS: \n', message,
            );
        } else {
            console.error('ERROR: \n', message);
        }
    }
};

test();
