/**
 * @param {number[]} arr
 * @param {number[][]} mat
 * @return {number}
 */
var firstCompleteIndex = function(arr, mat) {
    const nums = new Array(mat.length * mat[0].length + 1);
    const rows = new Array(mat.length).fill(0);
    const colls = new Array(mat[0].length).fill(0);

    for (let i = 0; i < mat.length; ++i) {
        for (let j = 0; j < mat[0].length; ++j) {
            const num = mat[i][j];
            nums[num] = [i, j];
        }
    }

    for (let i = 0; i < arr.length; ++i) {
        const [row, coll] = nums[arr[i]];
        rows[row] += 1;
        colls[coll] += 1;
        if (rows[row] === mat[0].length || colls[coll] === mat.length) {
            return i
        }
    }

    return 0;
};

/*

[1,4,5,2,6,3],

[
[4,3,5],
[1,2,6]
]



*/


const test = () => {
    const params = [
        {
            input: [[1,3,4,2], [[1,4],[2,3]]],
            output: 2,
        },
        {
            input: [[2,8,7,4,1,3,5,6,9], [[3,2,5],[1,4,6],[8,7,9]]],
            output: 3,
        },
        {
            input: [[1,4,5,2,6,3], [[4,3,5],[1,2,6]]],
            output: 1,
        },
    ];

    for (const { input, output } of params) {
        const result = firstCompleteIndex(...input);
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
