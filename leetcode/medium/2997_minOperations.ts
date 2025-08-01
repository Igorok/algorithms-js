function minOperations(nums: number[], k: number): number {
    let total: number = nums.reduce((acc: number, num: number) => acc ^ num, 0);

    let res: number = 0;
    for (let i: number = 0; i < 32; ++i) {
        if (total === k) {
            return res;
        }
        const tBit: number = total & 1;
        const kBit: number = k & 1;
        if (tBit !== kBit) {
            res += 1;
        }
        total = total >> 1;
        k = k >> 1;
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                nums: [2,0,2,0], k: 0
            },
            output: 0,
        },
        {
            input: {
                nums: [2,1,3,4], k: 1,
            },
            output: 2,
        },

    ];

    params.forEach(({input, output}) => {
        const { nums, k } = input;
        const result = minOperations(nums, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();