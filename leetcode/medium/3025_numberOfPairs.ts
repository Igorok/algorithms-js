function numberOfPairs(points: number[][]): number {
    points = points.sort((a, b) => {
        if (a[0] === b[0]) {
            return b[1] - a[1];
        }
        return a[0] - b[0];
    });

    let res: number = 0;

    for (let i: number = 0; i < points.length; ++i) {
        for (let j: number = i+1; j < points.length; ++j) {
            if (points[i][1] < points[j][1]) {
                continue;
            }

            let found: boolean = false;

            for (let k: number = i+1; k < j; ++k) {
                if (
                    points[k][1] >= points[j][1] &&
                    points[k][1] <= points[i][1]
                ) {
                    found = true;
                    break;
                }
            }

            if (!found) {
                res += 1;
            }
        }
    }

    return res;
};

/*

5     x
4         x  x
3     x
2   x     x
1 x     x
0 1 2 3 4 5 6 7

*/

const test = () => {
    const params = [
        {
            input: {
                points: [[3,1],[1,3],[1,1]]
            },
            output: 2,
        },
        {
            input: {
                points: [[1,1],[2,2],[3,3]]
            },
            output: 0,
        },
        {
            input: {
                points: [[6,2],[4,4],[2,6]]
            },
            output: 2,
        },
        {
            input: {
                points: [[0,0],[0,3]]
            },
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const { points } = input;
        const result = numberOfPairs(points);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();