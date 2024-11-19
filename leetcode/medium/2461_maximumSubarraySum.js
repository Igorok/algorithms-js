/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximumSubarraySum_1 = function(nums, k) {
    const visited = new Map();
    let sum = 0;
    let res = 0;

    for (let i = 0; i < k; ++i) {
        let count = (visited.get(nums[i]) || 0) + 1;
        visited.set(nums[i], count);
        sum += nums[i];
    }

    if (visited.size === k) {
        res = Math.max(res, sum);
    }

    for (let i = k; i < nums.length; ++i) {
        const newCount = (visited.get(nums[i]) || 0) + 1;
        visited.set(nums[i], newCount);
        sum += nums[i];

        const prevCount = visited.get(nums[i - k]) - 1;
        sum -= nums[i - k];
        if (prevCount === 0) {
            visited.delete(nums[i - k]);
        } else {
            visited.set(nums[i - k], prevCount);
        }

        if (visited.size === k) {
            res = Math.max(res, sum);
        }
    }

    return res;
};

/*

1, 2, 3, 3, 3, 4, 5, 6
6
12
15
*/

var maximumSubarraySum = function(nums, k) {
    const visitedIds = new Map();
    let sum = 0;
    let res = 0;

    let start = 0;
    for (let i = 0; i < nums.length; ++i) {
        if (k === 1) {
            res = Math.max(res, nums[i]);
            continue;
        }

        sum += nums[i];
        const visitedId = visitedIds.get(nums[i]) === undefined ? -1 : visitedIds.get(nums[i]);

        if (visitedId !== -1) {
            for (let j = start; j <= visitedId; ++j) {
                sum -= nums[j];
                visitedIds.delete(nums[j]);
            }
            start = visitedId + 1;

            if (start === i) {
                visitedIds.set(nums[i], i);
                continue;
            };
        }
        visitedIds.set(nums[i], i);

        if (i - start === k) {
            sum -= nums[start];
            visitedIds.delete(nums[start]);
            start += 1;
        }

        if (visitedIds.size === k) {
            res = Math.max(res, sum);
        }
    }

    return res;
};


const test = () => {
    const params = [
        {
            input: [[1,5,4,2,9,9,9], 3],
            output: 15,
        },
        {
            input: [[4,4,4], 3],
            output: 0,
        },
        {
            input: [[9,9,9,1,2,3], 3],
            output: 12,
        },
        {
            input: [[1, 2, 3, 3, 3, 4, 5, 6], 3],
            output: 15,
        },
        {
            input: [[1, 2, 3, 4, 5, 6], 1],
            output: 6,
        },
        {
            input: [[1,1,2], 2],
            output: 3,
        },
    ];


    for (const { input, output } of params) {
        const result = maximumSubarraySum(...input);
        const message = `
            INPUT: ${JSON.stringify(input)}
            OUTPUT: ${output}
            RESULT: ${result}
            `;

        if (JSON.stringify(result) === JSON.stringify(output)) {
            console.log(
                'SUCCESS: \n', message,
            );
        } else {
            console.error('ERROR: \n', message);
        }
    }
};

test();
