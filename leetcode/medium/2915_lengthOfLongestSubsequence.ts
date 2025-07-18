function lengthOfLongestSubsequence(nums: number[], target: number): number {
    const length: number[] = new Array(target + 1).fill(0);

    for (const num of nums) {
        for (let i: number = target-num; i > -1; --i) {
            if (!length[i]) {
                continue;
            }
            length[i + num] = Math.max(length[i + num], length[i]+1);
        }

        length[num] = Math.max(length[num], 1);
    }

    return length[target] ? length[target] : -1;
};

const test = () => {
    const params = [
        {
            input: {
                nums: [1,2,3,4,5], target: 9,
            },
            output: 3,
        },
        {
            input: {
                nums: [4,1,3,2,1,5], target: 7,
            },
            output: 4,
        },
        {
            input: {
                nums: [1,1,5,4,5], target: 3,
            },
            output: -1,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums, target } = input;
        const result = lengthOfLongestSubsequence(nums, target);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();