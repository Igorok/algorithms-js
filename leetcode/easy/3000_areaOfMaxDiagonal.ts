function areaOfMaxDiagonal(dimensions: number[][]): number {
    let id: number = 0;

    const rectangles: number[][] = [];
    rectangles[0] = [
        Math.sqrt(dimensions[id][0]**2 + dimensions[id][1]**2),
        dimensions[id][0] * dimensions[id][1],
    ];

    for (let i: number = 1; i < dimensions.length; ++i) {
        rectangles[i] = [
            Math.sqrt(dimensions[i][0]**2 + dimensions[i][1]**2),
            dimensions[i][0] * dimensions[i][1],
        ];

        if (
            rectangles[i][0] > rectangles[id][0] ||
            (rectangles[i][0] === rectangles[id][0] && rectangles[i][1] > rectangles[id][1])
        ) {
            id = i;
        }
    }


    return rectangles[id][1];
};

const test = () => {
    const params = [
        {
            input: {
                dimensions: [[9,3],[8,6]],
            },
            output: 48,
        },
        {
            input: {
                dimensions: [[3,4],[4,3]],
            },
            output: 12,
        },
    ];

    params.forEach(({input, output}) => {
        const { dimensions } = input;
        const result = areaOfMaxDiagonal(dimensions);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();