/**
 * @param {number[]} prices
 * @param {number} fee
 * @return {number}
 */
var maxProfit = function(prices, fee) {
    const profit = new Array(prices.length).fill(0);
    const buy = new Array(prices.length).fill(0);

    buy[0] = prices[0];

    for (let i = 1; i < prices.length; ++i) {
        profit[i] = Math.max(profit[i - 1], prices[i] - buy[i - 1] - fee); // my income, maximisation
        buy[i] = Math.min(buy[i - 1], prices[i] - profit[i]);  // my expenses, minimisation
    }

    return profit[profit.length - 1];
};


/*

    1   3   2   8   4   9
1
3
2
8
4
9

2
    1   3   2   8   4   9
s   0   0   0   5   5 9--1-2 = 8
b   1   1   1   1  -1  1

sell[i] = max(sell[i-1], price[i] - buy[i - 1])
buy[i] = min(buy[i - 1], price[i]- sell[i])

*/

const test = () => {
    const params = [
        {
            input: [[1,3,2,8,4,9], 2],
            output: 8,
        },
        {
            input: [[1,3,7,5,10,3], 3],
            output: 6,
        },
    ];

    params.forEach(({input, output}) => {
        const result = maxProfit(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();