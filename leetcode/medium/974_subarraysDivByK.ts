function subarraysDivByK(nums: number[], k: number): number {
    nums = nums.map((n) => ((n % k) + k) % k);

    const prefix: number[] = [];
    prefix[0] = nums[0] % k;
    for (let i = 1; i < nums.length; ++i) {
        prefix[i] = (nums[i] + prefix[i-1]) % k;
    }

    console.log(
        'nums', nums, '\n',
        'prefix', prefix,
    );

    let res: number = 0;
    const remaindersOfSum = new Map();
    remaindersOfSum.set(0, 1);
    for (let i: number = 0; i < nums.length; ++i) {
        const sumMod: number = prefix[i];
        const count: number = remaindersOfSum.get(sumMod) || 0;
        res += count;
        remaindersOfSum.set(sumMod, count + 1);
    }

    return res;
};

/*
nums    [ 4, 0, 0, 3, 2, 1 ]
prefix  [ 4, 4, 4, 2, 4, 0 ]
SUCCESS  input {"nums":[4,5,0,-2,-3,1],"k":5} output 7 result 7

0 +  1 + 2 + 0 + 3 + 1 = 7


*/

const test = () => {
    const params = [
        {
            input: { nums: [4,5,0,-2,-3,1], k: 5 },
            output: 7,
        },
        {
            input: { nums: [5], k: 9 },
            output: 0,
        },
        {
            input: { nums: [-1, 2, 9], k: 2 },
            output: 2,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums, k } = input;

        const result = subarraysDivByK(nums, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();