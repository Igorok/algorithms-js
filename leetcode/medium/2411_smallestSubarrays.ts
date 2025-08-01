function smallestSubarrays(nums: number[]): number[] {
    const countOfBits: number[][] = new Array(nums.length+1).fill(0).map(() => new Array(32).fill(0));

    for (let i: number = nums.length - 1; i > -1; --i) {
        let n: number = nums[i];

        for (let j: number = 0; j < 32; ++j) {
            countOfBits[i][j] += countOfBits[i+1][j];
            countOfBits[i][j] += n & 1;
            n = n >> 1;
        }
    }

    const getDiff = (arr1: number[], arr2: number[]) => {
        let n: number = 0;

        for (let i: number = 31; i > -1; --i) {
            if (arr1[i] - arr2[i] > 0) {
                n = n | 1;
            }
            if (i > 0) {
                n = n << 1;
            }
        }

        return n;
    };

    const search = (s: number, e: number): number => {
        let start = s;
        let end = e+1;
        const num: number = getDiff(countOfBits[s], new Array(32).fill(0));

        let res: number = end;

        while (start <= end) {
            const middle: number = Math.floor((start + end) / 2);
            const curr: number = getDiff(countOfBits[s], countOfBits[middle]);

            if (curr < num) {
                start = middle + 1;
            } else {
                res = middle;
                end = middle - 1;
            }
        }

        return res;
    };

    const res: number[] = new Array(nums.length).fill(0);
    res[res.length - 1] = 1;

    for (let i: number = 0; i < nums.length - 1; ++i) {
        const right: number = search(i, nums.length - 1);
        res[i] = right - i || 1;
    }

    return res;
};


/*



*/

const test = () => {
    const params = [
        {
            input: {
                nums: [0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,32,2,0,0,0,0,0,0,28,16,32,0,0,0,0,0,0,0,1,0,8,0,0,0,0,0,0,0,0,0,32,0,0,0,0,0,0,0,0,16,0,0,0,0,2,0,0,32,0,0,0,4,16,0,4,0,32,0,0,8,0,1,1,0,0,0,0,0],
            },
            output: [36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,43,42,41,40,39,38,37,43,42,41,40,39,38,37,36,35,34,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,1,1,1,1,1,1],
        },
        {
            input: {
                nums: [1,0,2,1,3],
            },
            output: [3,3,2,2,1],
        },
        {
            input: {
                nums: [1,2],
            },
            output: [2,1],
        },
    ];

    params.forEach(({ input, output }) => {
        const { nums } = input;
        const result = smallestSubarrays(nums);

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
