/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var resultsArray_1 = function(nums, k) {
    const isBlanced = (s, e) => {
        for (let i = s; i < e; ++i) {
            if (nums[i] !== nums[i + 1] - 1) {
                return false;
            }
        }
        return true;
    };

    const res = [];
    let start = 0;
    let end = k - 1;
    while (end !== nums.length) {
        if (isBlanced(start, end)) {
            res.push(nums[end]);
        } else {
            res.push(-1);
        }

        start += 1;
        end += 1;
    }

    return res;
};


var resultsArray = function(nums, k) {
    if (k === 1) return nums;

    const sortedArr = new Array(nums.length).fill(1);
    let notSorted = 0;

    const res = [];
    let start = 0;
    let end = k - 1;

    for (let i = 0; i < end; ++i) {
        const c = nums[i];
        const n = nums[i + 1];
        if (nums[i] + 1 !== nums[i + 1]) {
            sortedArr[i] = 0;
            notSorted += 1;
        }
    }


    while (end !== nums.length) {
        if (notSorted !== 0) {
            res.push(-1);
        } else {
            res.push(nums[end]);
        }

        if (sortedArr[start] === 0) {
            notSorted -= 1;
        }
        if (end + 1 !== nums.length && nums[end] + 1 !== nums[end + 1]) {
            notSorted += 1;
            sortedArr[end] = 0;
        }

        start += 1;
        end += 1;
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: [[1,2,3,4,3,2,5], 3],
            output: [3,4,-1,-1,-1],
        },

        {
            input: [[2,2,2,2,2], 4],
            output: [-1,-1],
        },
        {
            input: [[3,2,3,2,3,2], 2],
            output: [-1,3,-1,3,-1],
        },
        {
            input: [[1,3,4], 2],
            output: [-1,4],
        },
        {
            input: [[1,4], 1],
            output: [1,4],
        },
    ];

    params.forEach(({input, output}) => {
        const result = resultsArray(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();