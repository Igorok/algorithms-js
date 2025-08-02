function reductionOperations(nums: number[]): number {
    nums.sort((a, b) => a - b);
    const levels: number[] = [];

    let num: number = nums[0];
    let cnt: number = 1;

    for (let i: number = 1; i < nums.length; ++i) {
        if (nums[i] === num) {
            cnt += 1;
            continue;
        }
        levels.push(cnt);
        cnt = 1;
        num = nums[i];
    }
    levels.push(cnt);

    let res: number = 0;
    for (let i: number = levels.length - 1; i > 0; --i) {
        res += levels[i];
        levels[i-1] += levels[i];
    }


    return res;
};

/*

[1,1,2,2,3]

4
2
1



*/


const test = () => {
    const params = [
        {
            input: {
                nums: [5,1,3]
            },
            output: 3,
        },
        {
            input: {
                nums: [1,1,1]
            },
            output: 0,
        },
        {
            input: {
                nums: [1,1,2,2,3]
            },
            output: 4,
        },
    ];

    params.forEach(({ input, output }) => {
        const { nums } = input;
        const result = reductionOperations(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output)
                ? "SUCCESS "
                : "ERROR ",
            "input",
            JSON.stringify(input),
            "output",
            output,
            "result",
            result,
        );
    });
};

test();
