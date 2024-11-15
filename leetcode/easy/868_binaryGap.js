/**
 * @param {number} n
 * @return {number}
 */
var binaryGap = function (n) {
    let res = 0;
    let i = 0;
    let one = -1;

    while (n != 0) {
        const r = n % 2;
        n = Math.floor(n / 2);


        console.log(
            'i', i,
            'n', n,
            'r', r,
            'one', one,
        );


        if (r === 1) {
            
            if (one === -1) {
                one = i;
            } else {
                res = Math.max(res, i - one);
                one = i;
            }
        }
        i += 1;
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: 22,
            output: 2,
        },
        {
            input: 8,
            output: 0,
        },
        {
            input: 5,
            output: 2,
        },
    ];

    for (const { input, output } of params) {
        const result = binaryGap(input);
        const message = `
            INPUT: ${input}
            OUTPUT: ${output}
            RESULT: ${result}
            `;

        if (result === output) {
            console.log(
                'SUCCESS \n', message,
            );
        } else {
            console.error('SUCCESS \n', message);
        }
    }
};

test();
