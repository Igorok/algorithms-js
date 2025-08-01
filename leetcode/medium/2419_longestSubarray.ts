function longestSubarray(nums: number[]): number {
    let maxVal: number = -1;
    for (const num of nums) {
        maxVal = Math.max(maxVal, num);
    }

    let res: number = 1;

    let cnt: number = 0;
    for (let right: number = 0; right < nums.length; ++right) {
        if (nums[right] === maxVal) {
            cnt += 1;
        }
        if (nums[right] !== maxVal && cnt !== 0) {
            res = Math.max(res, cnt);
            cnt = 0;
        }
    }

    res = Math.max(res, cnt);
    cnt = 0;

    return res;
};


const test = () => {
    const params = [
        {
            input: {
                nums: [1,2,3,3,2,2]
            },
            output: 2,
        },
        {
            input: {
                nums: [1,2,3,4]
            },
            output: 1,
        },
    ];

    params.forEach(({ input, output }) => {
        const { nums } = input;
        const result = longestSubarray(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output)
                ? "SUCCESS "
                : "ERROR ",
            "input",
            JSON.stringify(input),
            "output",
            output,
            "result",
            result,
        );
    });
};

test();
