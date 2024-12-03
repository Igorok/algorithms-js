/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate_1 = function(nums, k) {
    const left = nums.slice(nums.length - k, nums.length);
    const right = nums.slice(0, nums.length - k);
    return left.concat(right);
};

var rotate_2 = function(nums, k) {
    const rem = k % nums.length;
    let start = nums.length - rem;
    let end = 0;

    while (start < nums.length) {
        const tmp = nums[start];

        for (i = start; i > end; --i) {
            nums[i] = nums[i - 1];
        }

        nums[end] = tmp;

        start += 1;
        end += 1;
    }

    return nums;
};

var rotate_3 = function(nums, k) {
    let rem = k % nums.length;
    while (rem) {
        const v = nums.pop();
        nums.unshift(v);
        rem -= 1;
    }
    return nums;
};

var rotate_4 = function(nums, k) {
    let rem = k % nums.length;
    if (rem) {
        const l = nums.length;
        const right = nums.slice(nums.length - rem, nums.length);
        nums.splice(0, 0, ...right);
        nums.length = l;
    }
    return nums;
};

var rotate = function(nums, k) {
    const reverse = (start, end) => {
        while (start < end) {
            const tmp = nums[start];
            nums[start] = nums[end];
            nums[end] = tmp;
            start += 1;
            end -= 1;
        }
    };

    let rem = k % nums.length;
    if (rem) {
        reverse(0, nums.length - 1);
        reverse(0, rem - 1);
        reverse(rem, nums.length - 1);
    }
    return nums;
};

const test = () => {
    const params = [
        {
            input: [[1,2,3,4,5,6,7], 3],
            output: [5,6,7,1,2,3,4],
        },
        {
            input: [[-1,-100,3,99], 2],
            output: [3,99,-1,-100],
        },
        {
            input: [[-1], 2],
            output: [-1],
        },
        {
            input: [[1,2], 5],
            output: [2,1],
        },
    ];

    params.forEach(({input, output}) => {
        const result = rotate(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();