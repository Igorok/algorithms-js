function shipWithinDays(weights: number[], days: number): number {

    const isOk = (val: number) => {
        let daysForTotal: number = 1;
        let acc: number = 0;

        for (let i: number = 0; i < weights.length; ++i) {
            if (weights[i] > val) {
                return false;
            }

            if (acc + weights[i] <= val) {
                acc += weights[i];
                continue;
            }

            daysForTotal += 1;
            acc = weights[i];

            if (daysForTotal > days) {
                return false;
            }
        }

        return true;
    }

    let start: number = 1;
    let end: number = weights.reduce((acc: number, val: number) => acc + val, 0);
    let res: number = end;

    while (start <= end) {
        const middle: number = Math.floor((start + end) / 2);

        if (isOk(middle)) {
            res = middle;
            end = middle - 1;
        } else {
            start = middle + 1;
        }
    }

    return res;
};


const test = () => {
    const params = [
        {
            input: {
                weights: [1,2,3,4,5,6,7,8,9,10],
                days: 5
            },
            output: 15,
        },
        {
            input: {
                weights: [3,2,2,4,1,4],
                days: 3,
            },
            output: 6,
        },
        {
            input: {
                weights: [1,2,3,1,1],
                days: 4,
            },
            output: 3,
        },
    ];

    params.forEach(({input, output}) => {
        const { weights, days } = input;
        const result = shipWithinDays(weights, days);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();