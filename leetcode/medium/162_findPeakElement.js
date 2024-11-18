/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
    if (nums.length === 1) return 0;

    let start = 0;
    let end = nums.length - 1;

    while (start <= end) {
        const middle = Math.floor((start + end) / 2);

        const lVal = middle > 0 ? nums[middle - 1] : nums[middle] - 1;
        const rVal = middle < (nums.length - 1) ? nums[middle + 1] : nums[middle] - 1;
        if (nums[middle] > lVal && nums[middle] > rVal) {
            return middle;
        }
        if (lVal > nums[middle]) {
            end = middle - 1;
        } else if (rVal > nums[middle]) {
            start = middle + 1;
        }
    }

    return 0;
};

/*

[1,2,1,2,3,4,5]
[5,4,3,2,1]
[5,4,10,11,12]




*/

const test = () => {
    const params = [
        {
            input: [1,2,3,1],
            output: 2,
        },
        {
            input: [1,2,1,3,5,6,4],
            output: 5,
        },
    ];

    for (const { input, output } of params) {
        const result = findPeakElement(input);
        const message = `
            INPUT: ${input}
            OUTPUT: ${output}
            RESULT: ${result}
            `;

        if (result === output) {
            console.log(
                'SUCCESS: \n', message,
            );
        } else {
            console.error('ERROR: \n', message);
        }
    }
};

test();
