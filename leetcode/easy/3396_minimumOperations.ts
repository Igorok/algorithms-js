function minimumOperations(nums: number[]): number {
    if (nums.length < 2) return 0;

    const countOfNumbers: Map<number, number> = nums.reduce((acc: Map<number, number>, num: number) => {
        const count: number = acc.get(num) || 0;
        acc.set(num, count + 1);
        return acc;
    }, new Map());

    if (countOfNumbers.size === nums.length) {
        return 0;
    }

    let res: number = 0;
    let i: number = 0;

    while (i < nums.length) {
        res += 1;
        for (let j: number = i; j < Math.min(i + 3, nums.length); ++j) {
            const num: number = nums[j];
            const count: number = (countOfNumbers.get(num) || 0) - 1;

            if (count === 0) {
                countOfNumbers.delete(num);
            } else {
                countOfNumbers.set(num, count);
            }
        }
        i = Math.min(i + 3, nums.length);

        const size: number = countOfNumbers.size;
        const length: number = nums.length - i;
        if (size === length) {
            return res;
        }
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: [1,2,3,4,2,3,3,5,7],
            output: 2,
        },
        {
            input: [4,5,6,4,4],
            output: 2,
        },
        {
            input: [6,7,8,9],
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const nums: number[] = input;
        const result = minimumOperations(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();