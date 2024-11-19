/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit_1 = function(prices) {
    let res = 0;

    for (let i = 0; i < prices.length; ++i) {
        for (let j = i+1; j < prices.length; ++j ) {
            res = Math.max(prices[j] - prices[i], res);
        }
    }

    return res;
};

var maxProfit = function(prices) {
    let res = 0;
    let start = 0;
    for (let i = 1; i < prices.length; ++i) {
        if (prices[i] < prices[start])
            start = i;

        res = Math.max(res, prices[i] - prices[start]);
    }
    return res;
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
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();