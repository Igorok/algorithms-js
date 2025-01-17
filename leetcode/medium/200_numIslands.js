/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    const visited = new Array(grid.length).fill(0).map(() => new Array(grid[0].length).fill(0));
    const dfs = (i, j) => {
        if (i < 0 || j < 0 || i === grid.length || j === grid[0].length || grid[i][j] === '0' || visited[i][j] === 1) {
            return;
        }

        visited[i][j] = 1;

        dfs(i + 1, j);
        dfs(i - 1, j);
        dfs(i, j + 1);
        dfs(i, j - 1);
    }

    let res = 0;

    for (let i = 0; i < grid.length; ++i) {
        for (let j = 0; j < grid[0].length; ++j) {
            if (grid[i][j] === '0' || visited[i][j] === 1) {
                continue;
            }
            res += 1;
            dfs(i, j);
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ],
            output: 1,
        },
        {
            input: [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ],
            output: 3,
        },
    ];

    for (const { input, output } of params) {
        const result = numIslands(input);
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
