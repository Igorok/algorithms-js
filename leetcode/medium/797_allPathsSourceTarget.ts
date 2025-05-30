function allPathsSourceTarget(graph: number[][]): number[][] {
    const res: number[][] = [];

    const dfs = (id: number, acc: number[]): void => {
        if (id === graph.length - 1) {
            res.push([...acc]);
            return;
        }

        for (const nei of graph[id]) {
            acc.push(nei);
            dfs(nei, acc);
            acc.pop();
        }
    }

    dfs(0, [0]);

    return res;
};

const test = () => {
    const params = [
        {
            input: { graph: [[1,2],[3],[3],[]] },
            output: [[0,1,3],[0,2,3]],
        },
        {
            input: { graph: [[4,3,1],[3,2,4],[3],[4],[]] },
            output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]],
        },
    ];

    params.forEach(({input, output}) => {
        const { graph } = input;
        const result = allPathsSourceTarget(graph);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();