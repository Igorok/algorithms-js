function minDominoRotations(tops: number[], bottoms: number[]): number {
    const n: number = tops.length;
    const countOfVals: Map<number, number[]> = new Map();

    for (let i: number = 0; i < n; ++i) {
        const top: number[] = countOfVals.get(tops[i]) || [0, 0, 0];
        top[0] += 1;
        top[2] += 1;
        countOfVals.set(tops[i], top);

        const bottom: number[] = countOfVals.get(bottoms[i]) || [0, 0, 0];
        bottom[1] += 1;
        if (bottoms[i] !== tops[i]) {
            bottom[2] += 1;
        }
        countOfVals.set(bottoms[i], bottom);
    }

    let res: number = Number.MAX_VALUE;

    countOfVals.forEach(([top, bottom, unique]) => {
        if (unique === n) {
            res = Math.min(res, n-top, n-bottom);
        }
    });

    return res === Number.MAX_VALUE ? -1 : res;
};

/*
[2,1,2,4,2,2]
[5,2,6,2,3,2]


[3,5,1,2,3]
[3,6,3,3,4]

1 2 1 3
1 1 1 3
*/

const test = () => {
    const params = [
        {
            input: { tops: [2,1,2,4,2,2], bottoms: [5,2,6,2,3,2] },
            output: 2,
        },
        {
            input: { tops: [3,5,1,2,3], bottoms: [3,6,3,3,4] },
            output: -1,
        },
    ];

    params.forEach(({input, output}) => {
        const { tops, bottoms } = input;

        const result = minDominoRotations(tops, bottoms);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();