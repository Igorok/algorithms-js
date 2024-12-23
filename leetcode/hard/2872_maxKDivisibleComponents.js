/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} values
 * @param {number} k
 * @return {number}
 */
var maxKDivisibleComponents = function(n, edges, values, k) {
    const adj = new Array(n).fill(0).map(() => []);
    edges.forEach(([s, e]) => {
        adj[s].push(e);
        adj[e].push(s);
    });

    let res = 0;
    const visited = new Array(n).fill(0);

    const dfs = (node) => {
        visited[node] = 1;

        let totalSum = values[node];
        for (const nei of adj[node]) {
            if (visited[nei]) continue;

            const sum = dfs(nei);
            if (sum % k) {
                totalSum += sum;
            } else {
                res += 1;
            }
        }

        return totalSum;
    }

    for (let i = 0; i < n; ++i) {
        if (!visited[i]) dfs(i)
    }

    return res + 1;
};

/*

3

5 5 1 2 6

10 1 3 1

*/


const test = () => {
    const params = [
        {
            input: [5, [[0,2],[1,2],[1,3],[2,4]], [1,8,1,4,4], 6],
            output: 2,
        },
        {
            input: [7, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [3,0,6,1,5,2,1], 3],
            output: 3,
        },
    ];

    params.forEach(({input, output}) => {
        const result = maxKDivisibleComponents(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();