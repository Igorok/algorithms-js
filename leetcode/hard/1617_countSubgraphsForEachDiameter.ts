function countSubgraphsForEachDiameter(n: number, edges: number[][]): number[] {
    return [];
};

const test = () => {
    const params = [
        {
            input: {
                n: 4, edges: [[1,2],[2,3],[2,4]]
            },
            output: [3,4,0],
        },
        {
            input: {
                n: 2, edges: [[1,2]]
            },
            output: [1],
        },
        {
            input: {
                n: 3, edges: [[1,2],[2,3]]
            },
            output: [2,1],
        },
    ];

    params.forEach(({input, output}) => {
        const { n, edges } = input;
        const result = countSubgraphsForEachDiameter(n, edges);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();