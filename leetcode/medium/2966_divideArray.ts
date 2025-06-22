function divideArray(nums: number[], k: number): number[][] {
    nums.sort((a, b) => a - b);

    const res: number[][] = [];
    let acc: number[] = [];

    for (let i: number = 0; i < nums.length; ++i) {
        if (acc.length === 0) {
            acc.push(nums[i]);
            continue;
        }

        if (nums[i] - acc[0] > k) {
            return [];
        }

        acc.push(nums[i]);

        if (acc.length === 3) {
            res.push([...acc]);
            acc = [];
        }
    }

    return res;
};


const test = () => {
    const params = [
        {
            input: {
                nums: [1,3,4,8,7,9,3,5,1], k: 2
            },
            output: [[1,1,3],[3,4,5],[7,8,9]],
        },
        {
            input: {
                nums: [2,4,2,2,5,2], k: 2,
            },
            output: [],
        },
        {
            input: {
                nums: [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k: 14
            },
            output: [[2,2,12],[4,8,5],[5,9,7],[7,8,5],[5,9,10],[11,12,2]],
        },
    ];

    params.forEach(({input, output}) => {
        const { nums, k } = input;
        const result = divideArray(nums, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();