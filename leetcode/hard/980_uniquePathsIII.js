/**
 * @param {number[][]} grid
 * @return {number}
 */
var uniquePathsIII = function(grid) {
    let start = undefined;
    let end = undefined;
    let count = 0;
    let res = 0;

    for (let i = 0; i < grid.length; ++i) {
        for (let j = 0; j < grid[0].length; ++j) {
            if (grid[i][j] === 0) {
                count += 1;
                continue;
            }
            if (grid[i][j] === 1) {
                count += 1;
                start = [i, j];
                continue;
            }
            if (grid[i][j] === 2) {
                count += 1;
                end = [i, j];
                continue;
            }
        }
    }

    const path = [];


    const dfs = (i, j, visited) => {
        const key = [i, j].join();
        if (
            i < 0 || j < 0 || i === grid.length || j === grid[0].length ||
            grid[i][j] === -1 || visited.has(key)
        ) {
            return;
        }
        visited.add(key);

        if (i === end[0] && j === end[1]) {
            if (visited.size === count) {
                res += 1;

                path.push(Array.from(visited));
            }
            return;
        }

        const arr = Array.from(visited);

        dfs(i-1, j, new Set(arr));
        dfs(i+1, j, new Set(arr));
        dfs(i, j-1, new Set(arr));
        dfs(i, j+1, new Set(arr));

    };

    dfs(start[0], start[1], new Set());


    console.log(JSON.stringify(path));

    return res;
};

/*
[
    [1,0,0,0],
    [0,0,0,0],
    [0,0,2,-1]
]


[
["0,0","1,0","2,0","2,1","1,1","0,1","0,2","1,2","2,2"],
["0,0","1,0","1,1","0,1","0,2","0,3","1,3","1,2","2,2"],
["0,0","0,1","0,2","1,2","1,1","1,0","2,0","2,1","2,2"],
["0,0","0,1","0,2","0,3","1,3","1,2","1,1","2,1","2,2"]
]


*/


const test = () => {
    const params = [
        {
            input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]],
            output: 2,
        },
        {
            input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]],
            output: 4,
        },
        {
            input: [[0,1],[2,0]],
            output: 0,
        },
    ];

    for (const { input, output } of params) {
        const result = uniquePathsIII(input);
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
