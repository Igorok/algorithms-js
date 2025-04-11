function minOperations(nums: number[], k: number): number {
    const arr: number[] = Array.from(new Set(nums)).sort((a: number, b: number) => a - b);

    if (arr[0] < k) {
        return -1;
    } else if (arr[0] === k) {
        return arr.length -1;
    }

    return arr.length;
};

const test = () => {
    const params = [
        {
            input: [[5,2,5,4,5], 2],
            output: 2,
        },
        {
            input: [[2,1,2], 2],
            output: -1,
        },
        {
            input: [[9,7,5,3], 1],
            output: 4,
        },
    ];

    params.forEach(({input, output}) => {
        const nums = input[0] as number[];
        const k = input[1] as number;

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