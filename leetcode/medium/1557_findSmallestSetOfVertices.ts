function findSmallestSetOfVertices(n: number, edges: number[][]): number[] {
    const parents: number[][] = new Array(n).fill(0).map(() => []);

    for (const [s, e] of edges) {
        parents[e].push(s);
    }

    const res: number[] = [];
    for (let i: number = 0; i < n; ++i) {
        if (parents[i].length === 0) {
            res.push(i);
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                n: 6, edges: [[0,1],[0,2],[2,5],[3,4],[4,2]],
            },
            output: [0,3],
        },
        {
            input: {
                n: 5, edges: [[0,1],[2,1],[3,1],[1,4],[2,4]],
            },
            output: [0,2,3],
        },
    ];

    params.forEach(({input, output}) => {
        const { n, edges } = input;
        const result = findSmallestSetOfVertices(n, edges);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

