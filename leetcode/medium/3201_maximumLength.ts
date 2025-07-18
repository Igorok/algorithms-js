function maximumLength_0(nums: number[]): number {
    const onlyEven: number[] = [];
    const onlyOdd: number[] = [];
    const evenFirst: number[] = [];
    const oddFirst: number[] = [];

    for (const num of nums) {
        if (num & 1) {
            onlyOdd.push(num);

            if (oddFirst.length === 0 || (oddFirst.at(-1) & 1) === 0) {
                oddFirst.push(num);
            }

            if (evenFirst.length !== 0 && (evenFirst.at(-1) & 1) === 0) {
                evenFirst.push(num);
            }
        } else {
            onlyEven.push(num);

            if (oddFirst.length !== 0 && (oddFirst.at(-1) & 1) === 1) {
                oddFirst.push(num);
            }

            if (evenFirst.length === 0 || (evenFirst.at(-1) & 1) === 1) {
                evenFirst.push(num);
            }
        }
    }


    return Math.max(
        onlyEven.length,
        onlyOdd.length,
        evenFirst.length,
        oddFirst.length,
    );
};

function maximumLength(nums: number[]): number {
    const onlyEven: number[] = [-1, 0];
    const onlyOdd: number[] = [-1, 0];
    const evenFirst: number[] = [-1, 0];
    const oddFirst: number[] = [-1, 0];

    for (const num of nums) {
        if (num & 1) {
            onlyOdd[1] += 1;

            if (oddFirst[1] === 0 || (oddFirst[0] & 1) === 0) {
                oddFirst[0] = num;
                oddFirst[1] += 1;
            }

            if (evenFirst[1] !== 0 && (evenFirst[0] & 1) === 0) {
                evenFirst[0] = num;
                evenFirst[1] += 1;
            }
        } else {
            onlyEven[1] += 1;

            if (oddFirst[1] !== 0 && (oddFirst[0] & 1) === 1) {
                oddFirst[0] = num;
                oddFirst[1] += 1;
            }

            if (evenFirst[1] === 0 || (evenFirst[0] & 1) === 1) {
                evenFirst[0] = num;
                evenFirst[1] += 1;
            }
        }
    }


    return Math.max(
        onlyEven[1],
        onlyOdd[1],
        evenFirst[1],
        oddFirst[1],
    );
};

const test = () => {
    const params = [
        {
            input: {
                nums: [1,2,3,4],
            },
            output: 4,
        },
        {
            input: {
                nums: [1,2,1,1,2,1,2],
            },
            output: 6,
        },
        {
            input: {
                nums: [1,3],
            },
            output: 2,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums } = input;
        const result = maximumLength(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();