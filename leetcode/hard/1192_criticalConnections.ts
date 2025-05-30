function criticalConnections(n: number, connections: number[][]): number[][] {
    return [];
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