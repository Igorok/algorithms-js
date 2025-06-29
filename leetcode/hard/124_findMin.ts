function findMin(nums: number[]): number {
    if (nums.length === 0 || nums[0] < nums.at(-1)) {
        return nums[0];
    }

    let left: number = 0;
    let right: number = nums.length - 1;

    while (left <= right) {
        const middle: number = Math.floor((left + right) / 2);
        if (middle > 0 && nums[middle - 1] > nums[middle]) {
            return nums[middle];
        }
        if (nums[middle] > nums[right]) {
            left = middle + 1;
            continue;
        }
        if (nums[middle] < nums[left]) {
            right = middle;
            left += 1;
            continue;
        }
        right -= 1;
    }

    return nums[left];
}

const test = () => {
    const params = [
        {
            input: {
                nums: [1, 3, 5],
            },
            output: 1,
        },
        {
            input: {
                nums: [2, 2, 2, 0, 1],
            },
            output: 0,
        },
        {
            input: {
                nums: [2, 2, 2, 0, 1, 1, 1, 1, 1, 1],
            },
            output: 0,
        },
        {
            input: {
                nums: [1, 2, 2, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            },
            output: 0,
        },
        {
            input: {
                nums: [2, 2, 2, 3, 3, 3, 0, 1, 1, 1, 2],
            },
            output: 0,
        },
        {
            input: {
                nums: [2, 2, 3, 3, 0, 1, 1, 2],
            },
            output: 0,
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
