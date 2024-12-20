/**
 * @param {number[]} arr
 * @return {number}
 */
var maxChunksToSorted_1 = function(arr) {
    const stack = [];

    let max = -1;
    for (const num of arr) {

        while (stack.length && stack.at(-1) > num) {
            stack.pop();
        }
        if (!stack.length || num >= max) {
            max = Math.max(max, num);
            stack.push(num);
        }
    }

    return stack.length;
};

var maxChunksToSorted_2 = function(arr) {
    const stack = [];

    for (const num of arr) {
        let max = num;

        while (stack.length && num < stack.at(-1)) {
            const r = stack.pop();
            max = Math.max(max, r);
        }

        stack.push(max);
    }

    return stack.length;
};

var maxChunksToSorted = function(arr) {
    const stack = [];

    for (const num of arr) {
        if (!stack.length || stack.at(-1) < num) {
            stack.push(num);
        } else {
            let max = stack.at(-1);

            while (stack.length && num < stack.at(-1)) {
                stack.pop();
            }

            stack.push(max);
        }
    }

    return stack.length;
};

/*

[2,0,4,6,3,1,7,5,8],


*/


const test = () => {
    const params = [
        {
            input: [4,3,2,1,0],
            output: 1,
        },
        {
            input: [1,0,2,3,4],
            output: 4,
        },
        {
            input: [4, 3, 1, 2, 5, 6, 7, 1, 2, 5, 8, 9],
            output: 3,
        },
        {
            input: [0,2,1],
            output: 2,
        },
        {
            input: [2,0,4,6,3,1,7,5,8],
            output: 2,
        },
    ];

    params.forEach(({input, output}) => {
        const result = maxChunksToSorted(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();