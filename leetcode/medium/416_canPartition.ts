function canPartition(nums: number[]): boolean {
    const sumOfArr: number = nums.reduce((acc: number, num: number) => acc + num, 0);
    if ((sumOfArr % 2) === 1) {
        return false;
    }
    const half: number = sumOfArr / 2;
    const arr: number[] = [...nums].sort((a: number, b: number) => a - b);

    let prev: number[] = new Array(half + 1).fill(0)
    let curr: number[] = new Array(half + 1).fill(0)

    for (const num of arr) {
        for (let i: number = 1; i < half + 1; ++i) {
            const diff: number = i - num;
            if (diff < 0) {
                curr[i] = prev[i];
            }
            if (diff === 0) {
                curr[i] = 1;
            }
            if (diff > 0) {
                if (prev[diff] != 0) {
                    curr[i] = 1 + prev[diff];
                } else {
                    curr[i] = prev[i];
                }
            }
            if (curr[half] != 0) {
                return true;
            }
        }
        prev = curr;
        curr = new Array(half + 1).fill(0)
    }

    return false;
};

/*

1, 1, 2, 5, 5, 10
12
    1 2 3 4 5 6 7 8 9 10 11 12
1   1 0 0 0 0 0 0 0 0 0  0  0
1   1 2 0 0 0 0 0 0 0 0  0  0
2   1 1 2 3
5
5
10

*/

const test = () => {
    const params = [
        {
            input: [23,13,11,7,6,5,5],
            output: true,
        },
        {
            input: [1,2,5],
            output: false,
        },
        {
            input: [1,1, 2,5,5, 10],
            output: true,
        },
        {
            input: [1,5,11,5],
            output: true,
        },
        {
            input: [1,2,3,5],
            output: false,
        },
    ];

    params.forEach(({input, output}) => {
        const result = canPartition(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();