/**
 * @param {number} n
 * @return {number}
 *
 * 790. Domino and Tromino Tiling
 * https://www.youtube.com/watch?v=auyxudCV_aU
 * https://www.youtube.com/watch?v=CecjOo4Zo-g
 */
var numTilings_1 = function(n) {
    if (n <= 2) return n;

    let res = [1, 1, 2]
    for (let i = 3; i <= n; ++i) {
        const [r1, r2, r3] = res;
        const r4 = (r3 * 2 + r1) % (10e8 + 7);
        res = [r2, r3, r4];
    }

    console.log(
        'res', res,
    );

    return res[2];
};

/*
1
a
a

2
bb  a a
bb  a a


3
bb a    abb    aaa   ccd    cdd
bb a    abb    aaa   cdd    ccd


4
bb bb    bbaa    aabb    abba    aaaa    ccda    accd    cdda    acdd    cbbd    ccdd
bb bb    bbaa    aabb    abba    aaaa    cdda    acdd    ccda    accd    ccdd    cbbd


a-
a-

--
bb

c--
cc-

cc-
c--

c--
bb-

bb-
c--




Even
a-
a-
res = acc[-1]+1

--
bb
res = acc[-2] + 1

Odd
c--
cc-
res = acc[-1] + 1

cc-
c--
res = acc[-1] + 1

*/


var numTilings_2 = function(n) {
    const div = 10e8+7;
    const accEven = new Array(n).fill(0);
    const accOdd = new Array(n).fill(0);
    accEven[0] = 1;
    accEven[1] = 1;
    accOdd[0] = 0;
    accOdd[1] = 1;
    for (let i = 2; i <= n; ++i) {
        accEven[i] = (accEven[i - 1] + accEven[i - 2] + accOdd[i - 2]*2) % div;
        accOdd[i] = (accOdd[i-1] + accEven[i-1]) % div;
    }

    console.log(
        'accEven', accEven,
        'accOdd', accOdd,
    );

    return accEven[n];
};


var numTilings = function(n) {
    const div = 10e8+7;
    const memo = new Array(n).fill(0).map(() => new Array(4).fill(-1));

    const getState = (c1, c2) => {
        // ?
        // ?
        if (c1 && c2) return 0;
        // c
        // ?
        if (!c1 && c2) return 1;
        // ?
        // c
        if (c1 && !c2) return 2;
        // a
        // a
        return 3;
    };

    const rec = (i, c1, c2) => {
        if (i == n) return 1;

        const state = getState(c1, c2);

        // console.log(
        //     'i', i,
        //     'c1', c1,
        //     'c2', c2,
        //     'state', state,
        // );

        if (memo[i][state] !== -1) return memo[i][state];

        let c3 = (i + 1 < n);
        let c4 = (i + 1 < n);
        let count = 0;

        // a ?
        // a ?
        if (c1 && c2) count += rec(i + 1, true, true);
        // b b
        // b b
        if (c1 && c2 && c3 && c4) count += rec(i + 1, false, false);
        // c ?
        // c c
        if (c1 && c2 && c3 && c4) count += rec(i + 1, true, false);
        // c c
        // c ?
        if (c1 && c2 && c3 && c4) count += rec(i + 1, false, true);
        // c d
        // d d
        if (!c1 && c2 && c3 && c4) count += rec(i + 1, false, false);
        // d d
        // c d
        if (c1 && !c2 && c3 && c4) count += rec(i + 1, false, false);
        // c ?
        // b b
        if (!c1 && c2 && c3 && c4) count += rec(i + 1, true, false);
        // b b
        // c ?
        if (c1 && !c2 && c3 && c4) count += rec(i + 1, false, true);
        // a a
        // a a
        if (!c1 && !c2) count += rec(i + 1, true, true);

        console.log(
            'i', i,
            'c1', c1,
            'c2', c2,
            'state', state,
            'count', count,
        );

        memo[i][state] = count % div;

        return memo[i][state];
    };

    const res = rec(0, true, true);

    return res;
};



const test = () => {
    const params = [
        {
            input: 1,
            output: 1,
        },
        {
            input: 2,
            output: 2,
        },
        {
            input: 3,
            output: 5,
        },
        // {
        //     input: 4,
        //     output: 11,
        // },
        // {
        //     input: 5,
        //     output: 24,
        // },
        // {
        //     input: 6,
        //     output: 53,
        // },
        // {
        //     input: 7,
        //     output: 117,
        // },
        // {
        //     input: 26,
        //     output: 393528322,
        // },
        // {
        //     input: 27,
        //     output: 867954037,
        // },
        // {
        //     input: 28,
        //     output: 914332884,
        // },
        // {
        //     input: 30,
        //     output: 312342182,
        // },
    ];

    for (const { input, output } of params) {
        const result = numTilings(input);
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
