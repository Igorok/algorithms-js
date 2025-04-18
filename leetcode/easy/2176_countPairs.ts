function countPairs(nums: number[], k: number): number {
    let res: number = 0;

    const idsByNumber: Map<number, number[]> = new Map();

    for (let i: number = 0; i < nums.length; ++i) {
        const num: number = nums[i];
        const ids: number[] = idsByNumber.get(num) || [];

        for (const id of ids) {
            if (((i * id) % k) === 0) {
                res += 1;
            }
        }

        ids.push(i);
        idsByNumber.set(num, ids);
    }

    return res;
};

/*

[3,1,2,2,2,1,3], 2

3,1,2,2,2,1,3
{
3: 2
1: 2
2: 3
}


*/

const test = () => {
    const params = [
        {
            input: [[3,1,2,2,2,1,3], 2],
            output: 4,
        },
        {
            input: [[1,2,3,4], 1],
            output: 0,
        },
    ];

    params.forEach(({input, output}) => {
        const nums = input[0] as number[]
        const k = input[1] as number
        const result = countPairs(nums, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();