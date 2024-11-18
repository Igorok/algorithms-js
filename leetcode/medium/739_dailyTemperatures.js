/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures_1 = function(temperatures) {
    const res = new Array(temperatures.length).fill(0);

    for (let i = 0; i < temperatures.length - 1; ++i) {
        for (let j = i + 1; j < temperatures.length; ++j) {
            if (temperatures[j] > temperatures[i]) {
                res[i] = j - i;
                break;
            }
        }
    }

    return res;
};

var dailyTemperatures = function(temperatures) {
    const res = new Array(temperatures.length).fill(0);

    const stack = [];

    for (let i = temperatures.length - 1; i > -1; --i) {
        const t = temperatures[i];

        while (stack.length && stack[stack.length - 1][0] <= t) {
            stack.pop();
        }

        if (stack.length) {
            const [pT, pI] = stack[stack.length - 1];
            res[i] = pI - i;
        }

        stack.push([t, i]);
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: [73,74,75,71,69,72,76,73],
            output: [1,1,4,2,1,1,0,0],
        },

        {
            input: [30,40,50,60],
            output: [1,1,1,0],
        },
        {
            input: [30,60,90],
            output: [1,1,0],
        },
    ];

    params.forEach(({input, output}) => {
        const result = dailyTemperatures(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();