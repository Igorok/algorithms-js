function findDuplicates_0(nums: number[]): number[] {
    const count: number[] = new Array(nums.length).fill(0);
    for (let i: number = 0; i < nums.length; ++i) {
        count[nums[i] - 1] += 1;
    }

    const visited: number[] = [];
    for (let i: number = 0; i < nums.length; ++i) {
        if (count[i] === 2) {
            visited.push(i + 1);
        }
    }

    return visited;
};

function findDuplicates(nums: number[]): number[] {
    const res: number[] = [];

    const dfs = (id: number) => {
        const i: number = id - 1;
        if (nums[i] < 0) {
            res.push(id);
            return;
        }

        const v: number = nums[i];
        nums[i] = -1;

        if (v !== 0)
        dfs(v)
    };

    for (let i: number = 0; i < nums.length; ++i) {
        if (nums[i] < 0) continue;
        const v: number = nums[i];
        nums[i] = 0;
        dfs(v);
    }

    return res;
};

/*

[4,3,2,7,8,2,3,1]

  0  1  2  3  4  5  6  7
-1, -1,-1,-1,-1,-1,-1,-1

3 +
4 +
2 +




*/

const test = () => {
    const params = [
        {
            input: {
                nums: [4,3,2,7,8,2,3,1]
            },
            output: [2,3],
        },
        {
            input: {
                nums: [1,1,2]
            },
            output: [1],
        },
        {
            input: {
                nums: [1]
            },
            output: [],
        },
    ];

    params.forEach(({input, output}) => {
        const { nums } = input;
        const result = findDuplicates(nums);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();