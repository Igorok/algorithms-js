function countPyramids(grid: number[][]): number {
    return 0;
};

/*

[
[1,1,1,1,0],
[1,1,1,1,1],
[1,1,1,1,1],
[0,1,0,0,1]
]


*/

const test = () => {
    const params = [
        {
            input: {
                grid: [[0,1,1,0],[1,1,1,1]],
            },
            output: 2,
        },
        {
            input: {
                grid: [[1,1,1],[1,1,1]],
            },
            output: 2,
        },
        {
            input: {
                grid: [[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,0,0,1]],
            },
            output: 13,
        },
    ];

    params.forEach(({input, output}) => {
        const { grid } = input;
        const result = countPyramids(grid);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();