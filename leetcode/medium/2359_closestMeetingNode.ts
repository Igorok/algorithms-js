function closestMeetingNode(edges: number[], node1: number, node2: number): number {
    const visited1: number[][] = new Array(edges.length).fill(0).map(() => ([-1, 10**6]));
    const visited2: number[][] = new Array(edges.length).fill(0).map(() => ([-1, 10**6]));

    const dfs = (id: number, visited: number[][], path: number) => {
        visited[id] = [1, path];

        const nei: number = edges[id];
        if (nei !== -1 && visited[nei][0] === -1) {
            dfs(nei, visited, path + 1);
        }
    }

    dfs(node1, visited1, 0);
    dfs(node2, visited2, 0);

    let res: number = -1;

    for (let i = 0; i < edges.length; ++i) {
        if (visited1[i][0] === 1 && visited2[i][0] === 1) {
            if (
                res === -1 ||
                (
                    Math.max(visited1[i][1], visited2[i][1]) < Math.max(visited1[res][1], visited2[res][1])
                )
            ) {
                res = i;
            }
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                edges: [4,4,8,-1,9,8,4,4,1,1], node1: 5, node2: 6,
            },
            output: 1,
        },
        {
            input: {
                edges: [2,2,3,-1], node1: 0, node2: 1
            },
            output: 2,
        },
        {
            input: { edges: [1,2,-1], node1: 0, node2: 2 },
            output: 2,
        },
        {
            input: { edges: [1,2,3,4,5,-1,5], node1: 0, node2: 6 },
            output: 5,
        },
    ];

    params.forEach(({input, output}) => {
        const { edges, node1, node2 } = input;
        const result = closestMeetingNode(edges, node1, node2);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();