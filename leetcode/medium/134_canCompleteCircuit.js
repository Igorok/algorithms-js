/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit_0 = function(gas, cost) {
    let profitIds = [];
    let total = 0;
    for (let i = 0; i < gas.length; ++i) {
        const profit = gas[i] - cost[i];
        if (gas[i] - cost[i] >= 0) {
            profitIds.push([i, profit]);
        }
        total += profit;
    }
    profitIds = profitIds.sort((a, b) => b[1] - a[1]);

    if (!profitIds.length || total < 0) {
        return -1;
    }

    const isCorrect = (id) => {
        let path = 0;
        let barrel = 0;
        while (path < gas.length) {
            barrel += gas[id] - cost[id];
            if (barrel < 0) {
                return -1;
            }
            id = (id + 1) % gas.length;
            path += 1;
        }
        return id;
    }

    for (const profit of profitIds) {
        const id = isCorrect(profit[0]);
        if (id !== -1) return id;
    }

    return -1;
};

var canCompleteCircuit = function(gas, cost) {
    let total = 0;
    let profit = 0
    let start = 0;
    for (let i = 0; i < gas.length; ++i) {
        profit += gas[i] - cost[i];
        total += (gas[i] - cost[i]);
        if (profit < 0) {
            profit = 0;
            start = i + 1;
        }
    }

    return total < 0 ? -1 : start;
};


const test = () => {
    const params = [
        // {
        //     input: [[1,2,3,4,5], [3,4,5,1,2]],
        //     output: 3,
        // },
        // {
        //     input: [[2,3,4], [3,4,3]],
        //     output: -1,
        // },
        // {
        //     input: [[3,1,1], [1,2,2]],
        //     output: 0,
        // },
        // {
        //     input: [[5,8,2,8], [6,5,6,6]],
        //     output: 3,
        // },
        // {
        //     input: [[10,1,1,1], [1,4,3,2]],
        //     output: 0,
        // },
        {
            input: [[4,5,2,6,5,3], [3,2,7,3,2,9]],
            output: -1,
        },
    ];

    params.forEach(({input, output}) => {
        const result = canCompleteCircuit(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();