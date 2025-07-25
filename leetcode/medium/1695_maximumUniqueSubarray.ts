function maximumUniqueSubarray(nums: number[]): number {
    let left: number = 0;
    let sum: number = nums[0];
    let res: number = sum;
    const count: Map<number, number> = new Map();
    count.set(nums[0], 1);

    for (let right: number = 1; right < nums.length; ++right) {
        while ((count.get(nums[right]) || 0) > 0) {
            const cnt: number = (count.get(nums[left]) || 0) - 1;
            if (cnt === 0) {
                count.delete(nums[left]);
            } else {
                count.set(nums[left], cnt);
            }
            sum -= nums[left];
            left += 1;
        }
        sum += nums[right];
        count.set(nums[right], 1);

        res = Math.max(res, sum);
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                nums: [10000],
            },
            output: 10000,
        },
        {
            input: {
                nums: [4,2,4,5,6],
            },
            output: 17,
        },

        {
            input: {
                nums: [5,2,1,2,5,2,1,2,5],
            },
            output: 8,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums } = input;
        const result = maximumUniqueSubarray(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();