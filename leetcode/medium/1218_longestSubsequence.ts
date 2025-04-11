function longestSubsequence(arr: number[], difference: number): number {
    const prevNumbers: Map<number, number> = new Map();

    let res: number = 0;
    for (const num of arr) {
        const prevNum: number = num - difference;
        const prevCount: number = prevNumbers.get(prevNum) || 0;
        const currentCount = prevCount + 1;
        prevNumbers.set(num, currentCount);

        res = Math.max(res, currentCount);
    }

    return res;
};

const test = () => {
    const params = [
        {
            input: [[1,2,3,4], 1],
            output: 4,
        },
        {
            input: [[1,3,5,7], 1],
            output: 1,
        },
        {
            input: [[1,5,7,8,5,3,4,2,1], -2],
            output: 4,
        },
    ];

    params.forEach(({input, output}) => {
        const arr: number[] = input[0] as number[];
        const difference: number = input[1] as number;
        const result = longestSubsequence(arr, difference);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();
