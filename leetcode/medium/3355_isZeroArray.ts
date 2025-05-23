function isZeroArray_0(nums: number[], queries: number[][]): boolean {
    for (const [s, e] of queries) {
        for (let i = s; i < Math.max(nums.length, e+1); ++i) {
            nums[i] = Math.max(nums[i]-1, 0);
        }
    }

    for (let i = 0; i < nums.length; ++i) {
        if (nums[i] !== 0) {
            return false;
        }
    }

    return true;
};


function isZeroArray(nums: number[], queries: number[][]): boolean {
    const marks: number[] = new Array(nums.length + 1).fill(0);

    for (const [s, e] of queries) {
        marks[s] -= 1;
        marks[Math.min(nums.length + 1, e + 1)] += 1;
    }

    let diff: number = 0;
    for (let i = 0; i < nums.length; ++i) {
        diff += marks[i];
        if (nums[i] + diff > 0) {
            return false;
        }
    }

    return true;
};

const test = () => {
    const params = [
        {
            input: {
                nums: [1, 0, 1], queries: [[0, 2]]
            },
            output: true,
        },
        {
            input: {
                nums: [4,3,2,1], queries: [[1,3],[0,2]]
            },
            output: false,
        },

    ];

    params.forEach(({input, output}) => {
        const { nums, queries } = input;
        const result = isZeroArray(nums, queries);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();