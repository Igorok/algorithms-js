function countSubarrays(nums: number[]): number {
    let res: number = 0;

    for (let i : number = 0; i < nums.length - 1; ++i) {
        const sumOf: number = nums[i-1] + nums[i+1];
        if (nums[i] === sumOf*2) {
            res += 1;
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: { nums: [1,2,1,4,1] },
            output: 1,
        },
        {
            input: { nums: [1,1,1] },
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums } = input;

        const result = countSubarrays(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();