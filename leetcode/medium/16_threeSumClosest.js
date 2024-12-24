/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    let diff = Number.MAX_SAFE_INTEGER;
    let res = 0;
    const data = nums.sort((a, b) => a - b);

    for (let i = 0; i < data.length - 2; ++i) {
        if (data[i] === data[i-1]) continue;

        let left = i + 1;
        let right = data.length - 1;

        while (left < right) {
            const sum = data[i] + data[left] + data[right];
            const d = Math.abs(target - sum);
            if (Math.abs(target - sum) < diff) {
                diff = d;
                res = sum;
            }
            if (sum === target) {
                return sum;
            } else if (sum > target) {
                right -= 1;
                while (data[right] === data[right+1] && left < right) {
                    right -= 1;
                }
            } else {
                left += 1;
                while (data[left] === data[left-1] && left < right) {
                    left += 1;
                }
            }
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: [[-1,2,1,-4], 1],
            output: 2,
        },
        {
            input: [[0,0,0], 1],
            output: 0,
        },
        {
            input: [[1,1,1,0], -100],
            output: 2,
        },
    ];

    params.forEach(({input, output}) => {
        const result = threeSumClosest(...input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();