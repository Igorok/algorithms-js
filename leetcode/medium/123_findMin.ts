function findMin(nums: number[]): number {
    if (nums.length === 1 || nums[0] < nums.at(-1)) {
        return nums[0];
    }

    let res: number = nums[0];
    let start: number = 0;
    let end: number = nums.length - 1;

    while (start <= end) {
        const middle: number = Math.floor((start + end) / 2);

        if (middle > 0 && nums[middle - 1] > nums[middle]) {
            return nums[middle];
        }

        if (nums[middle] > nums.at(-1)) {
            start = middle + 1;
            continue;
        }
        if (nums[middle] < nums[0]) {
            end = middle - 1;
            continue;
        }
    }

    return res;
}

const test = () => {
    const params = [
        {
            input: {
                nums: [3, 4, 5, 1, 2],
            },
            output: 1,
        },
        {
            input: {
                nums: [4, 5, 6, 7, 0, 1, 2],
            },
            output: 0,
        },
        {
            input: {
                nums: [11, 13, 15, 17],
            },
            output: 11,
        },
        {
            input: {
                nums: [2, 3, 1],
            },
            output: 1,
        },
    ];

    params.forEach(({ input, output }) => {
        const { nums } = input;
        const result = findMin(nums);

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
