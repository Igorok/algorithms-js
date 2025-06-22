function findLonely(nums: number[]): number[] {
    const count: number[] = new Array(1 + 10**6).fill(0);
    const res: number[] = [];

    for (const num of nums) {
        count[num] += 1;
    }

    for (const num of nums) {
        if (count[num] > 1) {
            continue;
        }
        if (num - 1 > -1 && count[num - 1]) {
            continue;
        }
        if (num + 1 < count.length && count[num + 1]) {
            continue;
        }

        res.push(num);
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: {
                nums: [10,6,5,8]
            },
            output: [10,8],
        },
        {
            input: {
                nums: [1,3,5,3]
            },
            output: [1,5],
        },
    ];

    params.forEach(({input, output}) => {
        const { nums } = input;
        const result = findLonely(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

