function zeroFilledSubarray(nums: number[]): number {
    // const getCount = (left: number, right: number) => {
    //     const length: number = right - left;
    //     let r: number = 0;
    //     for (let i: number = 1; i <= length; ++i) {
    //         r += i;
    //     }
    //     return r;
    // };

    const getCount = (left: number, right: number) => {
        const length: number = right - left;
        return (1 + length) * length / 2;
    };

    let res: number = 0;
    let left: number = -1;
    for (let right: number = 0; right < nums.length; ++right) {
        if (nums[right] === 0 && left === -1) {
            left = right;
            continue;
        }

        if (nums[right] !== 0 && left !== -1) {
            res += getCount(left, right);
            left = -1;
        }
    }

    if (left !== -1) {
        res += getCount(left, nums.length);
    }

    return res;
};

/*
0
1 - 1

0 0
1 - 2
2 - 1

0 0 0
1 - 3
2 - 2
3 - 1

0 0 0 0
1 - 4
2 - 3
3 - 2
4 - 1

0 0 0 0 0
1 - 5
2 - 4
3 - 3
4 - 2
5 - 1

*/

const test = () => {
    const params = [
        {
            input: {
                nums: [1,3,0,0,2,0,0,4],
            },
            output: 6,
        },
        {
            input: {
                nums: [0,0,0,2,0,0],
            },
            output: 9,
        },
        {
            input: {
                nums: [2,10,2019],
            },
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums } = input;
        const result = zeroFilledSubarray(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();