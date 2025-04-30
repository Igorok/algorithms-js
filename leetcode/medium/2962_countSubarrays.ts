function countSubarrays(nums: number[], k: number): number {
    const maxVal: number = Math.max(...nums);

    let res: number = 0;
    let left: number = 0;
    let count: number = 0;
    for (let right: number = 0; right < nums.length; ++right) {
        if (nums[right] === maxVal) {
            count += 1;
        }

        while (count >= k) {
            res += (nums.length - right);
            if (nums[left] === maxVal) {
                count -= 1;
            }
            left += 1;
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: { nums: [1,3,2,3,3], k: 2 },
            output: 6,
        },
        {
            input: { nums: [1,4,2,1], k: 3 },
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums, k } = input;

        const result = countSubarrays(nums, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();