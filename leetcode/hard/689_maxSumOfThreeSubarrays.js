/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSumOfThreeSubarrays_0 = function(nums, k) {
    let res = [];
    let maxSum = -1;

    const cache = {};

    const getSum = (id) => {
        if (cache[id] != undefined) return cache[id];

        let sum = 0;
        for (let i = id; i < id + k; ++i) {
            sum += nums[i];
        }

        cache[id] = sum;

        return sum;
    };

    for (let i = 0; i < (nums.length - 2*k-(k-1)); ++i) {
        let sum = getSum(i);

        for (let i1 = i+k; i1 < (nums.length - k-(k-1)); ++i1) {
            let sum2 = sum + getSum(i1);

            for (let i2 = i1+k; i2 < (nums.length - (k-1)); ++i2) {
                let sum3 = sum2 + getSum(i2);

                if (sum3 > maxSum) {
                    maxSum = sum3;
                    res = [i, i1, i2]
                }
            }
        }
    }

    return res;
};

var maxSumOfThreeSubarrays_1 = function(nums, k) {
    const cache = new Array(nums.length).fill(0);
    for (let i = 0; i < k; ++i) {
        cache[0] += nums[i];
    }

    for (let i = 1; i < nums.length-(k-1); ++i) {
        cache[i] = cache[i-1];
        cache[i] -= nums[i-1];
        cache[i] += nums[i+k-1];
    }

    const postfix = new Array(nums.length).fill(0);
    postfix[nums.length-1] = [cache[nums.length-1], nums.length-1];
    for (let i = postfix.length - 2; i > -1; --i) {
        postfix[i] = (cache[i] >= postfix[i+1][0])
            ? [cache[i], i]
            : [...postfix[i+1]];
    }

    let res = [];
    let allMax = -1;
    let left = [cache[0], 0]

    for (let start = 0; start <= nums.length-3*k; ++start) {
        if (cache[start] > cache[0]) {
            left = [cache[start], start];
        }
        for (let i = start+k; i < nums.length - k - (k-1); ++i) {
            const middle = cache[i];
            const right = postfix[i+k];

            const sum = left[0] + middle + right[0];
            if (sum > allMax) {
                allMax = sum;
                res = [left[1], i, right[1]];
            }

            if (middle === postfix[i]) break;
        }
    }

    return res;
};

var maxSumOfThreeSubarrays = function(nums, k) {
    const sums = new Array(nums.length).fill(0);
    for (let i = 0; i < k; ++i) {
        sums[0] += nums[i];
    }
    for (let i = 1; i < nums.length-(k-1); ++i) {
        sums[i] = sums[i-1];
        sums[i] -= nums[i-1];
        sums[i] += nums[i+k-1];
    }

    const cache = new Map();

    const getMaxSums = (id, count) => {
        const key = [id, count].join('_');
        if (cache.has(key)) {
            return cache.get(key);
        }

        if (id >= nums.length - (k-1) || count > 2) {
            return 0;
        }

        const include = sums[id] + getMaxSums(id + k, count+1);
        const exclude = getMaxSums(id+1, count);

        const max = Math.max(include, exclude);
        cache.set(key, max);

        return max;
    }
    getMaxSums(0, 0);

    const res = [];
    let i = 0;
    while (i <= nums.length - (k-1) && res.length < 3) {
        const include = sums[i] + getMaxSums(i + k, res.length+1);
        const exclude = getMaxSums(i+1, res.length);

        if (include >= exclude) {
            res.push(i);
            i += k;
        } else {
            i += 1;
        }
    }
    return res;
};

const test = () => {
    const params = [
        {
            input: [[1,2,1,2,6,7,5,1], 2],
            output: [0,3,5],
        },
        {
            input: [[1,2,1,2,1,2,1,2,1], 2],
            output: [0,2,4],
        },
        {
            input: [[7,13,20,19,19,2,10,1,1,19], 3],
            output: [1,4,7],
        },
    ];

    params.forEach(({input, output}) => {
        const result = maxSumOfThreeSubarrays(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();