function countCompleteSubarrays(nums: number[]): number {
    const uniqueTotal: Set<number> = new Set();
    for (const num of nums) {
        uniqueTotal.add(num);
    }

    let res: number = 0;
    const currentNums: Map<number, number> = new Map();
    let leftId: number = 0;

    for (let rightId: number = 0; rightId < nums.length; ++rightId) {
        const num: number = nums[rightId];

        currentNums.set(num, (currentNums.get(num) || 0) + 1);

        while (currentNums.size === uniqueTotal.size) {
            const first: number = nums[leftId];
            leftId += 1;

            const count: number = currentNums.get(first) - 1;
            if (count === 0) {
                currentNums.delete(first);
            } else {
                currentNums.set(first, count)
            }

            res += (nums.length - rightId);
        }
    }

    return res;
};

/*
0 1 2 3 4 5
1,3,1,2,2

 */
const test = () => {
    const params = [
        {
            input: {
                nums: [1,3,1,2,2],
            },
            output: 4,
        },
        {
            input: {
                nums: [5,5,5,5],
            },
            output: 10,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums } = input;

        const result = countCompleteSubarrays(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();