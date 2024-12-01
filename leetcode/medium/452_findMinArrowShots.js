/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
    const data = points.sort((a, b) => {
        if (a[1]==b[1]) return a[0]-b[0];
        return a[1]-b[1];
    });

    let res = 0;
    let start = 0;

    while (start < data.length) {
        let end = start;
        while (data[end] && data[end][0] <= data[start][1]) {
            end += 1;
        }
        res += 1;
        start = end;
    }

    return res;
};

/*

[1,6] [2,8]  [7,12] [10,16]


*/

const test = () => {
    const params = [
        {
            input: [[10,16],[2,8],[1,6],[7,12]],
            output: 2,
        },

        {
            input: [[1,2],[3,4],[5,6],[7,8]],
            output: 4,
        },
        {
            input: [[1,2],[2,3],[3,4],[4,5]],
            output: 2,
        },

        {
            input: [[1,6],[7,8],[2,12],[10,16],],
            output: 3,
        },
    ];

    params.forEach(({input, output}) => {
        const result = findMinArrowShots(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();