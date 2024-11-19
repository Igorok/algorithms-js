/**
 * @param {number[]} prices
 * @param {number} fee
 * @return {number}
 */
var maxProfit = function(prices, fee) {

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
1  -2   0  -1   5   1   6
3  -2  -2  -3   3  -1   4
2  -2  -2  -2   4   0   5
8  -2  -2  -2  -2  -6  -1
4  -2  -2  -2  -2  -2   3
9


    1   3   2   8   4   9
s   0   0  -1   5  -1   8
b  -3  -3  -3   5  -1   8
     -5/-3
        -4/-3






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
        const result = shortestSubarray(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();