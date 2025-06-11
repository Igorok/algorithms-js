function pacificAtlantic(heights: number[][]): number[][] {
    const shifts: number[][] = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    const n: number = heights.length;
    const m: number = heights[0].length;

    const visitedP: number[][] = new Array(n).fill(0).map(() => new Array(m).fill(0));
    const visitedA: number[][] = new Array(n).fill(0).map(() => new Array(m).fill(0));

    const dfs = (row: number, coll: number, visited: number[][]): void => {
        for (const [sR, sC] of shifts) {
            const newRow: number = row + sR;
            const newColl: number = coll + sC;

            if (newRow === -1 || newRow === n || newColl === -1 || newColl === m || visited[newRow][newColl] === 1) {
                continue;
            }

            if (heights[row][coll] > heights[newRow][newColl]) {
                continue;
            }

            visited[newRow][newColl] = 1;
            dfs(newRow, newColl, visited);
        }
    }

    for (let i: number = 0; i < n; ++i) {
        if (visitedP[i][0] === 0) {
            visitedP[i][0] = 1;
            dfs(i, 0, visitedP);
        }
        if (visitedA[i][m-1] === 0) {
            visitedA[i][m-1] = 1;
            dfs(i, m-1, visitedA);
        }
    }

    for (let i: number = 0; i < m; ++i) {
        if (visitedP[0][i] === 0) {
            visitedP[0][i] = 1;
            dfs(0, i, visitedP);
        }
        if (visitedA[n-1][i] === 0) {
            visitedA[n-1][i] = 1;
            dfs(n-1, i, visitedA);
        }
    }

    const res: number[][] = [];
    for (let i: number = 0; i < n; ++i) {
        for (let j: number = 0; j < m; ++j) {
            if (visitedA[i][j] === 1 && visitedP[i][j] === 1) {
                res.push([i, j]);
            }
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]],
            output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]],
        },
        {
            input: [[1]],
            output: [[0,0]],
        },
    ];

    params.forEach(({input, output}) => {
        const result = pacificAtlantic(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

