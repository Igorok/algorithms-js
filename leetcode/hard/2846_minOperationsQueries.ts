function minOperationsQueries(n: number, edges: number[][], queries: number[][]): number[] {
    const adj: number[][][] = new Array(n).fill(0).map(() => []);

    for (const [s, e, w] of edges) {
        adj[s].push([e, w]);
        adj[e].push([s, w]);
    }

    const maxLog: number = Math.ceil(Math.log2(n));
    const parentsByBin = new Array(n).fill(0).map(() => new Array(maxLog+1).fill(0));
    const deeps: number[] = new Array(n).fill(0);
    const weights: number[][] = new Array(n).fill(0).map(() => new Array(27).fill(0));

    const dfs = (node: number, parent: number, deep: number) => {
        deeps[node] = deep;

        parentsByBin[node][0] = parent;
        for (let i: number = 1; i <= maxLog; ++i) {
            parentsByBin[node][i] = parentsByBin[parentsByBin[node][i-1]][i-1];
        }

        for (const [nei, w] of adj[node]) {
            if (nei === parent) continue;

            for (let i: number = 0; i < weights[node].length; ++i) {
                weights[nei][i] += weights[node][i];
            }
            weights[nei][w] += 1;
            dfs(nei, node, deep+1);
        }
    };
    dfs(0, 0, 0);

    const getLCA = (start: number, end: number) => {
        let [s, e] = deeps[start] < deeps[end] ? [end, start] : [start, end];

        const diff: number = deeps[s] - deeps[e];
        if (diff > 0) {
            for (let i: number = 0; i <= maxLog; ++i) {
                if ((1 << i) & diff) {
                    s = parentsByBin[s][i];
                }
            }
        }

        if (s === e) {
            return s;
        }

        for (let i: number = maxLog; i > -1; --i) {
            if (parentsByBin[s][i] !== parentsByBin[e][i]) {
                s = parentsByBin[s][i];
                e = parentsByBin[e][i];
            } else {}
        }

        return parentsByBin[s][0];
    }

    const res: number[] = [];

    for (const [start, end] of queries) {
        const lca: number = getLCA(start, end);

        let total: number = 0;
        let freq: number = 0;

        for (let i: number = 0; i < 27; ++i) {
            const count: number = weights[start][i] + weights[end][i] - 2*weights[lca][i];
            total += count;
            freq = Math.max(freq, count);
        }

        res.push(total - freq);
    }

    return res;
};

/*

 0
 1
 2
 3
 4
5 6
7 8
9 10

const l = Math.ceil(Math.log2(11)) = 4;


0   [0,0,0,0]
1   [0,0,0,0]
2   [1,0,0,0]
3   [2,1,0,0]
4   [3,2,0,0]
5   [4,3,1,0]
6   [4,3,1,0]
7   [5,4,2,0]
8   [6,4,2,0]
9   [7,5,3,0]
10  [8,6,3,0]

7,10
7,8

*/



const test = () => {
    const params = [
        {
            input: {
                n: 8, edges: [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]], queries: [[4,6],[0,4],[6,5],[7,4]]
            },
            output: [1,2,2,3],
        },
        {
            input: {
                n: 7, edges: [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], queries: [[0,3],[3,6],[2,6],[0,6]]
            },
            output: [0,0,1,3],
        },

    ];

    params.forEach(({input, output}) => {
        const { n, edges, queries } = input;

        const result = minOperationsQueries(n, edges, queries);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();