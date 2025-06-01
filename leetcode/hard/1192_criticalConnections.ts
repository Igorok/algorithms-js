function criticalConnections(n: number, connections: number[][]): number[][] {
    const adj: number[][] = new Array(n).fill(0).map(() => ([]));
    for (const [s, e] of connections) {
        adj[s].push(e);
        adj[e].push(s);
    }

    let time: number = 0;
    const disc: number[] = new Array(n).fill(-1);
    const low: number[] = new Array(n).fill(-1);
    const parent: number[] = new Array(n).fill(-1);

    const res: number[][] = [];

    const dfs = (id: number) => {
        time += 1;

        low[id] = disc[id] = time;

        for (const nei of adj[id]) {
            if (parent[id] === nei) {
                continue;
            }
            if (disc[nei] === -1) {
                parent[nei] = id;
                dfs(nei);
                low[id] = Math.min(low[id], low[nei]);
            } else {
                low[id] = Math.min(low[id], disc[nei]);
            }

            if (low[nei] > disc[id]) {
                res.push([id, nei]);
            }
        }
    };

    dfs(0);



    return res;
};

const test = () => {
    const params = [
        {
            input: {
                n: 4, connections: [[0,1],[1,2],[2,0],[1,3]]
            },
            output: [[1,3]],
        },
        {
            input: {
                n: 2, connections: [[0,1]]
            },
            output: [[0,1]],
        },
    ];

    params.forEach(({input, output}) => {
        const { n, connections } = input;
        const result = criticalConnections(n, connections);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();