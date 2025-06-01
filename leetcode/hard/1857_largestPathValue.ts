function largestPathValue(colors: string, edges: number[][]): number {
    const visited: number[] = new Array(colors.length).fill(0);
    const memo: number[][] = new Array(colors.length).fill(0).map(() => new Array(26).fill(0));
    const adj: number[][] = new Array(colors.length).fill(0).map(() => []);
    for (const [s, e] of edges) {
        adj[s].push(e);
    }

    const aCode = 'a'.charCodeAt(0);
    let res: number = 1;

    const dfs = (id: number): void => {
        if (visited[id] === 1 || res === Number.POSITIVE_INFINITY) {
            res = Number.POSITIVE_INFINITY;
            return;
        }

        if (visited[id] === 2) {
            return;
        }

        visited[id] = 1;

        const idColor: number = colors[id].charCodeAt(0) - aCode;
        memo[id][idColor] = 1;

        for (const nei of adj[id]) {
            if (visited[nei] === 1) {
                res = Number.POSITIVE_INFINITY;
                return;
            }

            dfs(nei);

            for (let i: number = 0; i < 26; ++i) {
                let newColorCount: number = memo[nei][i];
                if (idColor === i) {
                    newColorCount += 1;
                }
                memo[id][i] = Math.max(memo[id][i], newColorCount);
            }

            res = Math.max(res, ...memo[id]);
        }

        visited[id] = 2;
    }

    for (let i: number = 0; i < colors.length; ++i) {
        dfs(i);
    }

    return (res === Number.POSITIVE_INFINITY) ? -1 : res;
};

const test = () => {
    const params = [
        {
            input: {
                colors: "abaca", edges: [[0,1],[0,2],[2,3],[3,4]]
            },
            output: 3,
        },
        {
            input: {
                colors: "a", edges: [[0,0]],
            },
            output: -1,
        },
    ];

    params.forEach(({input, output}) => {
        const { colors, edges } = input;
        const result = largestPathValue(colors, edges);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();