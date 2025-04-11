function longestArithSeqLength(nums: number[]): number {
    let maxCount: number = 1;
    const countOfDiffs: Map<number, number>[] = nums.map(() => new Map());

    for (let i: number = 1; i < nums.length; ++i) {
        for (let j = i - 1; j > -1; --j) {
            const diff: number = nums[i] - nums[j];

            const diffCount = countOfDiffs[i].get(diff) || 0;
            const prevDiffCount = countOfDiffs[j].get(diff) || 0;
            const count: number = Math.max(diffCount, prevDiffCount + 1);

            countOfDiffs[i].set(diff, count);
            maxCount = Math.max(maxCount, count);
        }
    }

    return maxCount + 1;
};

/*
3,6,9,12
6 - 3
9 - 3, 6
12 - 3,

---

9,4,7,2,10
9
4 - -5
7 - 3, -2
2 - -5, -2, -7
10 - 8, 3, 6, 1

---

*/

const test = () => {
    const params = [
        {
            input: [3,6,9,12],
            output: 4,
        },
        {
            input: [9,4,7,2,10],
            output: 3,
        },
        {
            input: [20,1,15,3,10,5,8],
            output: 4,
        },
        {
            input: [22,8,57,41,36,46,42,28,42,14,9,43,27,51,0,0,38,50,31,60,29,31,20,23,37,53,27,1,47,42,28,31,10,35,39,12,15,6,35,31,45,21,30,19,5,5,4,18,38,51,10,7,20,38,28,53,15,55,60,56,43,48,34,53,54,55,14,9,56,52],
            output: 6,
        },
    ];

    params.forEach(({input, output}) => {
        const nums = input as number[];

        const result = longestArithSeqLength(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();