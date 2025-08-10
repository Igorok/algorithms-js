function countRangeSum_0(nums: number[], lower: number, upper: number): number {
    let res: number = 0;

    const prefixSum: number[] = new Array(nums.length).fill(0);
    prefixSum[0] = nums[0];

    for (let i: number = 1; i < nums.length; ++i) {
        prefixSum[i] = nums[i] + prefixSum[i-1];
    }

    for (let i: number = 0; i < nums.length; ++i) {
        for (let j: number = i; j < nums.length; ++j) {
            const s: number = prefixSum[j] - (i > 0 ? prefixSum[i-1] : 0);

            if (s >= lower && s <= upper) {
                res += 1;
            }
        }
    }

    return res;
};

function countRangeSum(nums: number[], lower: number, upper: number): number {
    const prefixSum: number[][] = new Array(nums.length).fill(0);
    prefixSum[0] = [nums[0], 0];

    for (let i: number = 1; i < nums.length; ++i) {
        prefixSum[i] = [
            nums[i] + prefixSum[i-1][0],
            prefixSum[i-1][0],
        ];
    }

    console.log('prefixSum', JSON.stringify(prefixSum));


    const findGreater = (arr: number[][], prev: number): number => {
        let start: number = 0;
        let end: number = arr.length - 1;
        let res: number = -1;

        while (start <= end) {
            const middle: number = Math.floor((start + end) / 2);
            if ((arr[middle][0] - prev) >= lower) {
                res = middle;
                end = middle - 1;
            } else {
                start = middle + 1;
            }
        }

        return res;
    };
    const findLess = (arr: number[][], prev: number): number => {
        let start: number = 0;
        let end: number = arr.length - 1;
        let res: number = -1;

        while (start <= end) {
            const middle: number = Math.floor((start + end) / 2);
            if ((arr[middle][0] - prev) <= upper) {
                res = middle;
                start = middle + 1;
            } else {
                end = middle - 1;
            }
        }

        return res;
    };


    let res: number = 0;

    const mSort = (arr: number[][]): number[][] => {
        if (arr.length === 0) {
            return arr;
        }
        if (arr.length === 1) {
            const v: number = arr[0][0] - arr[0][1];
            if (v >= lower && v <= upper) {
                res += 1;
            }
            return arr;
        }

        const middle: number = Math.floor(arr.length / 2);
        const left: number[][] = mSort(arr.slice(0, middle));
        const right: number[][] = mSort(arr.slice(middle));

        for (const [curr, prev] of left) {
            const l: number = findGreater(right, prev);
            if (l === -1) {
                continue;
            }
            const r: number = findLess(right, prev);
            if (r === -1) {
                continue;
            }
            const s: number = r - l + 1;
            if (s > 0) {
                res += s;
            }
        }

        const merged: number[][] = [];

        let i: number = 0;
        let j: number = 0;

        while (i < left.length && j < right.length) {
            if (left[i][0] <= right[j][0]) {
                merged.push(left[i]);
                i += 1;
            } else {
                merged.push(right[j]);
                j += 1;
            }
        }

        while (i < left.length) {
            merged.push(left[i]);
            i += 1;
        }

        while (j < right.length) {
            merged.push(right[j]);
            j += 1;
        }

        return merged;
    };

    const sorted = mSort(prefixSum);


    return res;
};

/*
4+3+2+0+3+3+1+1
nums: [1, 1, 1, -10, 2, -2, 2, 10], lower: 0, upper: 10,
[1,2,3,-7,-5,-7,-5,5]


1 + x = 0;
x = 0 - 1

1 + x = 10;
x = 10 - 1


[[1,0],[2,1],[3,2],[-7,3],[-5,-7],[-7,-5],[-5,-7],[5,-5]]
[1, 1, 1, -10, 2, -2, 2, 10]
[[1,0],[2,1],[3,2],[-7,3],[-5,-7],[-7,-5],[-5,-7],[5,-5]]

[1,0],[2,1],[3,2],[-7,3: -10],
[-5,-7],[-7,-5],[-5,-7],[5,-5]

*/
const test = () => {
    const params = [
        {
            input: {
                nums: [1, 1, 1, -10, 2, -2, 2, 10], lower: 0, upper: 10,
            },
            output: 17,
        },
        {
            input: {
                nums: [-2,5,-1], lower: -2, upper: 2
            },
            output: 3,
        },
        {
            input: {
                nums: [0], lower: 0, upper: 0
            },
            output: 1,
        },
    ];

    params.forEach(({input, output}) => {
        const { nums, lower, upper } = input;

        const result = countRangeSum(nums, lower, upper);

        console.log(
            JSON.stringify(result) === JSON.stringify(output) ? 'SUCCESS ' : 'ERROR ',
            'input', JSON.stringify(input),
            'output', output,
            'result', result,
        );
    });
};

test();