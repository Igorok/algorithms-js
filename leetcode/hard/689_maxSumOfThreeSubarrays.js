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
    let res = [];

    const cache = new Array(nums.length).fill(0);

    for (let i = 0; i < k; ++i) {
        cache[0] += nums[i];
    }

    for (let i = 1; i < (nums.length-(k-1)); ++i) {
        cache[i] = cache[i-1];
        cache[i] -= nums[i-1];
        cache[i] += nums[i+k-1];
    }

    let start = 0;
    let end = nums.length - k;
    let startMax = [-1, -1];
    let endMax = [-1, -1];
    let allMax = -1;

    while (start + 2*k <= end) {
        if (cache[start] > startMax[0]) {
            startMax = [cache[start], start];
        }
        const tmp = endMax[0];
        if (cache[end] >= endMax[0]) {
            endMax = [cache[end], end];
        }

        let middleMax = [-1, -1];
        for (let i = start + k; i <= end - k; ++i) {
            if (cache[i] > middleMax[0]) {
                middleMax = [cache[i], i];
            }
        }

        const sum = startMax[0] + endMax[0] + middleMax[0];
        if (sum === allMax  && tmp === endMax[0] && res[2] !== endMax[1]) {
            res[2] = endMax[1];
        }
        if (sum > allMax) {
            allMax = sum;
            res = [
                startMax[1], middleMax[1], endMax[1],
            ];
        }

        start += 1;
        end -= 1;
    }


    return res;
};


var maxSumOfThreeSubarrays = function(nums, k) {
    const cache = new Array(nums.length).fill(0);
    for (let i = 0; i < k; ++i) {
        cache[0] += nums[i];
    }

    for (let i = 1; i < nums.length-(k-1); ++i) {
        cache[i] = cache[i-1];
        cache[i] -= nums[i-1];
        cache[i] += nums[i+k-1];
    }

    const prefix = [[cache[0], 0]];
    for (let i = 1; i < nums.length-(k-1); ++i) {
        prefix[i] = cache[i] > prefix[i-1][0]
            ? [cache[i], i]
            : [...prefix[i-1]];
    }

    const postfix = new Array(nums.length).fill(0);
    postfix[nums.length-1] = [cache[nums.length-1], nums.length-1];
    for (let i = postfix.length - 2; i > -1; --i) {
        postfix[i] = (cache[i] >= postfix[i+1][0])
            ? [cache[i], i]
            : [...postfix[i+1]];
    }

    let start = 0;
    let res = [];
    let allMax = -1;

    while (start + 3*k <= nums.length) {
        const left = prefix[start];
        for (let i = start+k; i < nums.length - k - (k-1); ++i) {
            const middle = cache[i];
            const right = postfix[i+k];

            const sum = left[0] + middle + right[0];
            if (sum > allMax) {
                allMax = sum;
                res = [left[1], i, right[1]];
            }
        }
        start += 1;
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