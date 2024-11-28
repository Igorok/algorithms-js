/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[]}
 */
var shortestDistanceAfterQueries = function(n, queries) {
    // Breadth first search
    const bfs = (adj, start, end) => {
        const queue = [[start, 0]];
        const visited = new Set();

        while (queue.length) {
            const [node, path] = queue.shift();

            visited.add(node);
            if (node === end) {
                return path;
            }

            for (const nei of adj[node]) {
                if (!visited.has(nei)) {
                    queue.push([nei, path + 1]);
                }
            }
        }

        return 0;
    };

    // adjacency matrix
    const adj = [];
    for (let i = 0; i < n - 1; ++i) {
        adj.push([i + 1]);
    }
    adj.push([]);

    const res = [];
    for (const [s, e] of queries) {
        // add new edge
        adj[s].push(e);
        // find new path
        res.push(bfs(adj, 0, n - 1));
    }

    return res;
};

/*



*/

const test = () => {
    const params = [
        {
            input: [5, [[2,4],[0,2],[0,4]]],
            output: [3,2,1],
        },
        {
            input: [4, [[0,3],[0,2]]],
            output: [1,1],
        },
    ];

    for (const { input, output } of params) {
        const result = shortestDistanceAfterQueries(...input);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${output}
            RESULT: ${result}
            `;

        if (JSON.stringify(result) === JSON.stringify(output)) {
            console.log(
                'SUCCESS: \n', message,
            );
        } else {
            console.error('ERROR: \n', message);
        }
    }
};

test();
