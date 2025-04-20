function maxProfit(prices: number[]): number {
    const costs: number[] = new Array(prices.length).fill(0);
    costs[0] = prices[0];
    const gain: number[] = new Array(prices.length).fill(0);

    for (let i: number = 1; i < prices.length; ++i) {
        costs[i] = Math.min(costs[i-1], prices[i] - gain[i-1]);
        gain[i] = Math.max(gain[i-1], prices[i] - costs[i]);
    }

    return gain.at(-1) || 0;
};

/*

p   [7, 1, 5, 3, 6, 4]
c   [7, 1, 1,-1,-1,-3]
g   [0, 0, 4, 4, 7, 7]

costs[n] = min(costs[n-1], price[n] - gain[n-1])
gain[n] = max(gain[n-1], price[n] - costs[n])


*/



const test = () => {
    const params = [
        {
            input: [7,1,5,3,6,4],
            output: 7,
        },
        {
            input: [1,2,3,4,5],
            output: 4,
        },
        {
            input: [7,6,4,3,1],
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const result = maxProfit(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();