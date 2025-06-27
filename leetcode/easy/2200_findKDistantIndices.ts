function findKDistantIndices(nums: number[], key: number, k: number): number[] {
    const checkIndex = (id: number) => {
        const start: number = Math.max(0, id - k);
        const end: number = Math.min(nums.length - 1, id + k);

        for (let i: number = start; i <= end; ++i) {
            if (nums[i] === key) {
                return true;
            }
        }

        return false;
    };

    const res: number[] = [];

    for (let i: number = 0; i < nums.length; ++i) {
        if (checkIndex(i)) {
            res.push(i);
        }
    }

    return res;
};


const test = () => {
    const params = [
        {
            input: {
                nums: [3,4,9,1,3,9,5], key: 9, k: 1,
            },
            output: [1,2,3,4,5,6],
        },
        {
            input: {
                nums: [2,2,2,2,2], key: 2, k: 2,
            },
            output: [0,1,2,3,4],
        },
    ];

    params.forEach(({input, output}) => {
        const { nums, key, k } = input;
        const result: number[] = findKDistantIndices(nums, key, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();
