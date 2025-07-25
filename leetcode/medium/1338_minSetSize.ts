function minSetSize(arr: number[]): number {
    let nums: number[] = new Array(2 + 10**5).fill(0);
    for (const num of arr) {
        nums[num] += 1;
    }
    nums = nums
        .filter((n: number) => n !== 0)
        .sort((a, b) => (b - a));

    let sum: number = 0;
    let count: number = 0;
    const half: number = Math.ceil(arr.length / 2);

    for (const num of nums) {
        sum += num;
        count += 1;

        if (sum >= half) {
            return count;
        }
    }

    return 0;
};

const test = () => {
    const params = [
        {
            input: {
                arr: [3,3,3,3,5,5,5,2,2,7],
            },
            output: 2,
        },
        {
            input: {
                arr: [7,7,7,7,7,7]
            },
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const { arr } = input;

        const result = minSetSize(arr);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();