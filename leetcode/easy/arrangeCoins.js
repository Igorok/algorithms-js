/**
 * @param {number} n
 * @return {number}
 */
var arrangeCoins_ = function(n) {
    let level = 1;
    let past = 1;
    let sum = past;

    while (sum < n) {
        const current = past + 1;
        if (n - sum < current) return level;

        sum += current;
        past = current;
        level += 1;
    }

    return level;
};

/*
a1 = a1
a2 = a1 + d
a3 = (a1 + d) + d
an = a1 + n*d

S = (a1 + an)*n / 2

тоже время, считаем все n вариантов прогрессии
*/
var arrangeCoins = function(n) {
    let level = 1;
    let sum = 1;

    while (sum < n) {
        // a1 = 1; d = 1;
        // const an = 1 + 1 * (level - 1) = level;

        level += 1;
        sum = (1 + level) * level / 2;

        if (sum > n) return level - 1;
    }

    return level;
};

/*

Sk = a1 * k + d * (k - 1)*k/2
a1 = 1
d = 1
Sk = k**2 + 0.5k
k**2 + 0.5k - Sk = 0;



*/


const test = () => {
    const params = [
        {
            input: 5,
            output: 2,
        },
        {
            input: 8,
            output: 3,
        },
    ];

    params.forEach(({input, output}) => {
        const result = arrangeCoins(input);

        console.log(
            result === output ? 'SUCCESS ' : 'ERROR ',
            'input', input,
            'output', output,
            'result', result,
        );

    });
};

test();
