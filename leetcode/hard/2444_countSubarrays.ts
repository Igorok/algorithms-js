function countSubarrays(nums: number[], minK: number, maxK: number): number {
    let start: number = -1;
    let minId: number = -1;
    let maxId: number = -1;
    let res: number = 0;

    for (let i = 0; i < nums.length; ++i) {
        if (nums[i] === minK) {
            minId = i;
        }
        if (nums[i] === maxK) {
            maxId = i;
        }

        if (nums[i] > maxK || nums[i] < minK) {
            start = i;
            minId = -1;
            maxId = -1;
        }

        if (minId === -1 || maxId === -1) {
            continue;
        }

        res += Math.min(minId, maxId) - start;
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: { nums: [1,3,5,2,7,5], minK: 1, maxK: 5 },
            output: 2,
        },
        {
            input: { nums: [1,1,1,1], minK: 1, maxK: 1 },
            output: 10,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums, minK, maxK } = input;

        const result = countSubarrays(nums, minK, maxK);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();