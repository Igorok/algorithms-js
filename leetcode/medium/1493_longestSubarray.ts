function longestSubarray(nums: number[]): number {
    let res: number = 0

    let left: number = 0;
    let ones: number = 0;
    let zeros: number = 0;

    for (let right: number = 0; right < nums.length; ++right) {
        while (zeros > 1) {
            if (nums[left] === 0) {
                zeros -= 1;
            } else {
                ones -= 1;
            }
            left += 1;
        }

        if (nums[right] === 0) {
            zeros += 1;
        } else {
            ones += 1;
        }

        const o: number = zeros > 0 ? ones : ones - 1;

        res = Math.max(res, o);
    }

    return res;
};

const test = () => {
    const params = [

        {
            input: {
                nums: [1,1,1]
            },
            output: 2,
        },
        {
            input: {
                nums: [1,1,0,1],
            },
            output: 3,
        },
        {
            input: {
                nums: [0,1,1,1,0,1,1,0,1]
            },
            output: 5,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums } = input;

        const result = longestSubarray(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();
