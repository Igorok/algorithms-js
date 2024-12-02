/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function(intervals) {
    const data = intervals.sort((a, b) => {
        if (a[1] === b[1]) return a[0] - b[0];
        return a[1] - b[1];
    });

    const notOverlap = [data[0]];
    const intLength = intervals.length;
    let notLength = 1;
    for (let i = 1; i < intLength; ++i) {
        if (data[i][0] >= notOverlap[notLength - 1][1]) {
            notOverlap.push(data[i]);
            notLength += 1;
        }
    }

    return intLength - notLength;
};

/*

[1,2],[2,3],[3,4],[1,3]

1 2 3 4
1 2
  2 3
1   3
    3 4



[1,2],[2,3],[3,4],[1,3]

1 1 2 3
2 3 3 4

o - 1,1; 2
c - 2; 1
over - 1
2; 1,1,2; 3
3; 2,3; 2
over - 1
3; 1,1,2,3; 4
4; 2,3,3,4; 4



[[0,2],[1,3],[2,4],[3,5],[4,6]]

0 1 2 3 4
2 3 4 5 6

0 1 2 3 4 5 6
0   2
  1   3
    2   4
      3   5
        4   6



*/


const test = () => {
    const params = [
        {
            input: [[1,2],[2,3],[3,4],[1,3]],
            output: 1,
        },

        {
            input: [[1,2],[1,2],[1,2]],
            output: 2,
        },
        {
            input: [[1,2],[2,3]],
            output: 0,
        },
        {
            input: [[0,2],[1,3],[2,4],[3,5],[4,6]],
            output: 2,
        },
    ];

    params.forEach(({input, output}) => {
        const result = eraseOverlapIntervals(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();