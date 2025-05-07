function change(amount: number, coins: number[]): number {
    if (amount === 0) return 0;

    coins.sort((a, b) => a - b);

    let prev: number[] = new Array(amount + 1).fill(0);
    let curr: number[] = new Array(amount + 1).fill(0);

    for (const coin of coins) {
        prev = curr;
        curr = new Array(amount + 1).fill(0);

        for (let i: number = 1; i <= amount; ++i) {
            const top: number = prev[i];
            if (coin === i) {
                curr[i] = 1;
            } else if (i > coin) {
                curr[i] = curr[i - coin];
            }
            curr[i] += top;
        }
    }

    return curr.at(-1);
};

/*

  0 1 2 3 4 5
1 0 1 1 1 1 1
2 0 1 2 2 3 3
5 0 1 2 2 3 4

*/

const test = () => {
    const params = [
        {
            input: { amount: 5, coins: [1,2,5] },
            output: 4,
        },
        {
            input: { amount: 3, coins: [2] },
            output: 0,
        },
        {
            input: { amount: 10, coins: [10] },
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const { amount, coins } = input;

        const result = change(amount, coins);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();
