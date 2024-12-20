/**
 * @param {number[]} prices
 * @return {number[]}
 */
var finalPrices = function(prices) {
    const res = new Array(prices.length).fill(0);
    const stack = [];
    for (let i = prices.length - 1; i > -1; --i) {
        const price = prices[i];
        while (stack.length && stack[stack.length - 1] > price) {
            stack.pop();
        }
        const discount = stack.length ? stack[stack.length - 1] : 0;
        res[i] = price - discount;
        stack.push(price);
    }
    return res;
};

const test = () => {
    const params = [
        {
            input: [8,4,6,2,3],
            output: [4,2,4,2,3],
        },
    ];

    params.forEach(({input, output}) => {
        const result = finalPrices(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();
