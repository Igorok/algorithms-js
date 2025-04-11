function canPartitionKSubsets_0(nums: number[], k: number): boolean {
    const sumOfArr: number = nums.reduce((acc: number, val: number) => acc + val, 0);
    if ((sumOfArr % k) !== 0) {
        return false;
    }

    const arr = [...nums].sort((a: number, b: number) => b - a);
    const target: number = sumOfArr / k;
    const visited: number[] = new Array(nums.length).fill(0);

    const getSumInArr = (id: number, sum: number): boolean => {
        if (sum === target) {
            return true;
        }
        if (id >= arr.length) {
            return false;
        }

        if (visited[id] === 0) {
            visited[id] = 1;
            let r: boolean = getSumInArr(id + 1, sum + arr[id]);
            if (r) {
                return r;
            }
            visited[id] = 0;
        }

        return getSumInArr(id + 1, sum);
    };

    for (let i = 0; i < k; ++i) {
        if (!getSumInArr(0, 0)) {
            return false;
        }
    }

    return true;
};

function canPartitionKSubsets(nums: number[], k: number): boolean {
    const sumOfArr: number = nums.reduce((acc: number, val: number) => acc + val, 0);
    if ((sumOfArr % k) !== 0) {
        return false;
    }

    nums = nums.sort((a, b) => a - b);
    const target: number = sumOfArr / k;
    let visited: number[] = new Array(nums.length).fill(0);


    const getSubsets = (id: number, sum: number, countOfSub: number): boolean => {
        if (countOfSub === 0) {
            return true;
        }
        if (sum === target) {
            return getSubsets(0, 0, countOfSub - 1);
        }

        for (let i: number = id; i < nums.length; ++i) {
            if (visited[i] === 1) {
                continue;
            }
            if (sum + nums[i] > target) {
                break;
            }

            visited[i] = 1;
            const r: boolean = getSubsets(i + 1, sum + nums[i], countOfSub);
            if (r) {
                return r;
            }
            visited[i] = 0;
        }

        return false;
    };


    return getSubsets(0, 0, k);
};

/*

[10,10,10,9,9,9,8,7,6,5,5,4,4,4,3,2]
5
21
[10,10,10,9,9,9,8,7,6,5,5,4,4,4,3,2]
[10,10,9,9,8,7,6,5,5,4,4,4,3] 10 9 2
[10,9,9,7,6,5,5,4,4,4] 10 8 3
[9,9,6,5,5,4,4] 10 7 4
[9,9,6,5,5,4,4]





*/

const test = () => {
    const params = [
        {
            input: [[4,3,2,3,5,2,1], 4],
            output: true,
        },
        {
            input: [[1,1,1,1,2,2,2,2], 2],
            output: true,
        },
        {
            input: [[1,1,1,1,2,2,2,2], 3],
            output: true,
        },
        {
            input: [[4,4,4,6,1,2,2,9,4,6], 3],
            output: true,
        },
        {
            input: [[1,2,3,4], 3],
            output: false,
        },
        {
            input: [[10,12,1,2,10,7,5,19,13,1], 4],
            output: true,
        },
        {
            input: [[4,5,9,3,10,2,10,7,10,8,5,9,4,6,4,9], 5],
            output: true,
        },
        {
            input: [[9,10,14,8,15,7,15,12,15,13,10,14,9,11,9,14], 5],
            output: true,
        },

    ];

    params.forEach(({input, output}) => {
        const nums: number[] = input[0] as number[];
        const k: number = input[1] as number;
        const result = canPartitionKSubsets(nums, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();