function maxCoins(piles: number[]): number {
    piles.sort((a, b) => b - a);

    const rounds: number = piles.length / 3;

    let sum: number = 0;
    let id: number = 1;
    for (let i: number = 0; i < rounds; ++i) {
        sum += piles[id];
        id += 2;
    }

    return sum;
};

/*

[
  8,
  7,
  4,
  2,
  2,
  1,
]

0 1 2 3 4 5 6 7 8
9,8,7,6,5,1,2,3,4


*/

const test = () => {
    const params = [
        {
            input: {
                piles: [2,4,1,2,7,8],
            },
            output: 9,
        },
        {
            input: {
                piles: [2,4,5],
            },
            output: 4,
        },
        {
            input: {
                piles: [9,8,7,6,5,1,2,3,4]
            },
            output: 18,
        },
    ];

    params.forEach(({input, output}) => {
        const { piles } = input;

        const result = maxCoins(piles);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();