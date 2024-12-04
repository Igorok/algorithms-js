/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    const buy = new Array(prices.length).fill(0);
    const profit = new Array(prices.length).fill(0);
    buy[0] = prices[0];

    for (let i = 1; i < prices.length; ++i) {
        buy[i] = Math.min(prices[i], buy[i - 1], prices[i] - profit[i-1]);
        profit[i] = prices[i] - buy[i];
    }

    return profit[profit.length - 1];
};


/*


price   [7, 1, 5, 3, 6, 4]
buy     [7, 1, 1,-1,-1,-3] min
profit  [0, 0, 4, 4, 7, 7] max

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