/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    if (intervals?.length < 2) {
        return intervals;
    }

    const res = [];

    const data = intervals.sort((a,b) => {
        if (a[0] === b[0]) {
            return a[1] - b[1];
        }
        return a[0] - b[0];
    });
    let interval = data[0];

    for (let i = 1; i < data.length; ++i) {
        const [start, end] = data[i];
        if (start <= interval[1]) {
            interval[0] = Math.min(interval[0], start);
            interval[1] = Math.max(interval[1], end);
        } else {
            res.push(interval);
            interval = [start, end];
        }
        if (i === data.length - 1) {
            res.push(interval);
        }
    }

    return res;
};


const test = () => {
    const params = [
        {
            input: [[1,3],[2,6],[8,10],[15,18]],
            output: [[1,6],[8,10],[15,18]],
        },
        {
            input: [[1,4],[4,5]],
            output: [[1,5]],
        },
        {
            input: [[1,3]],
            output: [[1,3]],
        },
        {
            input: [[2,3],[4,5],[6,7],[8,9],[1,10]],
            output: [[1,10]],
        },


    ];

    params.forEach(({input, output}) => {
        const result = merge(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();