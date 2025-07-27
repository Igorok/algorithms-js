function countHillValley(nums: number[]): number {
    let res: number = 0;
    const left: number[] = new Array(nums.length).fill(0);
    const right: number[] = new Array(nums.length).fill(0);

    left[0] = -1;
    for (let i: number = 1; i < left.length; ++i) {
        left[i] = (nums[i] !== nums[i-1]) ? nums[i-1] : left[i-1];
    }

    right[right.length - 1] = -1;
    for (let i: number = right.length - 2; i > -1; --i) {
        right[i] = (nums[i] !== nums[i+1]) ? nums[i+1] : right[i+1];
    }

    for (let i: number = 1; i < nums.length - 1; ++i) {
        if (nums[i] === nums[i-1]) {
            continue;
        }
        if (left[i] === -1 || right[i] === -1) {
            continue;
        }

        if (
            (nums[i] > left[i] && nums[i] > right[i]) ||
            (nums[i] < left[i] && nums[i] < right[i])
        ) {
            res += 1;
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                nums: [2,4,1,1,6,5],
            },
            output: 3,
        },
        {
            input: {
                nums: [6,6,5,5,4,1],
            },
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums } = input;
        const result = countHillValley(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();