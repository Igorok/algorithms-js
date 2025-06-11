function maxFrequency(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);

    const diffs: number[] = [];
    for (let i: number = 0; i < nums.length; ++i) {
        const prevId: number = (nums.length + i - 1) % nums.length;
        diffs.push(Math.abs(nums[i] - nums[prevId]));
    }



    return 0;
};

/*


*/

const test = () => {
    const params = [
        {
            input: {
                nums: [1,2,4], k: 5
            },
            output: 3,
        },
        {
            input: {
                nums: [1,4,8,13], k: 5
            },
            output: 2,
        },
        {
            input: {
                nums: [3,9,6], k: 2
            },
            output: 1,
        },
        {
            input: {
                nums: [1,1,1,1,5,6,7,7], k: 9
            },
            output: 5,
            // 9 - 1 - 2 -6
        },
    ];

    params.forEach(({input, output}) => {
        const { nums, k } = input;
        const result = maxFrequency(nums, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

