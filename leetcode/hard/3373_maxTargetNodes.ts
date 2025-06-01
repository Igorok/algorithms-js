function maxTargetNodes_0(edges1: number[][], edges2: number[][]): number[] {
    const adj1: number[][] = new Array(edges1.length + 1).fill(0).map(() => []);
    const adj2: number[][] = new Array(edges2.length + 1).fill(0).map(() => []);

    for (const [s, e] of edges1) {
        adj1[s].push(e);
        adj1[e].push(s);
    }
    for (const [s, e] of edges2) {
        adj2[s].push(e);
        adj2[e].push(s);
    }

    const getCount = (adj: number[][], id: number, memo: number[][], visited: number[]): number[] => {
        const res: number[] = [1, 0];

        visited[id] = 1;

        // const calculated: number[] = [];

        for (const nei of adj[id]) {
            if (visited[nei] === 1) {
                continue;
            }
            // if (visited[nei] === 2) {
            //     calculated.push(nei);
            //     continue;
            // }
            const [even, odd] = getCount(adj, nei, memo, visited);
            res[0] += odd;
            res[1] += even;
        }

        // for (const nei of calculated) {
        //     res[0] += memo[nei][1] - res[0];
        //     res[1] += memo[nei][0] - res[1];
        // }

        return res;
    };

    const memo2: number[][] = new Array(edges2.length + 1).fill(0).map(() => [1, 0]);
    const visited2: number[] = new Array(edges2.length + 1).fill(0);

    let maxOdd: number = 0;
    for (let i: number = 0; i < adj2.length; ++i) {
        const [even, odd] = getCount(adj2, i, memo2, new Array(edges2.length + 1).fill(0));
        memo2[i] = [even, odd];
        maxOdd = Math.max(maxOdd, odd);
        visited2[i] = 2;
    }

    const res: number[] = [];

    const memo1: number[][] = new Array(edges1.length + 1).fill(0).map(() => [1, 0]);
    const visited1: number[] = new Array(edges1.length + 1).fill(0);

    for (let i: number = 0; i < adj1.length; ++i) {
        const [even, odd] = getCount(adj1, i, memo1, new Array(edges1.length + 1).fill(0));
        memo1[i] = [even, odd];
        res.push(even + maxOdd);
        visited1[i] = 2;
    }

    return res;
};

function maxTargetNodes(edges1: number[][], edges2: number[][]): number[] {
    const adj1: number[][] = new Array(edges1.length + 1).fill(0).map(() => []);
    const adj2: number[][] = new Array(edges2.length + 1).fill(0).map(() => []);

    for (const [s, e] of edges1) {
        adj1[s].push(e);
        adj1[e].push(s);
    }
    for (const [s, e] of edges2) {
        adj2[s].push(e);
        adj2[e].push(s);
    }


    const level2: number[] = new Array(edges2.length + 1).fill(-1);
    const level1: number[] = new Array(edges1.length + 1).fill(-1);

    const dfs = (id: number, adj: number[][], level: number, parent: number, levels: number[]) => {
        const res: number[] = [0, 0];
        levels[id] = (level % 2);
        res[(level % 2)] += 1;

        for (const nei of adj[id]) {
            if (nei === parent) {
                continue;
            }
            const [even, odd] = dfs(nei, adj, level + 1, id, levels);
            res[0] += even;
            res[1] += odd;
        }

        return res;
    };

    const res2 = dfs(0, adj2, 0, 0, level2);
    const maxVal = Math.max(...res2);

    const [even, odd] = dfs(0, adj1, 0, 0, level1);

    const res: number[] = [];
    for (let i: number = 0; i < level1.length; ++i) {
        res.push(
            level1[i] === 0 ? even + maxVal : odd + maxVal
        );
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                edges1: [[2,1],[7,3],[0,4],[7,5],[2,6],[0,2],[0,7]],
                edges2: [[3,0],[1,2],[5,1],[6,3],[9,4],[5,6],[7,5],[9,7],[8,9]],
            },
            output: [11,11,9,11,9,11,11,9],
        },

        {
            input: {
                edges1: [[0,1],[0,2],[2,3],[2,4]], edges2: [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]],
            },
            output: [8,7,7,8,8],
        },
        {
            input: {
                edges1: [[0,1],[0,2],[0,3],[0,4]], edges2: [[0,1],[1,2],[2,3]],
            },
            output: [3,6,6,6,6],
        },
    ];

    params.forEach(({input, output}) => {
        const { edges1, edges2 } = input;
        const result = maxTargetNodes(edges1, edges2);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();