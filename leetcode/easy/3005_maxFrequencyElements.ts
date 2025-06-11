function maxFrequencyElements(nums: number[]): number {
    const frequency: number[] = new Array(101).fill(0);
    let maxFreq: number = 0;

    for (const num of nums) {
        frequency[num] += 1;
        maxFreq = Math.max(maxFreq, frequency[num]);
    }

    return frequency.reduce((acc: number, val: number) => {
        if (val === maxFreq) {
            acc += val;
        }
        return acc;
    }, 0);
};

const test = () => {
    const params = [
        {
            input: [1,2,2,3,1,4],
            output: 4,
        },
        {
            input: [1,2,3,4,5],
            output: 5,
        },
    ];

    params.forEach(({input, output}) => {
        const result = maxFrequencyElements(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();

