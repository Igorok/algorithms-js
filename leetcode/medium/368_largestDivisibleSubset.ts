function largestDivisibleSubset(nums: number[]): number[] {
    const arr: number[] = [...nums].sort((a: number, b: number) => a - b);
    const lengths: number[] = new Array(arr.length).fill(1);
    let maxLengthId = 0;

    for (let i: number = 0; i < arr.length; ++i) {
        let length = 1;
        for (let j: number = i - 1; j > -1; --j) {
            if ((arr[i] % arr[j]) === 0) {
                length = Math.max(length, lengths[j] + 1);
            }
        }
        lengths[i] = length;
        if (lengths[i] > lengths[maxLengthId]) {
            maxLengthId = i;
        }
    }

    const res: number[] = [];

    for (let i: number = maxLengthId; i > -1; --i) {
        if ((arr[maxLengthId] % arr[i]) === 0 && lengths[maxLengthId] - 1 === lengths[i]) {
            res.push(arr[maxLengthId]);
            maxLengthId = i;
        }
    }
    res.push(arr[maxLengthId]);

    return res;
};


const test = () => {
    const params = [
        {
            input: [1,2,3],
            output: [1,2],
        },
        {
            input: [1,2,4,8],
            output: [1,2,4,8],
        },
    ];

    params.forEach(({input, output}) => {
        const result = largestDivisibleSubset(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();