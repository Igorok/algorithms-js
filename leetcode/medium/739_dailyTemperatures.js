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

/*

73() - 0

76 - 0
76, 72 - 1
76, 72, 69 - 1
76, 72, 71


*/
var dailyTemperatures = function(temperatures) {
    const res = new Array(temperatures.length).fill(0);
    const stack = [];
    for (let i = temperatures.length; i > -1; --i) {
        while (stack.length) {
            if (stack[stack.length - 1][0] > temperatures[i]) {
                break;
            } else {
                stack.pop();
            }
        }

        if (stack.length) {
            res[i] = stack[stack.length - 1][1] - i;
        }
        stack.push([temperatures[i], i]);
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