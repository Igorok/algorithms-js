function getSkyline(buildings: number[][]): number[][] {
    return [];
};

const test = () => {
    const params = [
        {
            input: {
                buildings: [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]],
            },
            output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]],
        },
        {
            input: {
                buildings: [[0,2,3],[2,5,3]],
            },
            output: [[0,3],[5,0]],
        },
    ];

    params.forEach(({input, output}) => {
        const { buildings } = input;
        const result = getSkyline(buildings);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

