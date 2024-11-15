/**
 * @param {number[]} nums
 * @return {boolean}
 */
var hasTrailingZeros = function(nums) {
    let count = 0;
    for (const num of nums) {
        if ((num % 2) === 0) {
            count += 1;
        }
        if (count === 2) {
            return true;
        }
    }
    return false;
};


`
 100
1000
`


const test = () => {
    const params = [
        {
            input: [1,2,3,4,5],
            output: true,
        },
        {
            input: [2,4,8,16],
            output: true,
        },
        {
            input: [1,3,5,7,9],
            output: false,
        },
    ];

    for (const { input, output } of params) {
        const result = hasTrailingZeros(input);
        const message = `
            INPUT: ${input}
            OUTPUT: ${output}
            RESULT: ${result}
            `;

        if (result === output) {
            console.log(
                'SUCCESS: \n', message,
            );
        } else {
            console.error('ERROR: \n', message);
        }
    }
};

test();
