const findLeft = (start: number, lower: number, upper: number, arr: number[]): number|null => {
    let res: number | null = null;

    let s: number = start + 1;
    let e: number = arr.length - 1;

    while (s <= e) {
        const m: number = Math.floor((s + e) / 2);

        if (arr[m] + arr[start] > upper) {
            e = m - 1;
        } else if (arr[m] + arr[start] < lower) {
            s = m + 1;
        } else {
            res = m;
            e = m - 1;
        }
    }

    return res;
}

const findRight = (start: number, lower: number, upper: number, arr: number[]): number|null => {
    let res: number | null = null;

    let s: number = start + 1;
    let e: number = arr.length - 1;

    while (s <= e) {
        const m: number = Math.floor((s + e) / 2);

        if (arr[m] + arr[start] > upper) {
            e = m - 1;
        } else if (arr[m] + arr[start] < lower) {
            s = m + 1;
        } else {
            res = m;
            s = m + 1;
        }
    }

    return res;
}

function countFairPairs(nums: number[], lower: number, upper: number): number {
    let res: number = 0;
    const arr: number[] = [...nums].sort((a, b) => a - b);

    for (let i: number = 0; i < arr.length - 1; ++i) {
        const left: number|null = findLeft(i, lower, upper, arr);
        const right: number|null = findRight(i, lower, upper, arr);

        if (left === null || right === null) {
            continue;
        }

        res += right + 1 - left;
    }

    return res;
};

/*

0 <= i < j < n
lower <= nums[i] + nums[j] <= upper

[0,1,7,4,4,5], 3, 6
0 1 2 3 4 5
0,1,7,4,4,5

0 1 3 4 5 2
0 1 4 4 5 7




---


---

[1,7,9,2,5], 11, 11

0 1 2 3 4
1,7,9,2,5








*/


const test = () => {
    const params = [
        {
            input: [[0,1,7,4,4,5], 3, 6],
            output: 6,
        },
        {
            input: [[1,7,9,2,5], 11, 11],
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const nums = input[0] as number[];
        const lower = input[1] as number;
        const upper = input[2] as number;

        const result = countFairPairs(nums, lower, upper);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();