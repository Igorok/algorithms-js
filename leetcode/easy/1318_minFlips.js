/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var minFlips_1 = function(a, b, c) {
    const aArr = parseInt(a).toString(2).split('').reverse();
    const bArr = parseInt(b).toString(2).split('').reverse();
    const cArr = parseInt(c).toString(2).split('').reverse();

    const maxLength = Math.max(aArr.length, bArr.length, cArr.length);
    let res = 0;

    for (let i = 0; i < maxLength; ++i) {
        const aBit = aArr[i] || '0';
        const bBit = bArr[i] || '0';
        const cBit = cArr[i] || '0';

        if (cBit === '0') {
            if (aBit === '1') res += 1;
            if (bBit === '1') res += 1;
        } else {
            if (aBit === '1' || bBit === '1') continue;
            res += 1;
        }
    }

    return res;
};


var minFlips = function(a, b, c) {
    let res = 0;
    while (a || b || c) {
        const aBit = a & 1;
        const bBit = b & 1;
        const cBit = c & 1;

        if (cBit === 0) {
            if (aBit === 1) res += 1;
            if (bBit === 1) res += 1;
        } else {
            if (aBit !== 1 && bBit !== 1) {
                res += 1;
            };
        }

        a = a >> 1;
        b = b >> 1;
        c = c >> 1;
    }

    return res;
};

/*

[2, 6, 5]

010
110
101


*/

const test = () => {
    const params = [
        {
            input: [2, 6, 5],
            output: 3,
        },
        {
            input: [4, 2, 7],
            output: 1,
        },
        {
            input: [1, 2, 3],
            output: 0,
        },
    ];

    for (const { input, output } of params) {
        const result = minFlips(...input);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${output}
            RESULT: ${result}
            `;

        if (JSON.stringify(result) === JSON.stringify(output)) {
            console.log(
                'SUCCESS: \n', message,
            );
        } else {
            console.error('ERROR: \n', message);
        }
    }
};

test();
