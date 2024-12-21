/**
 * @param {number[][]} events
 * @return {number}
 */
var maxTwoEvents_1 = function(events) {
    const arr = events.sort((a, b) => {
        if (a[1] === b[1]) return a[2] - b[2];
        return a[1] - b[1];
    });

    console.log('arr', JSON.stringify(arr));

    const memo = new Array(arr.length).fill(0);
    let res = 0;
    for (let i = 0; i < arr.length; ++i) {
        let r = arr[i][2];
        for (let j = i - 1; j > -1; --j) {
            if (arr[j][1] < arr[i][0]) {
                r = Math.max(r, arr[j][2] + arr[i][2]);
            }
        }
        res = Math.max(res, r);
    }

    return res;
};


var maxTwoEvents_2 = function(events) {
    let res = 0;

    const quick = (arr) => {
        if (arr.length < 2) return;

        const pivot = Math.floor(Math.random() * arr.length);

        let l = 0;
        let r = 0;
        const left = [];
        const middle = [];
        const right = [];

        for (let i = 0; i < arr.length; ++i) {
            if (arr[i][0] > arr[pivot][1]) {
                right.push(arr[i]);
                r = Math.max(r, arr[i][2]);
            } else {
                left.push(arr[i]);
                l = Math.max(l, arr[i][2]);
            }
        }

        res = Math.max(res, l+r);

        if (!left.length || !right.length) return;

        quick(left);
        quick(right);
    }

    quick(events);

    return res;
};

var maxTwoEvents_3 = function(events) {
    const arr = events.sort((a, b) => (a[1] - b[1]));

    const getLess = (i) => {
        let end = i - 1;
        let start = 0;
        let res = -1;
        while (start <= end) {
            const m = Math.floor((start + end) / 2);
            if (arr[m][1] < arr[i][0]) {
                res = m;
                start = m + 1;
            } else {
                end = m - 1;
            }
        }
        return res;
    };

    let res = 0;
    for (let i = 0; i < arr.length; ++i) {
        let r = arr[i][2];
        let j = getLess(i);
        while (j > -1) {
            r = Math.max(r, arr[j][2] + arr[i][2]);
            j -= 1;
        }
        res = Math.max(res, r);
    }

    return res;
};


var maxTwoEvents = function(events) {
    const arr = events.reduce((acc, [s, e, v]) => {
        acc.push([s, 0, v]);
        acc.push([e + 1, 1, v]);
        return acc;
    }, []).sort((a, b) => {
        if (a[0] === b[0]) return b[1] - a[1];e
        return a[0] - b[0];
    });

    let res = 0;
    let maxPrev = 0;
    for (let i = 0; i < arr.length; ++i) {
        if (arr[i][1] === 1) {
            maxPrev = Math.max(maxPrev, arr[i][2]);
        } else {
            res = Math.max(res, maxPrev + arr[i][2]);
        }
    }

    return res;
};


const test = () => {
    const params = [
        {
            input: [[1,3,2],[4,5,2],[2,4,3]],
            output: 4,
        },
        {
            input: [[1,3,2],[4,5,2],[1,5,5]],
            output: 5,
        },
        {
            input: [[1,5,3],[1,5,1],[6,6,5]],
            output: 8,
        },
        {
            input: [[2,1_000_000_000,1_000_000],[1,1,1_000_000]],
            output: 2000000,
        },

    ];

    params.forEach(({input, output}) => {
        const result = maxTwoEvents(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();