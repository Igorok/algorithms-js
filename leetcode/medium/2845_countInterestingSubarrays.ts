function countInterestingSubarrays_0(nums: number[], modulo: number, k: number): number {
    let res: number = 0;

    for (let i: number = 0; i < nums.length; ++i) {
        let cnt: number = 0;
        for (let j: number = i; j < nums.length; ++j) {
            if ((nums[j] % modulo) === k) {
                cnt += 1;
            }
            if ((cnt % modulo) === k) {
                res += 1;
            }
        }
    }

    return res;
};

function countInterestingSubarrays_1(nums: number[], modulo: number, k: number): number {
    const divisible: number[] = nums.map((n) => (n % modulo) === k ? 1 : 0);
    const prefix: number[] = new Array(nums.length).fill(0);
    prefix[0] = divisible[0] % modulo;
    for (let i: number = 1; i < divisible.length; ++i) {
        prefix[i] = (prefix[i-1] + divisible[i]) % modulo;
    }

    console.log(
        'nums', nums,
        'divisible', divisible,
        'prefix', prefix,
    );


    let res: number = 0;
    const countOfMod = new Map();
    countOfMod.set(0, 1);


    for (let i = 0; i < prefix.length; ++i) {
        const countOfPrefix = countOfMod.get(prefix[i]) || 0;

        const remainder: number = (modulo + prefix[i] - k) % modulo;
        res += (countOfMod.get(remainder) || 0);

        countOfMod.set(prefix[i], countOfPrefix + 1)

    }


    return res;
};

function countInterestingSubarrays(nums: number[], modulo: number, k: number): number {
    let res: number = 0;
    let prefixSum: number = 0;
    const sumOfRemainders: Map<number, number> = new Map();
    sumOfRemainders.set(0, 1);

    for (let i = 0; i < nums.length; ++i) {
        if ((nums[i] % modulo) === k) {
            prefixSum += 1;
            prefixSum %= modulo;
        }

        const remainder: number = (prefixSum - k + modulo) % modulo;
        res += (sumOfRemainders.get(remainder) || 0);

        const countOfPrefixes = sumOfRemainders.get(prefixSum) || 0;
        sumOfRemainders.set(prefixSum, countOfPrefixes + 1);
    }


    return res;
};

/*

nums        [ 3, 2, 4 ]
divisible   [ 1, 0, 0 ]
prefix      [ 1, 1, 1 ]

ERROR  input {"nums":[3,2,4],"modulo":2,"k":1} output 3 result 6




*/

const test = () => {
    const params = [
        {
            input: { nums: [3,2,4], modulo: 2, k: 1 },
            output: 3,
        },
        {
            input: { nums: [3,1,9,6], modulo: 3, k: 0 },
            output: 2,
        },
        {
            input: { nums: [3,2,4, 3,2,4], modulo: 2, k: 1 },
            output: 12,
        },
        {
            input: { nums: [3, 3, 3, 1, 3, 3, 3], modulo: 3, k: 0 },
            output: 8,
        },
        {
            input: { nums: [4,5], modulo: 1, k: 0 },
            output: 3,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums, modulo, k } = input;

        const result = countInterestingSubarrays(nums, modulo, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();