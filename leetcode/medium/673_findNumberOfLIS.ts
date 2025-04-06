function findNumberOfLIS(nums: number[]): number {

    let maxLength: number = 1;
    let lengths: number[] = new Array(nums.length).fill(1);
    let paths: number[] = new Array(nums.length).fill(1);

    for (let i: number = 0; i < nums.length; ++i) {
        for (let j: number = i - 1; j > -1; --j) {
            if (nums[j] < nums[i]) {
                if (lengths[j] + 1 > lengths[i]) {
                    lengths[i] = lengths[j] + 1;
                    paths[i] = paths[j]
                } else if (lengths[j] + 1 == lengths[i]) {
                    paths[i] += paths[j];
                }
                maxLength = Math.max(maxLength, lengths[i]);
            }
        }
    }

    let res: number = lengths.reduce((acc: number, val: number, id: number) => {
        if (val === maxLength) {
            acc += paths[id];
        }

        return acc;
    }, 0);

    return res;
};

/*

1,3,5,4,7
1 2 3 3 4

*/

const test = () => {
    const params = [
        {
            input: [1,3,5,4,7],
            output: 2,
        },
        {
            input: [2,2,2,2,2],
            output: 5,
        },
        {
            input: [1,3,3,3,3,5,4,7],
            output: 8,
        },
        {
            input: [3,4,5,0,1,2],
            output: 2,
        },
    ];

    params.forEach(({input, output}) => {
        const result = findNumberOfLIS(input);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', JSON.stringify(output),
            'result', JSON.stringify(result),
        );
    });
};

test();