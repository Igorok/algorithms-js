/**
 * @param {number} n
 * @param {number} x
 * @return {number}
 */
var minEnd_1 = function(n, x) {
    console.log(
        'x: \n',
        x, parseInt(x).toString(2),

    );

    const arr = [x];
    const bitArr = [];
    let rem = x;
    while (rem !== 0) {
        bitArr.push(rem % 2);
        rem = Math.floor(rem / 2);
    }

    console.log(
        'bitArr', bitArr,
    );

    for (let i = 1; i < n; ++i) {
        let zero = -1;
        for (let j = 0; j < bitArr.length; ++j) {
            if (bitArr[j] === 0) {
                zero = j;
                break;
            }
        }

        if (zero != -1) {
            bitArr[zero] = 1;
            arr.push(parseInt([...bitArr].reverse().join(''), 2));
        }

        console.log(
            'bitArr', bitArr,
        );
    }

    console.log(
        'arr', arr,
    );


    return 0;
};

var minEnd_2 = function(n, x) {
    let last = x;

    for (let i = 1; i < n; ++i) {
        let b = last + 1;
        while ((b & x) !== x) {
            b += 1;
        }
        last = b;
    }

    return last;
};

var minEnd = function(n, x) {
    let last = x;

    for (let i = 1; i < n; ++i) {
        last = (last + 1) | x;
    }

    return last;
};




const test = () => {
    const params = [
        // [4, 5, 6] = [100, 101, 110] = 100 & 101 & 110 = 100
        {
            input: [3, 4],
            output: 6,
        },
        // [7, 15] = [111, 1111] = 0111 & 1111 = 111
        {
            input: [2, 7],
            output: 15,
        },
        {
            input: [4, 1],
            output: 7,
        },
        {
            input: [6715154, 7193485],
            output: 55012476815,
        },
    ];

    for (const { input, output } of params) {
        const result = minEnd(...input);
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
