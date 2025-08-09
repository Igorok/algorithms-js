function countRangeSum_0(nums: number[], lower: number, upper: number): number {
    let res: number = 0;

    const prefixSum: number[] = new Array(nums.length).fill(0);
    prefixSum[0] = nums[0];

    for (let i: number = 1; i < nums.length; ++i) {
        prefixSum[i] = nums[i] + prefixSum[i-1];
    }

    for (let i: number = 0; i < nums.length; ++i) {
        for (let j: number = i; j < nums.length; ++j) {
            const s: number = prefixSum[j] - (i > 0 ? prefixSum[i-1] : 0);

            if (s >= lower && s <= upper) {
                res += 1;
            }
        }
    }

    return res;
};

function countRangeSum(nums: number[], lower: number, upper: number): number {
    let res: number = 0;

    const prefixSum: number[] = new Array(nums.length).fill(0);
    prefixSum[0] = nums[0];

    for (let i: number = 1; i < nums.length; ++i) {
        prefixSum[i] = nums[i] + prefixSum[i-1];
    }

    console.log('prefixSum', prefixSum);

    for (let i: number = 0; i < nums.length; ++i) {
        for (let j: number = i; j < nums.length; ++j) {
            const s: number = prefixSum[j] - (i > 0 ? prefixSum[i-1] : 0);

            if (s >= lower && s <= upper) {
                res += 1;
            }
        }
    }

    return res;
};

/*
4+3+2+0+3+3+1+1
nums: [1, 1, 1, -10, 2, -2, 2, 10], lower: 0, upper: 10,
[1,2,3,-7,-5,-7,-5,5]

*/
const test = () => {
    const params = [
        {
            input: {
                nums: [1, 1, 1, -10, 2, -2, 2, 10], lower: 0, upper: 10,
            },
            output: 17,
        },
        {
            input: {
                nums: [-2,5,-1], lower: -2, upper: 2
            },
            output: 3,
        },
        {
            input: {
                nums: [0], lower: 0, upper: 0
            },
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums, lower, upper } = input;

        const result = countRangeSum(nums, lower, upper);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();