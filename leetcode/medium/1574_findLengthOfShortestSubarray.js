/**
 * @param {number[]} arr
 * @return {number}
 */
var findLengthOfShortestSubarray_1 = function(arr) {
    let res = arr.length;

    let id = 0;
    while (id < arr.length) {
        let past = id;
        let start = end = -1;

        for (let i = id + 1; i < arr.length; ++i) {
            if (arr[i] >= arr[past]) {
                past = i;
            }

            if (arr[i] < arr[past]) {
                if (start === -1) {
                    start = i;
                    end = i;
                } else {
                    end = i;
                }
                past = start - 1;
            }
        }

        console.log(
            'id', id,
            'start', start,
            'end', end,
        );

        if (start === -1 && id === 0) {
            return 0;
        }
        if (start === -1) {
            res = Math.min(res, id);
        }
        if (id === 0) {
            res = Math.min(res, end - start + 1);
        }

        id += 1;
    }

    return res;
};


var findLengthOfShortestSubarray = function(arr) {
    let firstEnd = 0;
    let secondStart = arr.length - 1;

    for (let i = 1; i < arr.length; ++i) {
        if (arr[i- 1] <= arr[i]) {
            firstEnd = i;
        } else {
            break;
        }
    }

    for (let i = arr.length - 2; i > -1; --i) {
        if (arr[i + 1] >= arr[i]) {
            secondStart = i;
        } else {
            break;
        }
    }

    console.log(
        'firstEnd', firstEnd,
        'secondStart', secondStart,
    );

    if (firstEnd === arr.length - 1) {
        return 0;
    }

    let res = Math.min(
        arr.length - firstEnd - 1,
        secondStart,
    );

    const binSearch = (s, e, num) => {
        let start = s;
        let end = e;

        let id = -1;

        while (start <= end) {
            const m = Math.floor((start + end) / 2);
            if (arr[m] >= num) {
                id = m;
                end = m -1;
            } else {
                start = m + 1
            }
        }

        return id;
    };

    for (let i = firstEnd; i > -1; --i) {
        const middle = arr[i];
        const me = binSearch(secondStart, arr.length - 1, middle);

        if (me !== -1) {
            const l1 = i + 1;
            const l2 = arr.length - me;

            const diff = arr.length - l1 - l2;
            if (diff < res) {
                res = diff;
            }
        }
    }


    return res;
};

/*
1,2,3, 1,4,1, 5,6,7

1,2,3,
1

1,2,3, 4
1

1,2,3, 4, 1
1
?
1,4,1


*/

const test = () => {
    const params = [
        {
            input: [1,2,3,10,4,2,3,5],
            output: 3,
        },
        {
            input: [5,4,3,2,1],
            output: 4,
        },
        {
            input: [1,2,3],
            output: 0,
        },
        {
            input: [1,2,3, 1, 4, 1, 5,6,7],
            output: 3,
        },
        {
            input: [10, 9, 8, 1,2,3,4,5,6],
            output: 3,
        },
        {
            input: [1,2,3,3,10,1,3,3,5],
            output: 2,
        },
    ];

    for (const { input, output } of params) {
        const result = findLengthOfShortestSubarray(input);
        const message = `
            INPUT: ${JSON.stringify(input)}
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
