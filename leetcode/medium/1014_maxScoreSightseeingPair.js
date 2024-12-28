/**
 * @param {number[]} values
 * @return {number}
 */
var maxScoreSightseeingPair_0 = function(values) {
    let res = Number.MIN_SAFE_INTEGER;

    for (let i = 0; i < values.length; ++i) {
        for (let j = i+1; j < values.length; ++j) {
            res = Math.max(res, values[i] + values[j] - i - j);
        }
    }

    return res;
};


/*

8,1,5,2,6

8 2 7  5 10
8 0 3 -1 2


*/

var maxScoreSightseeingPair_1 = function(values) {
    const iArrMax = [values[0]];
    for (let i = 1; i < values.length; ++i) {
        iArrMax.push(Math.max(
            iArrMax[i-1],
            values[i] + i,
        ));
    }
    const jArrMax = [];
    jArrMax[values.length-1] = values[values.length-1] - (values.length-1);
    for (let i = values.length-2; i > -1; --i) {
        jArrMax[i] = Math.max(
            jArrMax[i + 1],
            values[i] - i,
        );
    }

    let res = -1;

    for (let i = 0; i < values.length-1; ++i) {
        res = Math.max(res, iArrMax[i]+jArrMax[i+1]);
    }

    return res;
};

var maxScoreSightseeingPair_2 = function(values) {
    const jArrMax = [];
    jArrMax[values.length-1] = values[values.length-1] - (values.length-1);
    for (let i = values.length-2; i > -1; --i) {
        jArrMax[i] = Math.max(
            jArrMax[i + 1],
            values[i] - i,
        );
    }

    let res = -1;
    let l = -1;

    for (let i = 0; i < values.length-1; ++i) {
        l = Math.max(l, values[i] + i);
        res = Math.max(res, l + jArrMax[i+1]);
    }

    return res;
};

var maxScoreSightseeingPair_3 = function(values) {
    let res = -1;

    let right = values[values.length-1] - (values.length-1);

    for (let i = values.length-2; i > -1; --i) {
        const left = values[i] + i;
        res = Math.max(res, left + right);
        right = Math.max(
            right,
            values[i] - i,
        );
    }

    return res;
};


var maxScoreSightseeingPair = function(values) {
    let res = -1;
    let left = values[0];

    for (let i = 1; i < values.length; ++i) {
        res = Math.max(left + values[i] - i, res);
        left = Math.max(values[i] + i, left);
    }

    return res;
};


const test = () => {
    const params = [
        {
            input: [8,1,5,2,6],
            output: 11,
        },
        {
            input: [1,2],
            output: 2,
        },
        {
            input: [10,1,1,1,1,1,10],
            output: 14,
        },
        {
            input: [10,1,1,1,8,8,1,1,10],
            output: 15,
        },
    ];

    params.forEach(({input, output}) => {
        const result = maxScoreSightseeingPair(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();