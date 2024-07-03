/*
Best Time to Buy and Sell Stock [7,1,5,3,6,4]
There is array with prices, and I should find largest profit between buy and sell.
My profit is 0 and the day of buy is 0. I go through all array, this is a day of a sell. If I find a price lower I will change a day of a buy to this index. If difference between current price and price of a buy is large than 0 I can update my profit.
*/


/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    if (prices?.length < 2) return 0;

    let profit = 0;
    let buy = 0;

    for (let i = 1; i < prices.length; ++i) {
        if (prices[i] < prices[buy]) {
            buy = i;
        }

        if (prices[i] - prices[buy] > 0) {
            profit = Math.max(profit, prices[i] - prices[buy]);
        }

    }

    return profit;
};

const test = () => {
    const params = [
        {
            input: [7,1,5,3,6,4],
            output: 5,
        },
        {
            input: [7,6,4,3,1],
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const result = maxProfit(input);

        console.log(
            result === output ? 'SUCCESS ' : 'ERROR ',
            'input', input,
            'output', output,
            'result', result,
        );

    });
};

test();
