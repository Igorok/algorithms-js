function singleNonDuplicate(nums: number[]): number {
    if (nums.length === 1) {
        return nums[0];
    }

    let start: number = 0;
    let end: number = nums.length - 1;

    while (start <= end) {
        const middle: number = Math.floor((start + end) / 2);
        if (
            (middle === 0 && nums[middle] !== nums[middle + 1]) ||
            (middle === nums.length - 1 && nums[middle] !== nums[middle-1]) ||
            (middle > 0 && middle < nums.length - 1 && nums[middle] !== nums[middle - 1] && nums[middle] !== nums[middle + 1])
        ) {
            return nums[middle];
        }

        if (middle < nums.length-1 && nums[middle] === nums[middle+1]) {
            const leftSize: number = middle - start;
            if (leftSize % 2) {
                end = middle - 1;
            } else {
                start = middle + 2;
            }
        }

        if (middle > 0 && nums[middle] === nums[middle - 1]) {
            const leftSize: number = middle - start + 1;
            if (leftSize % 2) {
                end = middle - 2;
            } else {
                start = middle + 1;
            }
        }
    }

    return 0;
};

const test = () => {
    const params = [
        {
            input: {
                nums: [1,1,2,3,3,4,4,8,8],
            },
            output: 2,
        },
        {
            input: {
                nums: [3,3,7,7,10,11,11]
            },
            output: 10,
        },
    ];

    params.forEach(({ input, output }) => {
        const { nums } = input;
        const result = singleNonDuplicate(nums);

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
