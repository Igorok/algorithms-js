/**
 * @param {string} start
 * @param {string} target
 * @return {boolean}
 */
var canChange = function(start, target) {
    const n = target.length;
    let id = 0;
    for (let i = 0; i < n; ++i) {
        if (target[i] === '_') {
            continue;
        };

        while (id < n && start[id] === '_') {
            id += 1;
        }

        if (
            id === n ||
            target[i] !== start[id] ||
            (target[i] === 'R' && id > i) ||
            (target[i] === 'L' && i > id)
        ) {
            return false;
        }

        id += 1;
    }
    while (id < n && start[id] === '_') {
        id += 1;
    }

    return (id === n) ;
};


/*

_L__R__R_L

L______RR_








_L__R__R_
L______RR

l - 0
r - 7,8

l - 1
r - 4,7


*/



const test = () => {
    const params = [
        {
            input: ['_L__R__R_', 'L______RR'],
            output: true,
        },
        {
            input: ['R_L_', '__LR'],
            output: false,
        },
        {
            input: ['_R', 'R_'],
            output: false,
        },
        {
            input: ['_L__R__R_L', 'L______RR_'],
            output: false,
        },

    ];

    params.forEach(({input, output}) => {
        const result = canChange(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();