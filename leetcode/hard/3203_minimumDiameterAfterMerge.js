/**
 * @param {number[][]} edges1
 * @param {number[][]} edges2
 * @return {number}
 */
var minimumDiameterAfterMerge = function(edges1, edges2) {
    const getAdj = (arr) => {
        const adj = new Array(arr.length + 1).fill(0).map(() => []);
        for (const [s, e] of arr) {
            adj[s].push(e);
            adj[e].push(s);
        }
        return adj;
    };

    const getDiameter = (adj) => {
        const visited = new Array(adj.length).fill(0);
        let res = 0;

        const dfs = (node) => {
            let edges = [];

            for (const nei of adj[node]) {
                if (!visited[nei]) {
                    visited[nei] = 1;
                    edges.push(dfs(nei));
                }
            }

            edges = edges.sort((a, b) => b - a);

            const dist1 = edges?.[0] || 0;
            const dist2 = edges?.[1] || 0;
            const diameter = dist1 + dist2;

            res = Math.max(res, diameter);
            const dist = Math.max(dist1, dist2) + 1;

            return dist;
        };


        visited[0] = 1;
        dfs(0);

        return res;
    };

    const adj1 = getAdj(edges1);
    const adj2 = getAdj(edges2);

    const d1 = getDiameter(adj1);
    const d2 = getDiameter(adj2);

    const res = Math.max(
        Math.ceil(d1 / 2) + Math.ceil(d2 / 2) + 1,
        d1, d2,
    );

    return res;
};

const test = () => {
    const params = [
        {
            input: [[[0,1],[0,2],[0,3]], [[0,1]]],
            output: 3,
        },
        {
            input: [[[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]],
            output: 5,
        },
        {
            input: [
                [[0,1],[2,0],[3,2],[3,6],[8,7],[4,8],[5,4],[3,5],[3,9]],
                [[0,1],[0,2],[0,3]]
            ],
            output: 7,
        },
    ];

    params.forEach(({input, output}) => {
        const result = minimumDiameterAfterMerge(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();