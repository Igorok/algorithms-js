/**
 * @param {number} n
 * @param {number} time
 * @return {number}
 */
var passThePillow = function(n, time) {
    if (n === 1) return 1;
    if (time === n) {
        return n - 1;
    }
    if (time < n) return time + 1;
    if (n === 2) {
        return (time % n) ? 2 : 1;
    }

    // first traverse
    const rem = time - n;

    const i = Math.ceil(rem / (n - 1)) + 1;
    const j = rem % (n - 1);


    if (i % 2) {
        return 1 + j + 1;
    } else {
        return n - 1 - j;
    }
};


/*

10
1 2 3 4 5 6
5 4 3 2 1


8
1 2 3
2 1
2 3
2 1

2 3
2 1
2 3

54
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 // 18
17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 // 35
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 // 52
17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 // 69
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18


2 341
1
2
1
2
1
2
1
2

*/

const test = () => {
    const params = [
        {
            input: [3, 4],
            output: 1,
        },
        {
            input: [3, 8],
            output: 1,
        },
        {
            input: [18, 54],
            output: 15,
        },


        {
            input: [4, 5],
            output: 2,
        },
        {
            input: [3, 2],
            output: 3,
        },
        {
            input: [18, 38],
            output: 5,
        },
        {
            input: [2, 341],
            output: 2,
        },
    ];

    params.forEach(({input, output}) => {
        const result = passThePillow(...input);

        console.log(
            result === output ? 'SUCCESS ' : 'ERROR ',
            'input', input,
            'output', output,
            'result', result,
        );

    });
};

test();
