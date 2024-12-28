/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    const res = [];
    const odd = matrix.length % 2;
    let endY = Math.ceil(matrix.length / 2);

    for (let i = 0; i < endY; ++i) {
        let n = matrix.length - i;
        let m = matrix[0].length - i;

        let y = i;
        let x = i;

        if (x >= m) break;

        while (x < m) {
            res.push(matrix[y][x]);
            x += 1;
        }
        x -= 1;
        y += 1;
        if ((i < endY - 1 && odd) || (i < endY && !odd)) {
            while (y < n) {
                res.push(matrix[y][x]);
                y += 1;
            }

            if (matrix[0].length - 2*i === 1) break;

            x -= 1;
            y -= 1;
            while (x >= i) {
                res.push(matrix[y][x]);
                x -= 1;
            }
            x += 1;
            y -= 1;
            while (y > i) {
                res.push(matrix[y][x]);
                y -= 1;
            }
        }
    }

    return res;
};

/*


[1,2,3,4,8,12,16,20,24,23,22,21,17,13,9,5,6,7,11,15,19,18,14,10]
[1,2,3,4,8,12,16,20,24,23,22,21,17,13,9,5,6,7,11,15,19,18,14,10,14]



[ 1, 2, 3, 4],
[ 5, 6, 7, 8],
[ 9,10,11,12],
[13,14,15,16],
[17,18,19,20],
[21,22,23,24]


















*/

const test = () => {
    const params = [
        {
            input: [[1,2,3],[4,5,6],[7,8,9]],
            output: [1,2,3,6,9,8,7,4,5],
        },
        {
            input: [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
            output: [1,2,3,4,8,12,11,10,9,5,6,7],
        },
        {
            input: [[3],[2]],
            output: [3, 2],
        },
        {
            input: [[1, 2]],
            output: [1, 2],
        },
        {
            input: [[1, 2], [3, 4]],
            output: [1, 2, 4, 3],
        },
        {
            input: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            output: [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10],
        },
        {
            input: [[1], [2], [3]],
            output: [1, 2, 3],
        },
        {
            input: [[1, 2], [3, 4], [5, 6]],
            output: [1, 2, 4, 6, 5, 3],
        },
        {
            input: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],
            output: [1,2,3,6,9,12,15,14,13,10,7,4,5,8,11],
        },
        {
            input: [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]],
            output: [1,2,3,4,8,12,16,20,24,23,22,21,17,13,9,5,6,7,11,15,19,18,14,10],
        },


    ];

    params.forEach(({input, output}) => {
        const result = spiralOrder(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();