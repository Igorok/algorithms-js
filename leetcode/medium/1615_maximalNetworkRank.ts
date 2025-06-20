function maximalNetworkRank(n: number, roads: number[][]): number {
    const adj: Set<number>[] = new Array(n).fill(0).map(() => new Set());
    for (const [s, e] of roads) {
        adj[s].add(e);
        adj[e].add(s);
    }

    let res: number = 0;

    for (let i: number = 0; i < n; ++i) {
        for (let j: number = i + 1; j < n; ++j) {
            if (adj[i].has(j)) {
                res = Math.max(res, adj[i].size + adj[j].size - 1);
            } else {
                res = Math.max(res, adj[i].size + adj[j].size);
            }
        }
    }

    return res;
};


const test = () => {
    const params = [
        {
            input: {
                n: 4, roads: [[0,1],[0,3],[1,2],[1,3]],
            },
            output: 4,
        },
        {
            input: {
                n: 5, roads: [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]],
            },
            output: 5,
        },
        {
            input: {
                n: 8, roads: [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]],
            },
            output: 5,
        },
    ];

    params.forEach(({input, output}) => {
        const { n, roads } = input;
        const result = maximalNetworkRank(n, roads);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();