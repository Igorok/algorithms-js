/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    const data = nums.sort((a, b) => a - b);
    const res = [];

    const twoSum = (start, arr) => {
        const first = arr[0] + arr[1];
        let left = start;
        let right = data.length - 1;


        while (left < right) {
            const sum = first + data[left] + data[right];
            if (sum === target) {
                res.push([...arr, data[left], data[right]]);
                left += 1;
                while (data[left] === data[left-1] && left < right) {
                    left += 1;
                }
            } else if (sum < target) {
                left += 1;
                while (data[left] === data[left-1] && left < right) {
                    left += 1;
                }
            } else {
                right -= 1;
                while (data[right] === data[right+1] && left < right) {
                    right -= 1;
                }
            }
        }
    }

    const threeSum = (start, val) => {
        for (let i = start; i < data.length-2; ++i) {
            if (data[i] === data[i-1] && i > start) {
                continue;
            }
            twoSum(i+1, [val, data[i]]);
        }
    }

    for (let i = 0; i < data.length-3; ++i) {
        if (data[i] === data[i-1]) {
            continue;
        }
        threeSum(i+1, data[i])
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: [[1,0,-1,0,-2,2], 0],
            output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]],
        },
        {
            input: [[2,2,2,2,2], 8],
            output: [[2,2,2,2]],
        },
        {
            input: [[-2,-1,-1,1,1,2,2], 0],
            output: [[-2,-1,1,2],[-1,-1,1,1]],
        },
    ];

    params.forEach(({input, output}) => {
        const result = fourSum(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();