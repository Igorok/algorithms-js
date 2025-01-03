/**
 * @param {number[]} days
 * @param {number[]} costs
 * @return {number}
 */
var mincostTickets = function(days, costs) {
    const minCost = Math.min(...costs);
    const prices = [
        [1, costs[0]],
        [7, costs[1]],
        [30, costs[2]],
    ];
    const dp = new Array(days.length).fill(Number.MAX_SAFE_INTEGER);
    dp[0] = minCost;

    for (let i = 1; i < days.length; ++i) {
        const today = days[i];
        for (const [day, cost] of prices) {
            let start = i;
            while (start-1 > -1 && today - days[start-1] < day) {
                start -= 1;
            }
            const prev = start === 0 ? 0 : dp[start - 1];
            dp[i] = Math.min(dp[i], prev + cost);
        }
    }

    return dp.at(-1);
};

/*

[1,4,6,7,8,20] [2,7,15]
1,4,6,7,8,20
2 4 6 7 9 11



*/

const test = () => {
    const params = [
        {
            input: [[1,4,6,7,8,20], [2,7,15]],
            output: 11,
        },
        {
            input: [[1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]],
            output: 17,
        },
        {
            input: [[1,4,6,7,8,20], [7,2,15]],
            output: 6,
        },
    ];

    params.forEach(({input, output}) => {
        const result = mincostTickets(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();