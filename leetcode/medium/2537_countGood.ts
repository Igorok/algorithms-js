
function countGood(nums: number[], k: number): number {
    const count: Map<number, number> = new Map();
    count.set(nums[0], 1);

    let countPairs: number = 0;
    let start: number = 0;
    let res: number = 0;

    for (let i: number = 1; i < nums.length; ++i) {
        const num: number = nums[i];
        const cnt: number = count.get(num) || 0;
        count.set(num, cnt + 1);

        countPairs += cnt;

        while (countPairs >= k) {
            const startNum: number = nums[start];
            const cntForDelete: number = (count.get(startNum) || 0) - 1;
            if (countPairs - cntForDelete < k) {
                break;
            }
            count.set(startNum, cntForDelete);
            countPairs -= cntForDelete;
            start += 1;
        }

        if (countPairs >= k) {
            res += (start + 1);
        }

    }

    return res;
};

/*
1,1,1,1,1
0 1 3 6 10

---
 0 1 2 3 4 5 6
[3,1,4,3,2,2,4], 2

res = 1
memo = [0, 0, 0, 1, 1, 2, 3]
pairs = [3,2,4]
ids = {
    3: [0,3],
    1: [1,],
    4: [2,6],
    2: [4,5],
}

---
2
0 1 2 3 4 5 6
3,1,4,3,2,2,4

0 1 2 3 4 5 6
0 0 0 1 1 2 2

{
    3: 2,
    1: 1,
    4: 2,
    2: 2,
}
start = 0+2

res = 1+3


---
10
1,2,1,1,1,1, 2
0 0 1 3 6 10 1

*/

const test = () => {
    const params = [
        {
            input: [[3,1,4,3,2,2,4], 2],
            output: 4,
        },
        {
            input: [[1,1,1,1,1], 10],
            output: 1,
        },
        {
            input: [[1,2,1,1,1,1,2], 10],
            output: 2,
        },

    ];

    params.forEach(({input, output}) => {
        const nums: number[] = input[0] as number[];
        const k: number = input[1] as number;
        const result = countGood(nums, k);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();