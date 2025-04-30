/**
 * Calculate the number of valid arrays with given differences and boundary values
 * @param differences Array of differences between consecutive elements
 * @param lower Lower bound for array elements
 * @param upper Upper bound for array elements
 * @returns Number of possible arrays that satisfy the differences and boundaries
 */
function numberOfArrays_ai(differences: number[], lower: number, upper: number): number {
    let min = 0, max = 0, curr = 0;

    // Calculate cumulative differences and track min/max
    for (const diff of differences) {
        curr += diff;
        min = Math.min(min, curr);
        max = Math.max(max, curr);
    }

    // For any starting value x, the sequence will be:
    // x, x+d[0], x+d[0]+d[1], ...
    // We need all these values to be between lower and upper

    // For the minimum value (lower bound of x):
    // x + min_cumulative >= lower
    // x >= lower - min_cumulative
    const minStart = lower - min;

    // For the maximum value (upper bound of x):
    // x + max_cumulative <= upper
    // x <= upper - max_cumulative
    const maxStart = upper - max;

    // The actual starting value must be between lower and upper
    const validStart = Math.max(lower, minStart);
    const validEnd = Math.min(upper, maxStart);

    return validStart <= validEnd ? validEnd - validStart + 1 : 0;
}


function numberOfArrays_0(differences: number[], lower: number, upper: number): number {
    let res: number = 0;

    const getNext = (id: number, val: number, memo: number[]) => {
        if (id === differences.length) {
            res += 1;
            return;
        }
        const r: number = val + differences[id];
        if (r < lower || r > upper) {
            return;
        }
        getNext(id + 1, r, [...memo, r]);
    };

    for (let i: number = lower; i <= upper; ++i) {
        const r: number = i + differences[0];
        if (r < lower || r > upper) {
            continue;
        }
        getNext(1, r, [i]);
    }

    return res;
};

function numberOfArrays(differences: number[], lower: number, upper: number): number {
    let minDiff: number = 0;
    let maxDiff: number = 0;
    let currDiff: number = 0;

    for (let i: number = 0; i < differences.length; ++i) {
        currDiff += differences[i];
        minDiff = Math.min(minDiff, currDiff);
        maxDiff = Math.max(maxDiff, currDiff);
    }

    const start: number = minDiff < 0 ? lower - minDiff : lower + minDiff;
    const end: number = maxDiff < 0 ? upper + maxDiff : upper - maxDiff;

    if (start > end) {
        return 0;
    }

    return end - start + 1;
};

/*

differences[i] = hidden[i + 1] - hidden[i]

differences: [1,-3,4], lower: 1, upper: 6,
[3, 4, 1, 5]
[4, 5, 2, 6]

1, 6
1   [1, 2], [2, 3], [3, 4], [4, 5], [5, 6];
-3  [1, 2, -1], [2, 3, 0], [3, 4, 1], [4, 5, 2], [5, 6, 3]
4   [3, 4, 1, 5], [4, 5, 2, 6], [5, 6, 3, 7]
[3, 4, 1, 5], [4, 5, 2, 6]

---

differences: [3,-4,5,1,-2], lower: -4, upper: 5

[    3,  -4, 5,  1,  -2]
[x0, x1, x2, x3, x4, x5]
x,  x+3  x-1 x+4 x+5 x+3
minDiff = -1
maxDiff = 5

start = minDiff < 0 ? lower - minDiff : lower + minDiff;
end = maxDiff < 0 ? upper + maxDiff : upper - maxDiff;

---
[10, 10] 1, 1
    [10, 10]
x x+10 x+20
s = 1 - 10
e = 1 - 20
s > e

 */

const test = () => {
    const params = [
        {
            input: {
                differences: [1,-3,4], lower: 1, upper: 6,
            },
            output: 2,
        },
        {
            input: {
                differences: [3,-4,5,1,-2], lower: -4, upper: 5
            },
            output: 4,
        },
        {
            input: {
                differences: [4,-7,2], lower: 3, upper: 6
            },
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const { differences, lower, upper } = input;

        const result = numberOfArrays(differences, lower, upper);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();
