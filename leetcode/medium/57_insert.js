/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function(intervals, newInterval) {
    if (!intervals.length) {
        return [newInterval];
    }
    const res = [];
    let inserted = false;

    if (newInterval[0] <= intervals[0][0]) {
        inserted = true;
        if (newInterval[1] >= intervals[0][0]) {
            res.push([
                Math.min(newInterval[0], intervals[0][0]),
                Math.max(newInterval[1], intervals[0][1]),
            ]);
        } else {
            res.push(newInterval);
        }
    }

    for (let i = 0; i < intervals.length; ++i) {
        let interval = intervals[i];
        if (!inserted) {
            if (
                (interval[0] >= newInterval[0] && interval[0] <= newInterval[1]) ||
                (newInterval[0] >= interval[0] && newInterval[0] <= interval[1])
            ) {
                inserted = true;
                interval = [
                    Math.min(newInterval[0], interval[0]),
                    Math.max(newInterval[1], interval[1]),
                ];
            } else if (interval[0] >= newInterval[0]) {
                inserted = true;
                res.push(newInterval);
            }

        }

        if (!res.length) {
            res.push(interval);
            continue;
        }
        const last = res.at(-1);
        if (last[1] >= interval[0]) {
            res.pop();
            res.push([
                last[0],
                Math.max(last[1], interval[1])
            ]);
        } else {
            res.push(interval);
        }
    }

    if (!inserted) {
        res.push(newInterval);
    }


    return res;
};

const test = () => {
    const params = [
        {
            input: [[[1,3],[6,9]], [2,5]],
            output: [[1,5],[6,9]],
        },
        {
            input: [[[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]],
            output: [[1,2],[3,10],[12,16]],
        },
        {
            input: [[[1,3],[1,3],[1,2],[1,2],[1,3],[1,3],[1,3],[6,9]], [2,5]],
            output: [[1,5],[6,9]],
        },
        {
            input: [[[3,5],[12,15]], [6,6]],
            output: [[3,5],[6,6],[12,15]],
        },
    ];

    for (const { input, output } of params) {
        const result = insert(...input);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${JSON.stringify(output)}
            RESULT: ${JSON.stringify(result)}`;

        if (JSON.stringify(result) === JSON.stringify(output)) {
            console.log(
                `SUCCESS: ${message}`,
            );
        } else {
            console.error(`ERROR: ${message}`);
        }
    }
};

test();
