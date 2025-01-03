/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    const res = [];
    const used = new Array(nums.length).fill(0);

    const rec = (arr, usedLength) => {
        if (usedLength === nums.length) {
            res.push(arr);
        }

        for (let i = 0; i < nums.length; ++i) {
            if (!used[i]) {
                used[i] = 1;
                arr.push(nums[i]);

                rec([...arr], usedLength + 1);

                used[i] = 0;
                arr.pop();
            }
        }
    };

    rec([], 0);

    return res;
};

const test = () => {
    const params = [
        {
            input: [1,2,3],
            output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]],
        },
        {
            input: [0,1],
            output: [[0,1],[1,0]],
        },
        {
            input: [1],
            output: [[1]],
        },
    ];

    params.forEach(({input, output}) => {
        const result = permute(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();