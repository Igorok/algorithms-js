function hIndex(citations: number[]): number {
    if (citations.at(-1) < 2) {
        return citations.at(-1);
    }

    let res: number = 1;

    let left: number = 0;
    let right: number = citations.length - 1;

    while (left <= right) {
        const middle: number = Math.floor((left + right) / 2);
        const count: number = citations[middle];
        const length: number = citations.length - middle;

        if (length === count) {
            return count;
        } else if (length > count) {
            res = Math.max(res, count);
            left = middle + 1;
        } else {
            res = Math.max(res, length)
            right = middle - 1;
        }
    }

    return res;
};

/*

1, 1, 1, 1, 1

1 2 2 3 3 3 4 4 5 5 5 5 5

*/


const test = () => {
    const params = [
        {
            input: {
                citations: [11,15],
            },
            output: 2,
        },
        {
            input: {
                citations: [1,2],
            },
            output: 1,
        },
        {
            input: {
                citations: [0,1,3,5,6],
            },
            output: 3,
        },
        {
            input: {
                citations: [1,2,100],
            },
            output: 2,
        },
        {
            input: {
                citations: [0,1,1,1,1],
            },
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const { citations } = input;
        const result = hIndex(citations);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

