/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} distanceThreshold
 * @return {number}
 */
var findTheCity = function(n, edges, distanceThreshold) {
    const matrix = new Array(n).fill(0).map(() => []);

    let cities = new Array(n).fill(0).map((v, i) => [i, 0]);

    for (const [ from, to, weight ] of edges) {
        matrix[from].push([ to, weight ]);
        matrix[to].push([ from, weight ]);
    }
    matrix.map((arr) => arr.sort((a, b) => a[1] - b[1]));

    const dfs = ({ node, nodes, visited, path }) => {

        for (const [to, weight] of matrix[node]) {
            const p = path[node] + weight;
            if (
                p <= distanceThreshold
                && (!visited[to] || p < path[to])
            ) {
                path[to] = p;
                visited[to] = 1;
                nodes.add(to);
                dfs({ node: to, nodes, visited, path });
            }
        }

        return nodes;
    };

    let min = -1;
    let minCount = 10e6;

    for (let i = 0; i < n; ++i) {
        let nodes = new Set();
        let visited = new Array(n).fill(0);
        visited[i] = 1;
        let path = new Array(n).fill(0);

        dfs({ node: i, nodes, visited, path });

        if (nodes.size < minCount) {
            min = i;
            minCount = nodes.size;
        } else if (nodes.size === minCount && i > min) {
            min = i;
            minCount = nodes.size;
        }
    }

    return min;
};

const test = () => {
    const params = [
        {
            input: [4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4],
            output: 3,
        },
        {
            input: [5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2],
            output: 0,
        }
    ];
    params.forEach(({ input, output }) => {
        const result = findTheCity(...input);

        console.log(
            (JSON.stringify(output) === JSON.stringify(result)) ? 'SUCCESS' : 'ERROR',
            '\n input', JSON.stringify(input),
            '\n output', output,
            '\n result', result,
        );
    });
};
test();
