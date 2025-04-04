function maximumTripletValue(nums: number[]): number {
    const postfix: number[] = new Array(nums.length).fill(0);
    postfix[nums.length - 1] = nums[nums.length - 1];
    for (let i = nums.length - 2; i > -1; --i) {
        postfix[i] = Math.max(postfix[i+1], nums[i]);
    }

    let res: number = 0;
    let prev: number = nums[0];

    for (let i: number = 1; i < nums.length - 1; ++i) {
        const r: number = (prev - nums[i]) * postfix[i+1];
        res = Math.max(res, r);
        prev = Math.max(prev, nums[i]);
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: [12,6,1,2,7],
            output: 77,
        },
        {
            input: [1,10,3,4,19],
            output: 133,
        },
        {
            input: [1,2,3],
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const result = maximumTripletValue(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();